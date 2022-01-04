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

    def draw(self, screen):
        picture = pygame.transform.scale(
            self.image, (KNIFE_WIDTH, KNIFE_HEIGHT))
        rect = picture.get_rect()
        rect = rect.move((KNIFE_WIDTH, KNIFE_HEIGHT))
        screen.blit(picture, (self.rect.x, self.rect.y))

    def update(self):
        self.direction.x = 3
        self.rect.x += self.direction.x

    # def update(self, left, right):
    #     if left:
    #         self.direction.x = 3
    #         self.rect.x += self.direction.x
    #     if right:
    #         self.direction.x = -3
    #         self.rect.x += self.direction.x
