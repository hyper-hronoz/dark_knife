import pygame
import pygame_menu
from pygame_menu.widgets.widget.label import Label

class MenuController:
	def __init__(self, main_loop) -> None:
		# just a plug
		self._callable = self.show_main_menu
		self._reload_game = main_loop.notify_changes
		self._menu = None

		self._MENU_THEME = pygame_menu.themes.THEME_DARK

	def change(self, main_loop) -> None:
		self._screen = main_loop.screen
		self._MENU_WIDTH, self._MENU_HEIGHT = main_loop.WINDOW_WIDTH, main_loop.WINDOW_HEIGHT
		self._set_level_number = main_loop.set_level_number

	def show_main_menu(self) -> None:
		if (self._menu):
			self._menu.disable()
		self._callable = self.show_main_menu

		self._menu = pygame_menu.Menu("Dark Knife", self._MENU_WIDTH, self._MENU_HEIGHT, theme=self._MENU_THEME)

		self._menu.add.button('Play', self.show_do_nothing)
		self._menu.add.button('Quit', pygame_menu.events.EXIT)

		self._menu.mainloop(self._screen)

	def show_do_nothing(self) -> None:
		self._callable = lambda: True 
		self._menu.disable()

	def show_death(self) -> None:
		if (self._menu):
			self._menu.disable()
		self._callable = self.show_death

		self._menu = pygame_menu.Menu("you are dead man", self._MENU_WIDTH, self._MENU_HEIGHT, theme=self._MENU_THEME)

		self._menu.add.button('Try again', self.show_do_nothing)
		self._menu.add.button('Main menu', self.show_main_menu)

		self._set_level_number(0)

		self._reload_game()

		self._menu.mainloop(self._screen)

	def show_win(self) -> None:
		if (self._menu):
			self._menu.disable()
		self._callable = self.show_win

		self._menu = pygame_menu.Menu("your still alive congratulations!!!", self._MENU_WIDTH, self._MENU_HEIGHT, theme=self._MENU_THEME)

		self._menu.add.button('Play again', self.show_do_nothing)
		self._menu.add.button('Main menu', self.show_main_menu)

		self._set_level_number(0)

		self._reload_game()

		self._menu.mainloop(self._screen)

	def display(self, screen) -> None:
		self._callable()