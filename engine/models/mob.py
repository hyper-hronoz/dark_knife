import os
import re
import pygame

MOB_WIDTH = 30
MOB_HEIGHT = 50
MOB_COLOR = pygame.Color("black")


class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((MOB_WIDTH, MOB_HEIGHT))
        self.image.fill(MOB_COLOR)
        self.rect = pygame.Rect(x, y, MOB_WIDTH, MOB_HEIGHT)
        self.rect.bottom = y

    def draw(self, screen):
        picture = pygame.transform.scale(
            self.image, (MOB_WIDTH, MOB_HEIGHT))
        rect = picture.get_rect()
        rect = rect.move((MOB_WIDTH, MOB_HEIGHT))
        screen.blit(picture, self.rect)

    def update(self):
        pass
