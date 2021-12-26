import ast
import pygame, sys
from textures import drawer
from models import hero
from textures import drawer
from models import hero


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

    player = pygame.sprite.GroupSingle()
    player_sprite = hero.Player(55,55)
    player.add(player_sprite)

    level = drawer.Level(LEVEL)
    platforms = level.create_platforms()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(backgroung, (0,0))

        player.update()

        for platform in platforms:
            screen.blit(platform.image, platform.rect)

        
        player.draw(screen)

        pygame.display.update()
        
if __name__ == "__main__":
    main()

# venv\Scripts\activate.bat 
# python engine\test_loop.py