from typing import Collection
import pygame, sys, ast
from engine.test_moves.player_movement import Collision
from model import Platform, Player
from textures import Level
from test_moves import player_movement.Collision as Collision


with open(r"./levels/1.hyi", "r") as file:
    content = file.read()
    LEVEL = ast.literal_eval(content)
    cell_size = LEVEL["cell_size"]
    WINDOW_WIDTH = len(LEVEL["texturesMap"][0]) * cell_size
    WINDOW_HEIGHT = len(LEVEL["texturesMap"]) * cell_size

DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
BACKGROUND_COLOR = "#223759"

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dark Knife")
    backgroung = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    backgroung.fill(pygame.Color(BACKGROUND_COLOR))
    player = Player(55,55)
    left = right = up = False

    level = Level(LEVEL)
    platforms = level.fill_textures().get_platforms()

    while True:
        clock.tick(120)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                up = True
            if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                up = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                left = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                right = True

            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                right = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                left = False  

        screen.blit(backgroung, (0,0))
        
        player.update(left, right, up)
        player.draw(screen)
        x = Collision(platforms)
        x.main()
        # for platform in platforms:
        #     platform: Platform 
        #     screen.blit(platform.image, platform.rect)
        #     if platform.rect.colliderect(player):
        #         print("done")
        #         if player.speed_x > 0:                      
        #             player.right = player.rect.left
        #             player.speed_x = 0
        #             print(1)

        #         if player.speed_x < 0:                      
        #             player.left = player.rect.right 
        #             player.speed_x = 0
        #             print(2)

        #         if player.speed_y > 0:                     
        #             player.bottom = player.rect.top 
        #             onGround = True          
        #             player.speed_y = 0
        #             print(3)                 

        #         if player.speed_y < 0:                     
        #             player.rect.top = player.rect.bottom 
        #             player.speed_y = 0  
        #             print(4)

    
        pygame.display.update()
        
if __name__ == "__main__":
    main()

# venv\Scripts\activate.bat 
# python engine\test_loop.py
