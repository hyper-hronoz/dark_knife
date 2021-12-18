import pygame

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = pygame.Surface((WIDTH,HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект

    def update(self,  left, right):
        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
 
        if right:
            self.xvel = MOVE_SPEED # Право = x + n
         
        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        self.rect.x += self.xvel # переносим свои положение на xvel 
   
    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))