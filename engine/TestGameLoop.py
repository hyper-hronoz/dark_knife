import pygame, sys


WINDOW_WIDTH = 800 
WINDOW_HEIGHT = 640 
DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
BACKGROUND_COLOR = "#00FFFF"

def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dark Knife")
    backgroung = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    backgroung.fill(pygame.Color(BACKGROUND_COLOR))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        pygame.display.update()
        clock.tick(60)
        

if __name__ == "__main__":
    main()