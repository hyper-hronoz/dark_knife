import io
import pygame
import sys
import ast
import base64
from models import Platform


class Level:
    def __init__(self, level) -> None:
        self.level = level

        self.PLATFORM_WIDTH = 15
        self.PLATFORM_HEIGHT = 15
        self.PLATFORM_GEOMETRY = (self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT)
        self.PLATFORM_COLOR = "#000000"

        self.platforms = pygame.sprite.Group()

        self.textures_map = self.level["textures_map"]
        self.cell_size = self.level["cell_size"]

        self.used_textures = {}

    def get_texture(self, id) -> pygame.image:
        try:
            output = io.BytesIO(base64.b64decode(self.level["textures"][id]))
            return pygame.image.load(output)
        except Exception as e:
            print(f"Textures with {id=} not found because of {e}")

    def get_spawn_coords(self):
        spawn_coordinates = []

        for y in range(len(self.textures_map)):
            for x in range(len(self.textures_map[y])):
                texture_id = self.textures_map[y][x]

                if (texture_id == "start"):
                    spawn_coordinates.append(
                        (x * self.cell_size, y * self.cell_size))

        if not spawn_coordinates:
            for y in range(len(self.textures_map) // 2):
                for x in range(len(self.textures_map[y])):
                    texture_id_1 = self.textures_map[y][x]
                    texture_id_2 = self.textures_map[y + 1][x]

                    if (texture_id_1 == texture_id_2 == ""):
                        spawn_coordinates.append(
                            (x * self.cell_size, (y + 1) * self.cell_size))

        return spawn_coordinates

    def get_level_up_coordinates(self):
        level_up_coordinates = []
        for y in range(len(self.textures_map)):
            for x in range(len(self.textures_map[y])):
                texture_id = self.textures_map[y][x]

                if (texture_id == "finish"):
                    level_up_coordinates.append(
                        (x * self.cell_size, y * self.cell_size))
        return level_up_coordinates

    def get_platforms(self):
        x = y = 0

        for y in range(len(self.textures_map)):
            for x in range(len(self.textures_map[y])):
                texture_id = self.textures_map[y][x]

                if (texture_id == ""):
                    continue

                if texture_id not in self.used_textures:
                    self.used_textures[texture_id] = self.get_texture(
                        texture_id)

                picture = pygame.transform.scale(
                    self.used_textures[texture_id], (self.cell_size, self.cell_size))
                rect = picture.get_rect()
                rect = rect.move((x * self.cell_size, y * self.cell_size))
                self.platforms.add(Platform(rect, picture))

        return self.platforms
