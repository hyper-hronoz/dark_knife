import pygame


class Player(pygame.sprite.Sprite):
    MOVE_SPEED = 5
    HERO_WIDTH = 22
    HERO_HEIGHT = 32
    HERO_COLOR = pygame.Color("red")
    JUMP_HEIGHT = 10
    GRAVITY = 0.5

    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.HERO_WIDTH, self.HERO_HEIGHT))
        self.image.fill(self.HERO_COLOR)

        self.rect = pygame.Rect(x, y, self.HERO_WIDTH, self.HERO_HEIGHT)

        self.direction = pygame.math.Vector2(0, 0)
        self.isJump = False

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()

    def gravity(self) -> None:
        self.direction.y += self.GRAVITY
        self.rect.y += self.direction.y

    def jump(self) -> None:
        if self.direction.y == 0 and not self.isJump:
            self.direction.y -= self.JUMP_HEIGHT
            self.isJump = True

    def update(self) -> None:
        self.get_input()
