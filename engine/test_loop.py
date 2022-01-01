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
        # setting default values
        # self.player_coordinates = 0, 0

        self.load_player_textures()
        self.load_next_level()
        self.main()

    def load_player_textures(self):
        absolute_folder = re.sub(os.path.basename(__file__), "", os.path.abspath(__file__))
        right_movement_textures_path = os.path.join(absolute_folder, "resources/images/right_movement_set/")
        self.player_textures["right"] = [pygame.image.load(f"{right_movement_textures_path}right-{i}.png") for i in range(1, 14)]
        left_movement_textures_path = os.path.join(absolute_folder, "resources/images/left_movement_set/")
        self.player_textures["left"] = [pygame.image.load(f"{left_movement_textures_path}left-{i}.png") for i in range(1, 14)]
        print(self.player_textures)

    def load_next_level(self) -> None:
        self.level_data = self.get_level()

        if self.level_data == "gg":
            self.game_end_congratulations()
            return

        if not self.level_data:
            self.game_id_failure_to_start()
            return

        self.cell_size = self.level_data["cell_size"]
        self.WINDOW_WIDTH = len(self.level_data["textures_map"][0]) * self.cell_size
        self.WINDOW_HEIGHT = len(self.level_data["textures_map"]) * self.cell_size

        level = Level(self.level_data)
        self.platforms = level.get_platforms()
        
        spawn_coordinates: list = level.get_spawn_coords()
        self.add_player(spawn_coordinates[randrange(len(spawn_coordinates))])

        level_up_coordinates: list = level.get_level_up_coordinates()
        self.level_up_platforms = [pygame.Rect(coordinate[0], coordinate[1], self.cell_size, self.cell_size) for coordinate in level_up_coordinates]

        self.level_number += 1

    def get_level(self) -> dict:
        try:
            if not os.path.isfile(f"./levels/{self.level_number}.hyi"):
                self.level_number = "boss.hyi"

            if not os.path.isfile(f"./levels/{self.level_number}.hyi"):
                self.level_number = "gg"
                return

            with open(f"./levels/{self.level_number}.hyi", "r") as file:
                content = file.read()
                return ast.literal_eval(content)
        except Exception as e:
            print(f"File opening error probably because of {e}")
        
    def game_end_congratulations(self):
        pass

    def game_id_failure_to_start(self):
        pass

    def add_knife(self, knife_position: tuple[int]) -> None:
        x, y = (50, 50)
        self.knife = pygame.sprite.GroupSingle()
        knife_sprite = Knife(55, 55)
        self.knife.add(knife_sprite)

    def add_player(self, player_position: tuple[int]) -> None:
        x, y = player_position
        self.player = Player(x, y)
        self.player.setPlayerAnimation(self.player_textures)

    def horizontal_movement_collision_listener(self) -> None:
        player = self.player.ground.sprite
        player.rect.x += player.direction.x * player.MOVE_SPEED

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

                self.isNextLevel(sprite) 

    def vertical_movement_collision_listener(self) -> None:
        player = self.player.ground.sprite
        player.gravity()

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.isJump = False

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

                self.isNextLevel(sprite) 

    def isNextLevel(self, sprite) -> None:
        for level_up_platfrom in self.level_up_platforms:
            if level_up_platfrom.colliderect(sprite):
                self.load_next_level()

    def main(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dark Knife")

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        backgroung = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        backgroung.fill(pygame.Color(BACKGROUND_COLOR))

        self.add_knife(0)


        while True:
            clock.tick(75)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(backgroung, (0, 0))

            [platform.draw(screen) for platform in self.platforms]

            self.player.update()
            self.horizontal_movement_collision_listener()
            self.vertical_movement_collision_listener()
            self.player.draw(screen)

            self.knife.update()
            self.knife.draw(screen)

            pygame.display.update()


if __name__ == "__main__":
    run = Loop()

# Windows
# venv\Scripts\activate.bat
# python engine\test_loop.py

# Linux
# source venv/bin/activate
# python3 engine/test_loop.py
