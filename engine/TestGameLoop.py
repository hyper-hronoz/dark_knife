import pygame, sys
from test_textures import test_level


WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 640 
DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
BACKGROUND_COLOR = "#FFFFFF"

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dark Knife")
    backgroung = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    backgroung.fill(pygame.Color(BACKGROUND_COLOR))
    level = test_level.Level()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backgroung, (0,0))
        level.draw_textures(screen)
        pygame.display.update()
        
if __name__ == "__main__":
    main()

# venv\Scripts\activate.bat 
# python engine\TestGameLoop.py