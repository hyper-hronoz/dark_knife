import ast
import pygame
import sys
from textures import drawer
from models import hero
from textures import drawer
from models import hero


with open(r"./levels/1.hyi", "r") as file:
    content = file.read()
    LEVEL = ast.literal_eval(content)
    cell_size = LEVEL["cell_size"]
    WINDOW_WIDTH = len(LEVEL["textures_map"][0]) * cell_size
    WINDOW_HEIGHT = len(LEVEL["textures_map"]) * cell_size

DISPLAY = (WINDOW_WIDTH, WINDOW_HEIGHT)
BACKGROUND_COLOR = "#223759"


class Level:
    def add_player(self):
        self.player = pygame.sprite.GroupSingle()
        player_sprite = hero.Player(55, 55)
        self.player.add(player_sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * hero.MOVE_SPEED

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.gravity()

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.isJump = False

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(DISPLAY)
        clock = pygame.time.Clock()
        pygame.display.set_caption("Dark Knife")
        backgroung = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

        backgroung.fill(pygame.Color(BACKGROUND_COLOR))

        self.add_player()

        level = drawer.Level(LEVEL)
        self.platforms = level.create_platforms()

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(backgroung, (0, 0))

            for platform in self.platforms:
                screen.blit(platform.image, platform.rect)

            self.player.update()
            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.player.draw(screen)

            pygame.display.update()


if __name__ == "__main__":
    run = Level()
    run.main()

# Windows
# venv\Scripts\activate.bat
# python3 engine\test_loop.py

# Linux
# source venv/bin/activate
# python3 engine/test_loop.py
