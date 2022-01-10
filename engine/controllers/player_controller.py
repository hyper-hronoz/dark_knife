import re, os, pygame
from types import MethodType
from sys import platform
from listeners import CollisionListener
from models import Player, Platform

class PlayerController:
	def __init__(self, main_loop) -> None:
		self._player_textures = {}
		self._absolute_folder: str = main_loop.absolute_folder
		self._load_next_level: MethodType = main_loop.level_controller.load_next_level

		self.player_listener = CollisionListener()

	def change(self, main_loop) -> None:
		# копии того что о нас есть в главном цикле
		self._level_up_platforms: pygame.sprite.Group = main_loop.level_up_platforms
		self._platforms: pygame.sprite.Group = main_loop.platforms
		self._mobs: pygame.sprite.Group = main_loop.mobs

	def _load_player_textures(self) -> None:
		right_movement_textures_path = os.path.join(
			self._absolute_folder, "resources/images/right_movement_set/")
		self._player_textures["right"] = [pygame.transform.scale(pygame.image.load(
			f"{right_movement_textures_path}right-{i}.png"), (Player.HERO_WIDTH, Player.HERO_HEIGHT)) for i in range(1, 14)]
		left_movement_textures_path = os.path.join(
			self._absolute_folder, "resources/images/left_movement_set/")
		self._player_textures["left"] = [pygame.transform.scale(pygame.image.load(
			f"{left_movement_textures_path}left-{i}.png"), (Player.HERO_WIDTH, Player.HERO_HEIGHT)) for i in range(1, 14)]
		return self._player_textures

	def spawn_player(self, player_position) -> Player:
		x, y = player_position
		self.player = Player(x, y)
		self.player.is_moves = False
		return self.player

	def _return_player_to_normal_vertical_position(self, *args) -> None:
		platform: Platform = args[0]
		if self.player.direction.y > 0:
			self.player.rect.bottom = platform.rect.top
			self.player.direction.y = 0
			self.player.isJump = False

		if self.player.direction.y < 0:
			self.player.rect.top = platform.rect.bottom
			self.player.direction.y = 0

	def _return_player_to_normal_horizontal_position(self, *args) -> None:
		platform: Platform = args[0]
		if self.player.direction.x < 0:
			self.player.rect.left = platform.rect.right
		if self.player.direction.x > 0:
			self.player.rect.right = platform.rect.left

	def _kill_player(self, *args):
		player = args[1]
		player.kill()
		print('sds')

	def player_horizontal_movement_collision(self) -> None:
		self.player.rect.x += self.player.direction.x
		self.player_listener.on_collide(self.player, self._level_up_platforms, self._load_next_level)
		self.player_listener.on_collide(self.player, self._platforms, self._return_player_to_normal_horizontal_position)
		self.player_listener.on_collide(self.player, self._mobs, self._kill_player)

	def player_vertical_movement_collision(self) -> None:
		self.player.gravity()
		self.player_listener.on_collide(self.player, self._level_up_platforms, self._load_next_level)
		self.player_listener.on_collide(self.player, self._platforms, self._return_player_to_normal_vertical_position)
		self.player_listener.on_collide(self.player, self._mobs, self._kill_player)


	def set_animation(self) -> None:
		self.player.set_player_animations(self._load_player_textures())

	def display(self, screen) -> None:
		self.player.update()
		self.player.is_moves = True
		self.player_horizontal_movement_collision()
		self.player_vertical_movement_collision()
		self.player.draw(screen)
	
