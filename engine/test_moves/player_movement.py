from sys import platform
import pygame
from model import Player
from model import Platform
from test_loop import screen

class Collision:
    def __init__(self, platforms):
        self.platforms = platforms
        self.player = Player(55,55)
        platform: Platform() 
        screen.blit(platform.image, platform.rect)

    def collision_x(self):
        for platform in self.platforms:
            if platform.rect.colliderect(self.player.rect):
                if self.player.speed_x < 0:
                    self.player.rect.left = platform.rect.right
                elif self.player.speed_x > 0:
                    self.player.rect.right = platform.rect.left

    def collision_y(self):
        for platform in self.platforms:
            if platform.rect.colliderect(self.player.rect):
                if self.player.speed_y < 0:
                    self.player.rect.top = platform.rect.bottom
                elif self.player.speed_y > 0:
                    self.player.rect.bottom = platform.rect.top
    def main(self):
        self.collision_x
        self.collision_y

class Action:
    def movement(self, key_input):
        self.key_input = key_input
        up = key_input[pygame.K_w]
        down = key_input[pygame.K_s]
        left = key_input[pygame.K_a]
        right = key_input[pygame.K_d]
        y_move = up or down
        x_move = left or right
        if left:
            self.direction.x = -1
            if up or down:
                self.rect.x += -self.velx_diag
            else:
                self.rect.x += -self.velx
        elif right:
                self.direction.x = 1
                if up or down:
                    self.rect.x += self.velx_diag
                else:
                    self.rect.x += self.velx
        else:
            self.direction.x = 0

        # this is the important part
        # check the x collision first
        self.collision_x()

        if up:
            self.direction.y = -1
            if left or right:
                self.rect.y += -self.vely_diag
            else:
                self.rect.y += -self.vely
        elif down:
            self.direction.y = 1
            if left or right:
                self.rect.y += self.vely_diag
            else:
                self.rect.y += self.vely
        else:
            self.direction.y = 0

        # now check for the y collision
        self.collision_y()