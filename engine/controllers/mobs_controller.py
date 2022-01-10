import pygame
from pygame.sprite import Sprite
from models import Mob
from listeners import CollisionListener

class MobsController:
	def __init__(self, main_loop) -> None:
		self.collide_listener = CollisionListener()
		self.mobs = pygame.sprite.Group()
	
	def change(self, main_loop):
		self.enemy_spawn_platforms = main_loop.enemy_spawn_platforms
		self.knifes = main_loop.knifes
		for mob in self.mobs:
			mob.kill()
		self.add_mobs()

	def add_mobs(self):
		for i in self.enemy_spawn_platforms:
			self.mobs.add(Mob(i.rect.x, i.rect.y))
	
	def display(self, screen):
		self.mobs.draw(screen)
		for knife in self.knifes:
			self.collide_listener.on_collide(knife, self.mobs, self.kill_mob)

	def kill_mob(self, *args):
		enemy: Sprite
		knife: Sprite
		enemy, knife = args[0], args[1]
		enemy.kill()
		knife.kill()
		
		