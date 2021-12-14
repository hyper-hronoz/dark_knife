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

        with open("../levels/hyi.hyi", "r") as file:
            # print(json.loads(content))
            content = file.read()
            self.level = ast.literal_eval(content)

        # self.level = [
        #     "-------------------------",
        #     "-                       -",
        #     "-                       -",
        #     "-                       -",
        #     "-            --         -",
        #     "-                       -",
        #     "--                      -",
        #     "-                       -",
        #     "-                   --- -",
        #     "-                       -",
        #     "-                       -",
        #     "-      ---              -",
        #     "-                       -",
        #     "-   -----------        --",
        #     "-                       -",
        #     "-                -      -",
        #     "-                   --  -",
        #     "-                       -",
        #     "-                       -",
        #     "-------------------------"]

    def getTexture(self, id):
        for texture in self.level["textures"]:
            if id in texture:
                output = io.BytesIO(base64.b64decode(texture[id]))
                return pygame.image.load(output)

    def draw_textures(self, screen):
        x=y=0 # coords

        for position in self.level["texturesMap"]:
            texture_id = position["fill"]

            if (texture_id == ""):
                continue
                
            if texture_id not in self.usedTextures:
                self.usedTextures[texture_id] = self.getTexture(texture_id)
            
            # platform = pygame.Surface((self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))
            # platform.fill(pygame.Color(self.PLATFORM_COLOR)) 
            # screen.blit(self.usedTextures[texture_id], (position["x"], position["y"]))
            picture = pygame.transform.scale(self.usedTextures[texture_id], (20, 20))
            rect = picture.get_rect()
            rect = rect.move((position["x"], position["y"]))
            screen.blit(picture, rect)

        print(self.usedTextures)                                 
    # def draw_textures(self, screen):
    #     x=y=0 # coords
    #     for row in self.level:
    #         for col in row:
    #             if col == "-":
    #                 platform = pygame.Surface((self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))
    #                 platform.fill(pygame.Color(self.PLATFORM_COLOR)) 
    #                 screen.blit(platform, (x,y))
                                
    #             x += self.PLATFORM_WIDTH
    #         y += self.PLATFORM_HEIGHT   
    #         x = 0                   