import pygame


class Player(pygame.sprite.Sprite):

    MOVE_SPEED = 1
    HERO_WIDTH = 22
    HERO_HEIGHT = 32
    HERO_COLOR =  pygame.Color("red")
    JUMP_POWER = 1 
    GRAVITY = 1 

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((self.HERO_WIDTH, self.HERO_HEIGHT))
        self.image.fill(pygame.Color(self.HERO_COLOR))

        self.rect = pygame.Rect(x, y, self.HERO_WIDTH, self.HERO_HEIGHT) 

        self.isLeftPressed = False
        self.isRightPressed = False
        self.isBottomPressed = False
        self.isTopPressed = False

        self.fallSpeed = 0

    def updatePlayerPostion(self):
        self.previousPosition = self.rect.copy()
        if self.isLeftPressed:
            self.rect.x -= self.MOVE_SPEED
 
        if self.isRightPressed:
            self.rect.x += self.MOVE_SPEED

        if self.isTopPressed:
            self.rect.y -= self.JUMP_POWER

        if self.isBottomPressed:
            self.rect.y += self.MOVE_SPEED

        self.fallSpeed = self.fallSpeed * 1 + self.GRAVITY / 2
        # self.rect.y += self.fallSpeed * 0.5
        # self.rect.y += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))