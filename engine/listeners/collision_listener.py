from types import MethodType
from multipledispatch import dispatch
from typing import Any, T
import pygame


class CollisionListener:
    """Делаю так, потому, что возможно перегрузка, в данном случае у нас есть только связь одна ко многим (Player, Platforms), но также возможно что будет (Knifes, Platforms) - это уже многие ко многим, или один к одному"""

    @dispatch(pygame.sprite.Group, pygame.sprite.Sprite, MethodType)
    def on_collide(self, objects: pygame.sprite.Group, object: pygame.sprite.Sprite, callback = lambda x: x) -> pygame.sprite.Sprite:
        self.on_collide(object, objects, callback)

    @dispatch(pygame.sprite.Sprite, pygame.sprite.Group, MethodType)
    def on_collide(self, object: pygame.sprite.Sprite, objects: pygame.sprite.Group, callback = lambda x: x) -> pygame.sprite.Sprite:
        for sprite in objects:
            if sprite.rect.colliderect(object.rect):
                if callback:
                    return callback(sprite)
                return sprite

    @dispatch(pygame.sprite.Sprite, pygame.sprite.Sprite, MethodType)
    def on_collide(self, object_1: pygame.sprite.Sprite, object_2: pygame.sprite.Sprite, callback = lambda x: x) -> bool:
        if object_1.rect.colliderect(object_2.rect):
            if callback:
                return callback()
            return True