from typing import final
import pygame
import sys
import os
import re
from random import randrange

from utils import Level
from models import Knife, Platform, Player
from controllers import PlayerController, LevelController, KnifeController, MobsController

BACKGROUND_COLOR = "#223759"


class Loop:

    def __init__(self) -> None:
        self.absolute_folder = re.sub(os.path.basename(
            __file__), "", os.path.abspath(__file__))

        self.observers = []

        self.level_controller = LevelController(self)
        self.player_controller = PlayerController(self)
        self.knife_controller = KnifeController(self)
        self.mob_controller = MobsController(self)

        #! обязательно должен быть первым, он должен подтягивать изменения первым, чтобы уже от него другие контроллеры все подтягивали
        self.add_observer(self)

        self.add_observer(self.player_controller)
        self.add_observer(self.knife_controller)
        self.add_observer(self.mob_controller)

        # в нем вызывается метод notify_changes, который вызывает метод change у каждого объекта, которого мы хотим оповестить о загрузке нового уровня, для того чтобы он самостоятельно подтянул изменения
        self.level_controller.load_next_level()

        self.main()

    def add_observer(self, model) -> None:
        self.observers.append(model)

    def notify_changes(self) -> None:
        [observer.change(self) for observer in self.observers]

    def create_picture(self, picture_group, picture_name, scale):
        abs_path = os.path.abspath(__file__)
        final_path = fr'''{abs_path[:-12]}resources\images\{picture_group}\{picture_name}.png'''
        picture = pygame.image.load(final_path)
        resized_picture = pygame.transform.scale(picture, scale)

        return resized_picture

    def change(self, заглушка_намомни_мне_это_исправить_без_нее_не_работает) -> None:
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = self.level_controller.WINDOW_WIDTH, self.level_controller.WINDOW_HEIGHT
        self.WINDOW_SCALE = (self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.platforms = self.level_controller.platforms
        self.level_up_platforms = self.level_controller.level_up_platforms
        self.enemy_spawn_platforms = self.level_controller.enemy_spawn_platforms
        self.knifes = self.knife_controller.knifes
        self.mobs = self.mob_controller.mobs
        for i in self.enemy_spawn_platforms:
            print(i.rect.x, i.rect.y)

        spawn_platform: Platform = self.level_controller.spawn_coordinates
        self.player: Player = self.player_controller.spawn_player(
            (spawn_platform.rect.left, spawn_platform.rect.top))
        self.player_controller.set_animation()

    def main(self) -> None:
        pygame.init()
        pygame.display.set_caption("Dark Knife")

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.WINDOW_SCALE)

        backgroung = self.create_picture(
            "background", "desert", self.WINDOW_SCALE)

        while True:
            clock.tick(75)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(backgroung, (0, 0))

            self.knife_controller.display(screen)
            self.level_controller.display(screen)
            self.mob_controller.display(screen)
            self.player_controller.display(screen)

            pygame.display.update()


if __name__ == "__main__":
    run = Loop()

# Windows
# venv\Scripts\activate.bat
# python engine\test_loop.py

# Linux
# source venv/bin/activate
# python3 engine/test_loop.py
