import pygame


class Player(pygame.sprite.Sprite):

    MOVE_SPEED = 5 
    HERO_WIDTH = 22
    HERO_HEIGHT = 32
    HERO_COLOR =  pygame.Color("red")
    JUMP_POWER = 10 
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

        self.velocity = pygame.math.Vector2(0, 0)
    
        self.isJump = False

        self.fallSpeed = 0


    def keyPressListener(self):
        self.previousPosition = self.rect.copy()

        if self.isLeftPressed:
            self.velocity.x = -self.MOVE_SPEED
        elif self.isRightPressed:
            self.velocity.x = +self.MOVE_SPEED
        else:
            self.velocity.x = 0

        if self.isTopPressed:
            if self.velocity.y == 0:
                self.velocity.y = -self.JUMP_POWER
        elif self.isBottomPressed: 
            self.velocity.y = self.MOVE_SPEED
        else:
            self.velocity.y = 0


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))

    def updatePosition(self, platforms):
        for platform in platforms:
            platform: pygame.Rect

            # if platform[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            #     dx = 0

            if platform.rect.colliderect(self.rect.x, self.rect.y + self.velocity.y, self.width, self.height):

                if self.velocity.y < 0:
                    dy = platform.rect.bottom - self.rect.top
                    self.velocity.y = 0

                elif self.velocity.y >= 0:
                    dy = platform.rect.top - self.rect.bottom
                    self.velocity.y = 0

        # self.velocity.y += (self.fallSpeed * 1 + self.GRAVITY / 2) * 0.5

        self.rect.y += self.velocity.y
        self.rect.x += self.velocity.x