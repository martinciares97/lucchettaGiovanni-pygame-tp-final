import pygame
from pygame.locals import *
from constantes import *
from auxiliar import Auxiliar
from os import listdir
from os.path import join, isfile

from object import Block


class Background:
    def __init__(self, x, y, width, height, path=None):
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        if path != None:
            self.image = pygame.image.load(path).convert()
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Parallax(Background):
    def __init__(self, x, y, width, height, path, path_dir):
        super().__init__(x, y, width, height, path)
        self.width = width
        self.height = height
        self.sprite_list = self.get_parallax(path_dir)
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)
        self.frame = 0
        self.scroll = 0
        self.delta_x = 0
        self.speed = 1

    def get_parallax(self, path) -> list:
        images = [f for f in listdir(path) if isfile(join(path, f))]
        sprite_list = []
        for image in images:
            surface_sprite = pygame.image.load(join(path, image)).convert_alpha()
            sprite_list.append(
                pygame.transform.scale(surface_sprite, (ANCHO_VENTANA, ALTO_VENTANA))
            )

        return sprite_list

    def handle_move(self, events):
        self.delta_x = 0
        if events[pygame.K_RIGHT]:
            self.delta_x = 5
        if events[pygame.K_LEFT]:
            self.delta_x = -5

    def update(self):
        self.scroll += self.delta_x

    def draw(self, screen: pygame.Surface):
        for x in range(-ANCHO_VENTANA // self.width, ANCHO_VENTANA * 2 // self.width):
            self.speed = 1
            for image in self.sprite_list:
                screen.blit(image, ((x * 1100) - self.scroll * self.speed, 0))
                self.speed += 0.1
