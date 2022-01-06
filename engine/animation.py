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


class LevelLoader:
    def __init__(self):
        self.level_number = 0
        self.player_textures = {}

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

    def add_player(self, player_position):
        x, y = player_position
        self.player = Player(x, y)
        self.player.setPlayerAnimation(self.loader.player_textures)
        self.player.is_moves = False

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

        self.spawn_coordinates: list = level.get_spawn_coords()
        self.add_player(self.spawn_coordinates[randrange(
            len(self.spawn_coordinates))])
        level_up_coordinates: list = level.get_level_up_coordinates()
        self.level_up_platforms = [pygame.Rect(
            x, y, self.cell_size, self.cell_size) for x, y in level_up_coordinates]

        self.level_number += 1
