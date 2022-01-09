from re import M
from sys import platform
import pygame
from utils import AbstractController
from listeners import CollisionListener
from models import Knife, Platform, Player

class KnifeController(AbstractController):

	def __init__(self, main_loop) -> None:
		self.knifes = pygame.sprite.Group()
		self.knife_collision_listener = CollisionListener()
		self.timer = 50

	def change(self, main_loop):
		self._platforms: pygame.sprite.Group = main_loop.platforms
		self._player: Player = main_loop.player
		for sprite in self.knifes:
			sprite.kill()

	def _return_knife_to_notmal_horizontal_position(self, *args):
		knife: Knife
		platform: Platform
		platform, knife  = args[0], args[1]
		if knife.direction.x < 0:
			knife.rect.left = platform.rect.right
		elif knife.direction.x > 0:
			knife.rect.right = platform.rect.left

	def knife_horizontal_movement_collision(self):
		for knife in self.knifes:
			knife: Knife
			knife.rect.x += knife.direction.x
			self.knife_collision_listener.on_collide(knife, self._platforms, self._return_knife_to_notmal_horizontal_position)

	def update(self):
		keys = pygame.key.get_pressed()

		self.timer -= 1

		if keys[pygame.K_e]:
			if self.timer <= 0:
				x, y = (self._player.rect.x, self._player.rect.y)
				self.knife = Knife((x + 25), (y + 20), 'left')
				self.knifes.add(self.knife)
				self.timer = 50
				print(len(self.knifes))

		if keys[pygame.K_q]:
			if self.timer <= 0:
				x, y = (self._player.rect.x, self._player.rect.y)
				self.knife = Knife((x - 25), (y + 20), 'right')
				self.knifes.add(self.knife)
				self.timer = 50

	def display(self, screen):
		self.update()
		self.knifes.update()
		self.knifes.draw(screen)
		self.knife_horizontal_movement_collision()