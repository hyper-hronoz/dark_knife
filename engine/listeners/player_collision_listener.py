import pygame
from models import Player, Platform
from . import CollisionListener


class PlayerCollistionListener(CollisionListener):
	def __init__(self) -> None:
		super().__init__()

	def on_player_platforms_collision(self, object: Player, platforms: list[Platform], callback):
		if sprite := self.on_collide(object, platforms):
			return callback(sprite)