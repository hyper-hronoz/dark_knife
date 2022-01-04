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

BACKGROUND_COLOR = "#223759"


class Loop:

    def __init__(self) -> None:
        self.level_number = 0

        self.player_textures = {}

        self.load_player_textures()
        self.load_next_level()
        self.main()

    def load_player_textures(self):
        absolute_folder = re.sub(os.path.basename(
            __file__), "", os.path.abspath(__file__))
        right_movement_textures_path = os.path.join(
            absolute_folder, "resources/images/right_movement_set/")
        self.player_textures["right"] = [pygame.transform.scale(pygame.image.load(
            f"{right_movement_textures_path}right-{i}.png"), (Player.HERO_WIDTH, Player.HERO_HEIGHT)) for i in range(1, 14)]
        left_movement_textures_path = os.path.join(
            absolute_folder, "resources/images/left_movement_set/")
        self.player_textures["left"] = [pygame.transform.scale(pygame.image.load(
            f"{left_movement_textures_path}left-{i}.png"), (Player.HERO_WIDTH, Player.HERO_HEIGHT)) for i in range(1, 14)]

    def load_next_level(self) -> None:
        self.level_data = self.get_level()

        if self.level_data == "gg":
            self.game_end_congratulations()
            return

        if not self.level_data:
            self.game_id_failure_to_start()
            return

        self.cell_size = self.level_data["cell_size"]
        self.WINDOW_WIDTH = len(
            self.level_data["textures_map"][0]) * self.cell_size
        self.WINDOW_HEIGHT = len(
            self.level_data["textures_map"]) * self.cell_size

        level = Level(self.level_data)
        self.platforms = level.get_platforms()

        spawn_coordinates: list = level.get_spawn_coords()
        self.add_player(spawn_coordinates[randrange(len(spawn_coordinates))])

        level_up_coordinates: list = level.get_level_up_coordinates()
        self.level_up_platforms = [pygame.Rect(
            x, y, self.cell_size, self.cell_size) for x, y in level_up_coordinates]

        self.level_number += 1

    def get_level(self) -> dict:
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

    def game_end_congratulations(self):
        pass

    def game_id_failure_to_start(self):
        pass

    def isNextLevel(self, sprite):
        for level_up_platfrom in self.level_up_platforms:
            if level_up_platfrom.colliderect(sprite):
                self.load_next_level()

    def add_knife(self, knife):
        self.knifes = pygame.sprite.Group()
        self.knifes.add(knife)
        print("kk")

    def add_player(self, player_position):
        x, y = player_position
        self.player = Player(x, y)
        self.player.setPlayerAnimation(self.player_textures)
        self.player.is_moves = False

    def horizontal_movement_collision_listener(self):
        player = self.player
        player.rect.x += player.direction.x

        for sprite in self.platforms:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

                self.isNextLevel(sprite)

    def vertical_movement_collision_listener(self):
        player = self.player
        player.gravity()

        for platform in self.platforms:
            if platform.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = platform.rect.top
                    player.direction.y = 0
                    player.isJump = False

                elif player.direction.y < 0:
                    player.rect.top = platform.rect.bottom
                    player.direction.y = 0

                self.isNextLevel(platform)

    def main(self):
        pygame.init()
        pygame.display.set_caption("Dark Knife")

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(
            (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        backgroung = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        backgroung.fill(pygame.Color(BACKGROUND_COLOR))

        #
        # self.add_knife(knife_position)

        while True:
            clock.tick(75)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(backgroung, (0, 0))

            keys = pygame.key.get_pressed()
            flag = False
            if keys[pygame.K_e]:
                x, y = (self.player.rect.x, self.player.rect.y)
                self.add_knife(Knife(x, y))
                left = True
                right = False
                flag = True
            if keys[pygame.K_q]:
                x, y = (self.player.rect.x, self.player.rect.y)
                self.add_knife(Knife(x, y))
                left = False
                right = True
                flag = True

            if flag:
                self.knifes.update(left, right)
                self.knifes.draw(screen)

            [platform.draw(screen) for platform in self.platforms]

            self.player.update()
            self.player.is_moves = True
            self.horizontal_movement_collision_listener()
            self.vertical_movement_collision_listener()
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
