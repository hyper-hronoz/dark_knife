import pygame

MOVE_SPEED = 7
HERO_WIDTH = 22
HERO_HEIGHT = 32
HERO_COLOR =  pygame.Color("red")
JUMP_POWER = 10
GRAVITY = 0.35

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((HERO_WIDTH,HERO_HEIGHT))
        self.image.fill(HERO_COLOR)

        self.rect = pygame.Rect(x, y, HERO_WIDTH, HERO_HEIGHT) 
        
        self.speed_x = 0 
        self.start_x = x 

        
        self.speed_y = 0
        self.start_y = y

        self.on_ground = False
    def update(self, left, right, up):
        if left:
            self.speed_x = -MOVE_SPEED # left = x- n
 
        if right:
            self.speed_x = MOVE_SPEED # right = x + n

        if up:
            if self.on_ground:
                self.speed_y = -JUMP_POWER
         
        if not(left or right): # hero stands
            self.speed_x = 0
        if not self.on_ground:
            self.speed_y +=  GRAVITY

        self.on_ground = False;
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x 

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))