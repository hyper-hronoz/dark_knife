import pygame
import os


class Player(pygame.sprite.Sprite):
    HERO_WIDTH = 30
    HERO_HEIGHT = 50
    MOVE_SPEED = 3
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

        self.walk_count = 0

        self.last_direction = "right"

        self.is_moves = True

    def animate(self):
        if self.direction.x < 0:
            self.image = self.animations["left"][self.walk_count //
                                                 2 % len(self.animations["left"])]
            self.walk_count += 1
            self.last_direction = "left"
        elif self.direction.x > 0:
            self.image = self.animations["right"][self.walk_count //
                                                  2 % len(self.animations["right"])]
            self.walk_count += 1
            self.last_direction = "right"
        else:
            self.image = self.animations[self.last_direction][0]

    def setPlayerAnimation(self, animations):
        self.animations = animations
        self.animate()

    def draw(self, screen) -> None:
        #print(self.rect.x, self.rect.y)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def get_input(self) -> None:
        if not self.is_moves:
            return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = self.MOVE_SPEED
        elif keys[pygame.K_LEFT]:
            self.direction.x = -self.MOVE_SPEED
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()

        self.animate()

    def gravity(self) -> None:
        self.direction.y += self.GRAVITY
        self.rect.y += self.direction.y

    def jump(self) -> None:
        if self.direction.y == 0 and not self.isJump:
            self.direction.y -= self.JUMP_HEIGHT
            self.isJump = True

    def update(self) -> None:
        self.get_input()
