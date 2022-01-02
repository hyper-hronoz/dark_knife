import pygame
import os


class Player(pygame.sprite.Sprite):
    MOVE_SPEED = 5
    HERO_WIDTH = 20
    HERO_HEIGHT = 50
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

        self.ground = pygame.sprite.GroupSingle(self)
        self.ground.add(self)

        self.last_direction = "right"
        self.animation_delay = 5

    def animate(self):
        if self.direction.x < 0:
            self.image = self.animations["left"][self.walk_count % len(
                self.animations)]
            self.walk_count += 1
            self.last_direction = "left"
        elif self.direction.x > 0:
            self.image = self.animations["right"][self.walk_count % len(
                self.animations)]
            self.walk_count += 1
            self.last_direction = "right"
        else:
            self.image = self.animations[self.last_direction][0]

    def setPlayerAnimation(self, animations):
        self.animations = animations
        self.animate()

    def draw(self, screen) -> None:
        picture = pygame.transform.scale(
            self.image, (self.HERO_WIDTH, self.HERO_HEIGHT))
        rect = picture.get_rect()
        rect = rect.move((self.HERO_WIDTH, self.HERO_HEIGHT))
        screen.blit(picture, (self.rect.x, self.rect.y))

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
