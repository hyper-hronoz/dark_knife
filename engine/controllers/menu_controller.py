import pygame
import pygame_menu
from pygame_menu.widgets.widget.label import Label

class MenuController:
	def __init__(self, main_loop) -> None:
		# just a plug
		self._callable = self.show_main_menu
		self._reload_game = main_loop.notify_changes

		self._MENU_THEME = pygame_menu.themes.THEME_DARK

	def change(self, main_loop) -> None:
		self._screen = main_loop.screen
		self._MENU_WIDTH, self._MENU_HEIGHT = main_loop.WINDOW_WIDTH, main_loop.WINDOW_HEIGHT

	def show_main_menu(self) -> None:
		self._callable = self.show_main_menu

		self._main_menu = pygame_menu.Menu("Dark Knife", self._MENU_WIDTH, self._MENU_HEIGHT, theme=self._MENU_THEME)

		self._main_menu.add.button('Play', self.show_do_nothing)
		self._main_menu.add.button('Quit', pygame_menu.events.EXIT)

	def show_do_nothing(self) -> None:
		print("work")
		self._callable = lambda: True 
		self._main_menu.disable()

	def show_death(self) -> None:
		self._callable = self.show_death

		self._main_menu = pygame_menu.Menu("you are dead man", self._MENU_WIDTH, self._MENU_HEIGHT, theme=self._MENU_THEME)

		self._main_menu.add.button('Try again', self.show_do_nothing)
		self._main_menu.add.button('Main menu', self.show_main_menu)

		self._reload_game()

		

	def show_win(self) -> None:
		self._callable = self.show_win

		self._main_menu = pygame_menu.Menu("your still alive congratulations!!!", self._MENU_WIDTH, self._MENU_HEIGHT, theme=self._MENU_THEME)

		self._main_menu.add.button('Play again', self.show_do_nothing)
		self._main_menu.add.button('Main menu', self.show_main_menu)

	def display(self, screen) -> None:
		if not self._callable():
			self._main_menu.mainloop(screen)
		else:
			self._main_menu.disable()