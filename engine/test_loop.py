import pygame
import sys
import os
import re
from random import randrange

from utils import Level
from models import Knife, Platform, Player
from controllers import PlayerController, LevelController, KnifeController

BACKGROUND_COLOR = "#223759"


class Loop:

	def __init__(self) -> None:
		self.absolute_folder = re.sub(os.path.basename(__file__), "", os.path.abspath(__file__))

		self.observers = []

		self.level_controller = LevelController(self)
		self.player_controller = PlayerController(self)
		self.knife_controller = KnifeController(self)

		self.add_observer(self)
		self.add_observer(self.player_controller)
		self.add_observer(self.knife_controller)

		# в нем вызывается метод notify_changes, который вызывает метод change у каждого объекта, которого мы хотим оповестить о загрузке нового уровня, для того чтобы он самостоятельно подтянул изменения
		self.level_controller.load_next_level()

		self.main()

	def add_observer(self, observer):
		self.observers.append(observer)
	
	def notify_changes(self):
		[observer.change(self) for observer in self.observers]

	def change(self, заглушка_намомни_мне_это_исправить_без_нее_не_работает):
		self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.level_controller.WINDOW_WIDTH, self.level_controller.WINDOW_HEIGHT
		self.platforms = self.level_controller.platforms
		self.level_up_platforms = self.level_controller.level_up_platforms

		spawn_platform: Platform = self.level_controller.spawn_coordinates
		self.player: Player = self.player_controller.spawn_player((spawn_platform.rect.left, spawn_platform.rect.top))
		self.player_controller.set_animation()

	def main(self):
		pygame.init()
		pygame.display.set_caption("Dark Knife")

		clock = pygame.time.Clock()
		screen = pygame.display.set_mode(
			(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

		backgroung = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
		backgroung.fill(pygame.Color(BACKGROUND_COLOR))

		while True:
			clock.tick(75)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			screen.blit(backgroung, (0, 0))

			self.knife_controller.display(screen)
			self.level_controller.display(screen)
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
