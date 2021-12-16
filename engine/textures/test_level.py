import io
import pygame, sys
import ast
import base64


class Level:
    def __init__(self):
        self.PLATFORM_WIDTH = 15
        self.PLATFORM_HEIGHT = 15
        self.PLATFORM_GEOMETRY = (self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT)
        self.PLATFORM_COLOR = "#000000"

        self.usedTextures = {}

        with open(r"C:\Users\jegor\PycharmProject\dark_knife\engine\textures\data\hyi.hyi", "r") as file:
            content = file.read()
            self.level = ast.literal_eval(content)

    def getTexture(self, id):
        for texture in self.level["textures"]:
            if id in texture:
                output = io.BytesIO(base64.b64decode(texture[id]))
                return pygame.image.load(output)

    def draw_textures(self, screen):
        x=y=0 

        for position in self.level["texturesMap"]:
            texture_id = position["fill"]

            if (texture_id == ""):
                continue
                
            if texture_id not in self.usedTextures:
                self.usedTextures[texture_id] = self.getTexture(texture_id)

            picture = pygame.transform.scale(self.usedTextures[texture_id], (20, 20))
            rect = picture.get_rect()
            rect = rect.move((position["x"], position["y"]))
            screen.blit(picture, rect)

        print(self.usedTextures)                                 
