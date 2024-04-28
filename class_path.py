import pygame
from os.path import join

class Path:
    def __init__(self, *args) -> None:
        self.image = pygame.image.load(join(*args))
