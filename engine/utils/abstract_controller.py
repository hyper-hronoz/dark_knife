from abc import abstractclassmethod, ABC

import pygame

class AbstractController(ABC):

	@abstractclassmethod
	def display(self, screen: pygame.Surface) -> None:
		pass