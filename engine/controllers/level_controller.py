import ast, pygame, os, base64, io
from random import randrange
from models import Platform
from utils import Level

class LevelController:
	TEXTURES_VERTICAL_SCALE = 1

	def __init__(self, main_loop) -> None:
		self._notify_changes = main_loop.notify_changes
		self._absolute_folder = main_loop.absolute_folder
		self.level_number = 0 
		self.spawn_coordinates = 0, 0
		self.used_textures = {}

	def change(self, main_loop) -> None:
		self._call_win = main_loop.menu_controller.show_win
		self._call_death = main_loop.menu_controller.show_death

	def set_level_number(self, number: int) -> None:
		self.level_number = number
		self.load_next_level()

	def load_next_level(self, *args) -> None:
			self.level_data = self._get_level()

			if self.level_number == "gg":
				self._call_win()
				return

			self.cell_size = self.level_data["cell_size"]
			self.LEVEL_WIDTH = len(self.level_data["textures_map"][0]) * self.cell_size
			self.LEVEL_HEIGHT = len(self.level_data["textures_map"]) * self.cell_size

			self.level = Level(self.level_data)

			self.platforms_coordinates: list = self.level.get_platforms_coordinates()
			self.spawn_coordinates: list = self.level.get_spawn_coordinates()
			self.enemy_spawn_coordinates: list = self.level.get_enemy_coordinates()
			self.level_up_coordinates: list = self.level.get_level_up_coordinates()

			self.level_number += 1

			self._notify_changes()

	def _parse_coordinates_to_sprites(self, coordinates) -> pygame.sprite.Group:
		print(coordinates)
		sprites = pygame.sprite.Group()
		cell_size = self.cell_size * self.TEXTURES_VERTICAL_SCALE
		if not coordinates:
			return sprites 
		if len(coordinates[0]) == 2:
			for x, y in coordinates:
				x = x * self.TEXTURES_VERTICAL_SCALE
				y = y * self.TEXTURES_VERTICAL_SCALE
				sprites.add(Platform(pygame.Rect(x, y, cell_size, cell_size)))
		if len(coordinates[0]) == 3:
			for x, y, texture_id in coordinates:
				x = x * self.TEXTURES_VERTICAL_SCALE
				y = y * self.TEXTURES_VERTICAL_SCALE
				self._get_picture(texture_id)
				picture = pygame.transform.scale(self.used_textures[texture_id], (cell_size, cell_size))
				rect = picture.get_rect()
				rect = rect.move((x * cell_size, y * cell_size))
				sprites.add(Platform(pygame.Rect(x, y, cell_size, cell_size), picture))
		return sprites

	
	def _get_texture(self, id) -> pygame.image:
		try:
			output = io.BytesIO(base64.b64decode(self.level_data["textures"][id]))
			return pygame.image.load(output)
			
		except Exception as e:
			print(f"Textures with {id} not found because of {e}")

	def _get_picture(self, texture_id):
		if texture_id not in self.used_textures:
			self.used_textures[texture_id] = self._get_texture(
				texture_id)

		return pygame.transform.scale(self.used_textures[texture_id], (self.cell_size, self.cell_size))

	def get_platforms_sprites(self):
		self.platforms = self._parse_coordinates_to_sprites(self.platforms_coordinates)
		self.enemy_spawn_platforms = self._parse_coordinates_to_sprites(self.enemy_spawn_coordinates)
		self.player_spawn_platforms = self._parse_coordinates_to_sprites(self.spawn_coordinates)
		self.level_up_platforms = self._parse_coordinates_to_sprites(self.level_up_coordinates)

	def _get_level(self) -> dict:
		try:
			if not os.path.isfile(f"./levels/{self.level_number}.txt"):
				self.level_number = "boss.txt"

			if not os.path.isfile(f"./levels/{self.level_number}.txt"):
				self.level_number = "gg"
				return

			with open(f"./levels/{self.level_number}.txt", "r") as file:
				content = file.read()
				return ast.literal_eval(content)
		except Exception as e:
			print(f"File opening error probably because of {e}")

	def display(self, screen) -> None:
		[platform.draw(screen) for platform in self.platforms]

