import ast
import pygame
import sys
from random import randrange
from drawers import Level
from models import Knife, Platform, Player

BACKGROUND_COLOR = "#223759"

class Loop: 
    def __init__(self) -> None:
        self.level_data = self.get_level(0)

        self.cell_size = self.level_data["cell_size"]
        self.WINDOW_WIDTH = len(self.level_data["textures_map"][0]) * self.cell_size
        self.WINDOW_HEIGHT = len(self.level_data["textures_map"]) * self.cell_size
    
    def get_level(self, level_id: str | int) -> dict:
        with open(f"./levels/{level_id}.hyi", "r") as file:
            content = file.read()
            return ast.literal_eval(content)

    def add_knife(self, knife_position: tuple[int]) -> None:
        x, y = knife_position
        self.knife = pygame.sprite.GroupSingle()
        knife_sprite = Knife(55, 55)
        self.knife.add(knife_sprite)

    def add_player(self, player_position: tuple[int]) -> None:
        x, y = player_position
        self.player = pygame.sprite.GroupSingle()
        player_sprite = Player(x, y)
        self.player.add(player_sprite)

    def horizontal_movement_collision_listener(self) -> None:
        player = self.player.sprite
        player.rect.x += player.direction.x * player.MOVE_SPEED

        for sprite in self.platforms.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision_listener(self) -> None:
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

    def next_level_collision_listener(self, level_up_platforms: list[pygame.Rect]) -> None:
        player = self.player.sprite

        for platform in level_up_platforms:
            if player.rect.colliderect(platform):
                self.level_up()

    def level_up(self):
        pass

    def main(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dark Knife")

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        backgroung = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        backgroung.fill(pygame.Color(BACKGROUND_COLOR))

        # self.add_knife(0)

        level = Level(self.level_data)
        self.platforms = level.get_platforms()
        
        spawn_coordinates: list = level.get_spawn_coords()
        self.add_player(spawn_coordinates[randrange(len(spawn_coordinates))])

        level_up_coordinates: list = level.get_level_up_coordinates()
        self.next_level_collision_listener([pygame.Rect(coordinate[0], coordinate[1], self.cell_size, self.cell_size) for coordinate in level_up_coordinates])

        while True:
            clock.tick(75)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(backgroung, (0, 0))

            [platform.draw(screen) for platform in self.platforms]

            self.player.update()
            self.horizontal_movement_collision_listener()
            self.vertical_movement_collision_listener()
            self.player.draw(screen)

            # self.knife.update()
            # self.knife.draw(screen)

            pygame.display.update()


if __name__ == "__main__":
    run = Loop()
    run.main()

# Windows
# venv\Scripts\activate.bat
# python engine\test_loop.py

# Linux
# source venv/bin/activate
# python3 engine/test_loop.py
