import pygame

MOVE_SPEED = 7
HERO_WIDTH = 22
HERO_HEIGHT = 32
HERO_COLOR =  pygame.Color("red")
JUMP_HEIGHT = -10
GRAVITY = 0.35

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((HERO_WIDTH,HERO_HEIGHT))
        self.image.fill(HERO_COLOR)
        self.rect = pygame.Rect(x, y, HERO_WIDTH, HERO_HEIGHT) 

        self.direction = pygame.math.Vector2(0,0)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y)) 

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def gravity(self):
        self.direction.y += GRAVITY
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = JUMP_HEIGHT

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * MOVE_SPEED
        self.gravity()
 