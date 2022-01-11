import os
import re
import pygame

KNIFE_WIDTH = 50
KNIFE_HEIGHT = 20
KNIFE_COLOR = pygame.Color("black")


class Knife(pygame.sprite.Sprite):
    def __init__(self, x, y, marker):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((KNIFE_WIDTH, KNIFE_HEIGHT))
        self.image.fill(KNIFE_COLOR)
        self.rect = pygame.Rect(x, y, KNIFE_WIDTH, KNIFE_HEIGHT)

        self.direction = pygame.math.Vector2(0, 0)
        self.marker = marker

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.marker == "left":
            self.direction.x = 8
            self.rect.x += self.direction.x
        if self.marker == "right":
            self.direction.x = -8
            self.rect.x += self.direction.x
