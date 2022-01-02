import pygame

KNIFE_WIDTH = 30
KNIFE_HEIGHT = 10
KNIFE_COLOR = pygame.Color("black")


class Knife(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((KNIFE_WIDTH, KNIFE_HEIGHT))
        self.image.fill(KNIFE_COLOR)
        self.rect = pygame.Rect(x, y, KNIFE_WIDTH, KNIFE_HEIGHT)
        self.direction = pygame.math.Vector2(0, 0)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.direction.x = 3
        elif keys[pygame.K_q]:
            self.direction.x = -3

    def draw(self, screen):
        picture = pygame.transform.scale(
            self.image, (self.KNIFE_WIDTH, self.KNIFE_HEIGHT))
        rect = picture.get_rect()
        rect = rect.move((self.KNIFE_WIDTH, self.KNIFE_HEIGHT))
        screen.blit(picture, (self.rect.x, self.rect.y))

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x
