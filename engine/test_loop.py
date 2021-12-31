import pygame
import sys
import ast

from pygame.constants import KEYDOWN
from model import Platform, Player, Level


with open(r"./levels/1.hyi", "r") as file:
    content = file.read()
    LEVEL = ast.literal_eval(content)
    cell_size = LEVEL["cell_size"]
    WINDOW_WIDTH = len(LEVEL["textures_map"][0]) * cell_size
    WINDOW_HEIGHT = len(LEVEL["textures_map"]) * cell_size

DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
BACKGROUND_COLOR = "#223759"


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dark Knife")
    backgroung = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

    backgroung.fill(pygame.Color(BACKGROUND_COLOR))

    player = Player(55, 55)

    level = Level(LEVEL)
    platforms = level.create_platforms().get_platforms()

    while True:
        clock.tick(75)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    player.isLeftPressed = True

                if event.key == pygame.K_RIGHT:
                    player.isRightPressed = True

                if event.key == pygame.K_UP:
                    player.isTopPressed = True

                if event.key == pygame.K_DOWN:
                    player.isBottomPressed = True


            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    player.isLeftPressed = False

                if event.key == pygame.K_RIGHT:
                    player.isRightPressed = False

                if event.key == pygame.K_UP:
                    player.isTopPressed = False

                if event.key == pygame.K_DOWN:
                    player.isBottomPressed = False

        screen.blit(backgroung, (0, 0))

        for platform in platforms:
            screen.blit(platform.image, platform.rect)

        player.keyPressListener()

        player.updatePosition(platforms)

        player.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()

# venv\Scripts\activate.bat
# python engine\test_loop.py
