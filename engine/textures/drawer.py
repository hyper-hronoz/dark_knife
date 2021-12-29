import io
import pygame
import sys
import ast
import base64
from models import Platform


class Level:
    def __init__(self, level):
        self.level = level
        self.PLATFORM_WIDTH = 15
        self.PLATFORM_HEIGHT = 15
        self.PLATFORM_GEOMETRY = (self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT)
        self.PLATFORM_COLOR = "#000000"
        self.platforms = pygame.sprite.Group()

        self.used_textures = {}

    def get_texture(self, id):
        for texture in self.level["textures"]:
            if id in texture:
                output = io.BytesIO(base64.b64decode(texture[id]))
                return pygame.image.load(output)

    def get_player_position(self):
        for y in self.level["textures_map"]:
            for x in y:
                if ("start" in self.level[y][x]):
                    return (x, y)

    def create_platforms(self):
        x = y = 0
        cell_size = self.level["cell_size"]
        textures_map = self.level["textures_map"]

        for y in range(len(textures_map)):
            for x in range(len(textures_map[y])):
                texture_id = textures_map[y][x]

                if (texture_id == ""):
                    continue

                if texture_id not in self.used_textures:
                    self.used_textures[texture_id] = self.get_texture(
                        texture_id)

                picture = pygame.transform.scale(
                    self.used_textures[texture_id], (cell_size, cell_size))
                rect = picture.get_rect()
                rect = rect.move((x * cell_size, y * cell_size))
                self.platforms.add(Platform(rect, picture))
                # screen.blit(picture, rect)
        return self.platforms
