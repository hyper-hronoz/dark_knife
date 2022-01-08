import pygame
import sys
import os
import re
from random import randrange

from utils import Level
from models import Knife, Platform, Player
from controllers import PlayerController, LevelController

BACKGROUND_COLOR = "#223759"


class Loop:

	def __init__(self) -> None:
		self.absolute_folder = re.sub(os.path.basename(__file__), "", os.path.abspath(__file__))
		self.observers = []


		self.knifes = pygame.sprite.Group()
		self.mobs = pygame.sprite.Group()


		self.level_controller = LevelController(self)
		self.rebuild_level()


		self.main()


	def add_observer(self, observer):
		self.observers.append(observer)
	
	def notifyChanges(self):
		[observer.change() for observer in self.observers]

	def rebuild_level(self, *arg):
		self.level_controller.load_next_level()
		self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.level_controller.get_window_size()
		self.platforms = self.level_controller.get_platforms()
		self.level_up_platforms = self.level_controller.get_level_up_platforms()
		spawn_platform: Platform = self.level_controller.get_player_position()

		self.player_controller = PlayerController(self)
		self.player_controller.change(self)
		self.player = self.player_controller.spawn_player((spawn_platform.rect.left, spawn_platform.rect.top))
		self.player_controller.set_animation()


		# self.notifyChanges()

	# def knife_horizontal_movement_collision(self):
	# 	knifes = self.knifes
	# 	for knife in knifes:
	# 		knife.rect.x += knife.direction.x
	# 		self.horizontal_movement_collision_checker(knife)

	def main(self):
		pygame.init()
		pygame.display.set_caption("Dark Knife")

		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(
			(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

		backgroung = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		backgroung.fill(pygame.Color(BACKGROUND_COLOR))

		timer = 50
		while True:
			# print(timer)
			clock.tick(75)
			timer -= 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			screen.blit(backgroung, (0, 0))

			keys = pygame.key.get_pressed()

			# if keys[pygame.K_e]:
			#     if timer <= 0:
			#         x, y = (self.player.rect.x, self.player.rect.y)
			#         self.knife = Knife((x + 25), (y + 20), 'left')
			#         self.knifes.add(self.knife)
			#         timer = 50
					# print(len(self.knifes))

			# if keys[pygame.K_q]:
			#     if timer <= 0:
			#         x, y = (self.player.rect.x, self.player.rect.y)
			#         self.knife = Knife((x - 25), (y + 20), 'right')
			#         self.knifes.add(self.knife)
			#         timer = 50

				# print(len(self.knifes))

			# self.knifes.update()
			# self.knifes.draw(screen)
			# self.knife_horizontal_movement_collision()

			self.level_controller.display(screen)
			# print(self.player_controller.player.rect.top)
			self.player_controller.display(screen)

			pygame.display.update()


if __name__ == "__main__":
	run = Loop()

# Windows
# venv\Scripts\activate.bat
# python engine\test_loop.py

# Linux
# source venv/bin/activate
# python3 engine/test_loop.py
