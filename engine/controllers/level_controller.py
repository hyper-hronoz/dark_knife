import ast, pygame, os
from random import randrange
from models import Platform
from utils import Level, AbstractController

class LevelController(AbstractController):
	def __init__(self, main_loop) -> None:
		self._notify_changes = main_loop.notify_changes
		self._absolute_folder = main_loop.absolute_folder
		self.level_number = 0
		self.spawn_coordinates = 0, 0


	def load_next_level(self, *args) -> None:
			self.level_data = self._get_level()

			if self.level_number == "gg":
				return

			self.cell_size = self.level_data["cell_size"]
			self.WINDOW_WIDTH = len(self.level_data["textures_map"][0]) * self.cell_size
			self.WINDOW_HEIGHT = len(self.level_data["textures_map"]) * self.cell_size

			level = Level(self.level_data)
			spawn_coordinates: list = level.get_spawn_platforms()
			level_up_coordinates: list = level.get_level_up_coordinates()

			self.platforms = level.get_platforms()
			self.spawn_coordinates = spawn_coordinates[randrange(len(spawn_coordinates))]
			self.level_up_platforms = pygame.sprite.Group()

			for x, y in level_up_coordinates:
				self.level_up_platforms.add(Platform(pygame.Rect(x, y, self.cell_size, self.cell_size)))

			self.level_number += 1

			self._notify_changes()

			# for sprite in self.knifes:
			# 	sprite.kill()

	def _get_level(self) -> dict:
		try:
			if not os.path.isfile(f"./levels/{self.level_number}.txt"):
				self.level_number = "boss.txt"

			if not os.path.isfile(f"./levels/{self.level_number}.txt"):
				self.level_number = "gg"

			with open(f"./levels/{self.level_number}.txt", "r") as file:
				content = file.read()
				return ast.literal_eval(content)
		except Exception as e:
			print(f"File opening error probably because of {e}")

	def display(self, screen):
		[platform.draw(screen) for platform in self.platforms]

