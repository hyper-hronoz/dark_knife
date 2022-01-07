import os
import re
import pygame

MOB_WIDTH = 50
MOB_HEIGHT = 20
MOB_COLOR = pygame.Color("black")


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, marker):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOB_WIDTH, MOB_HEIGHT))
        self.image.fill(MOB_COLOR)
        self.rect = pygame.Rect(x, y, MOB_WIDTH, MOB_HEIGHT)

        self.direction = pygame.math.Vector2(0, 0)
        self.marker = marker

    def draw(self, screen):
        picture = pygame.transform.scale(
            self.image, (MOB_WIDTH, MOB_HEIGHT))
        rect = picture.get_rect()
        rect = rect.move((MOB_WIDTH, MOB_HEIGHT))
        screen.blit(picture, (self.rect.x, self.rect.y))

    def update(self):
        pass
