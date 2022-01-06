import ast
import pygame
import sys
import os
import re
from random import randrange

from pygame import sprite
from utils import Level
from models import Knife, Platform, Player
from typing import Union
from animation import LevelLoader

BACKGROUND_COLOR = "#223759"


class Loop:

    def __init__(self) -> None:

        self.knifes = pygame.sprite.Group()
        self.loader = LevelLoader()
        self.loader.load_player_textures()
        self.loader.load_next_level()
        # f
        self.main()

    def isNextLevel(self, sprite):
        for level_up_platfrom in self.loader.level_up_platforms:
            if level_up_platfrom.colliderect(sprite):
                self.loader.load_next_level()

                for sprite in self.knifes:
                    sprite.kill()

    def add_player(self, player_position):
        x, y = player_position
        self.player = Player(x, y)
        self.player.setPlayerAnimation(self.loader.player_textures)
        self.player.is_moves = False

    def horizontal_movement_collision_checker(self, object):
        for sprite in self.loader.platforms:
            if sprite.rect.colliderect(object.rect):
                if object.direction.x < 0:
                    object.rect.left = sprite.rect.right
                elif object.direction.x > 0:
                    object.rect.right = sprite.rect.left

                self.isNextLevel(sprite)

    def player_horizontal_movement_collision(self):
        player = self.player
        player.rect.x += player.direction.x
        self.horizontal_movement_collision_checker(player)

    def knife_horizontal_movement_collision(self):
        knifes = self.knifes
        for knife in knifes:
            knife.rect.x += knife.direction.x
            self.horizontal_movement_collision_checker(knife)

    def player_vertical_movement_collision(self):
        player = self.player
        player.gravity()

        for platform in self.loader.platforms:
            if platform.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = platform.rect.top
                    player.direction.y = 0
                    player.isJump = False

                elif player.direction.y < 0:
                    player.rect.top = platform.rect.bottom
                    player.direction.y = 0

                self.isNextLevel(platform)

    def knife_animation(self):
        absolute_folder = re.sub(os.path.basename(
            __file__), "", os.path.abspath(__file__))
        path = os.path.join(absolute_folder,
                            "resources\images\knife_images/knife.png")
        return path

    def main(self):
        pygame.init()
        pygame.display.set_caption("Dark Knife")

        clock = pygame.time.Clock()
        display = (self.loader.WINDOW_WIDTH, self.loader.WINDOW_HEIGHT)
        screen = pygame.display.set_mode(display)

        backgroung = pygame.Surface(display)
        backgroung.fill(pygame.Color(BACKGROUND_COLOR))

        timer = 50
        path = self.knife_animation()
        while True:
            print(timer)
            clock.tick(75)
            timer -= 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(backgroung, (0, 0))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_e]:

                if timer <= 0:
                    x, y = (self.player.rect.x, self.player.rect.y)
                    self.knife = Knife((x + 25), (y + 20), 'left', path)
                    self.knifes.add(self.knife)
                    timer = 50
                    print(len(self.knifes))

            if keys[pygame.K_q]:
                if timer <= 0:
                    x, y = (self.player.rect.x, self.player.rect.y)
                    self.knife = Knife((x + 25), (y + 20), 'right', path)
                    self.knifes.add(self.knife)
                    timer = 50

                print(len(self.knifes))

            self.knifes.update()
            self.knifes.draw(screen)
            self.knife_horizontal_movement_collision()

            [platform.draw(screen) for platform in self.loader.platforms]

            self.player.update()
            self.player.is_moves = True
            self.player_horizontal_movement_collision()
            self.player_vertical_movement_collision()
            self.player.draw(screen)

            pygame.display.update()


if __name__ == "__main__":
    run = Loop()

# Windows
# venv\Scripts\activate.bat
# python engine\test_loop.py

# Linux
# source venv/bin/activate
# python3 engine/test_loop.py
