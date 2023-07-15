import pygame
from constantes import *
from class_support import Support


class Platform:
    def __init__(
        self, main_surface, path_image, x, y, width, height, row, column, type=1
    ):
        self.main_surface = main_surface
        self.image_list = Support.getSurfaceCompact(
            path_image, column, row, width, height
        )

        self.image = self.image_list[type]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self, offset_x):
        self.main_surface.blit(self.image, self.rect)
