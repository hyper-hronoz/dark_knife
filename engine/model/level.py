import io, pygame, sys, base64
from model import Platform

class Level:
    def __init__(self, level):
        self.level = level
        self.platforms = pygame.sprite.Group()
        self.PLATFORM_COLOR = "#000000"
        self.usedTextures = {}

    def get_platforms(self):
        return self.platforms

    def _getTexture(self, id):
        for texture in self.level["textures"]:
            if id in texture:
                output = io.BytesIO(base64.b64decode(texture[id]))
                return pygame.image.load(output)

    def create_platforms(self):
        x=y=0 

        cell_size = self.level["cell_size"]

        textures_map = self.level["textures_map"]

        for y in range(len(textures_map)):
            for x in range(len(textures_map[y])):
                texture_id = textures_map[y][x]

                if (texture_id == ""):
                    continue

                if texture_id not in self.usedTextures:
                    self.usedTextures[texture_id] = self._getTexture(texture_id)

                picture = pygame.transform.scale(self.usedTextures[texture_id], (cell_size, cell_size))
                rect = picture.get_rect()
                
                rect = rect.move((x * cell_size, y * cell_size))

                self.platforms.add(Platform(rect, picture))

        return self
