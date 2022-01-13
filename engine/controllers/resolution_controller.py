from models import Player
from controllers import LevelController

class ResolutionController:
	def __init__(self, main_loop) -> None:
		pass

	def change(self, main_loop):
		self._cell_size = main_loop.cell_size

		self._LEVEL_WIDTH = main_loop.LEVEL_WIDTH
		self._LEVEL_HEIGHT = main_loop.LEVEL_HEIGHT

		self._WINDOW_WIDTH = main_loop.WINDOW_WIDTH
		self._WINDOW_HEIGHT = main_loop.WINDOW_HEIGHT
		return self

	def calculate_vertical_scale(self):
		self.vertical_scale = self._WINDOW_HEIGHT / self._LEVEL_WIDTH
		return self

	def calculate_horizontal_scale(self):
		self.horizontal_scale = self._WINDOW_WIDTH / self._LEVEL_HEIGHT
		return self

	def apply_vertical_scale(self):
		try:
			Player.JUMP_POWER = self.vertical_scale
			LevelController.TEXTURES_VERTICAL_SCALE = self.vertical_scale
		except Exception as e:		
			print(e)
		return self
