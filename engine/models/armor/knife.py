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

        if keys[pygame.K_SPACE]:
            print('hi')
            self.knife_move()

    def knife_move(self):
        self.rect.x + 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.get_input()
