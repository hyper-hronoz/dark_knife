import pygame, sys


class Level:
    def __init__(self):
        self.PLATFORM_WIDTH = 32
        self.PLATFORM_HEIGHT = 32
        self.PLATFORM_GEOMETRY = (self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT)
        self.PLATFORM_COLOR = "#000000"

        self.level = [
            "-------------------------",
            "-                       -",
            "-                       -",
            "-                       -",
            "-            --         -",
            "-                       -",
            "--                      -",
            "-                       -",
            "-                   --- -",
            "-                       -",
            "-                       -",
            "-      ---              -",
            "-                       -",
            "-   -----------        --",
            "-                       -",
            "-                -      -",
            "-                   --  -",
            "-                       -",
            "-                       -",
            "-------------------------"]

    def draw_textures(self, screen):
        x=y=0 # coords
        for row in self.level:
            for col in row:
                if col == "-":
                    platform = pygame.Surface((self.PLATFORM_WIDTH, self.PLATFORM_HEIGHT))
                    platform.fill(pygame.Color(self.PLATFORM_COLOR)) 
                    screen.blit(platform, (x,y))
                                
                x += self.PLATFORM_WIDTH
            y += self.PLATFORM_HEIGHT   
            x = 0                   