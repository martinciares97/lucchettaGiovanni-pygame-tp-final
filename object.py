import pygame
from os import listdir
from os.path import isfile, join


class Object(pygame.sprite.Sprite):
    def __init__(
        self, main_surface: pygame.Surface, x, y, width=100, height=100, name=None
    ) -> None:
        super().__init__()
        self.main_surface = main_surface

        self.name = name
        self.width = width
        self.height = height
        # self.sec_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        # self.sec_rect = self.sec_surface.get_rect()
        # self.sec_rect.x = x
        # self.sec_rect.y = y
        self.sec_rect = pygame.Rect(x, y, width, height)
        self.sec_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    def draw(self, offset_x):
        # self.main_surface.blit(self.sec_surface,self.sec_rect)
        self.main_surface.blit(
            self.sec_surface, (self.sec_rect.x - offset_x, self.sec_rect.y)
        )


class Block(Object):
    def __init__(self, main_surface, x, y, size) -> None:
        super().__init__(main_surface, x, y, size, size)
        self.block = self.get_block(size)
        self.rect = self.block.get_rect()
        self.rect.x = x  # Establecer la posición en el eje x utilizando rect.x
        self.rect.y = y  # Establecer la posición en el eje y utilizando rect.y
        self.sec_surface.blit(self.block, (0, 0))
        self.mask = pygame.mask.from_surface(self.sec_surface)

    def get_block(self, size):
        path = join("assets", "Terrain", "Terrain.png")
        image = pygame.image.load(path)
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96, 0, size, size)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
