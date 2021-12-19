import pygame, sys
from textures import test_level
from moves import hero


WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 640 
DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
BACKGROUND_COLOR = "#223759"

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dark Knife")
    backgroung = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    backgroung.fill(pygame.Color(BACKGROUND_COLOR))
    player = hero.Player(55,55)
    left = right = False
    up = False

    level = test_level.Level()

    while True:
        clock.tick(60)
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
        level.draw_textures(screen)

        player.update(left, right, up)
        player.draw(screen)
        pygame.display.update()
        
if __name__ == "__main__":
    main()

# venv\Scripts\activate.bat 
# python engine\TestGameLoop.py