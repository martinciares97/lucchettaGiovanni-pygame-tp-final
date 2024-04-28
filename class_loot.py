import pygame

from constantes import *
from debug_mod import get_mode


class Loot:
    def __init__(self, main_surface: pygame.Surface, items, x, y, w=100, h=100, name=None,) -> None:
        self.main_surface = main_surface
        self.name = name
        self.width = w
        self.height = h
        self.frame = 0
        self.items = items
        self.animacion_activa = self.items["Apple"]
        self.surface = self.animacion_activa[self.frame]
        self.rect = self.surface.get_rect(x=x, y=y, w=w, h=h)
        self.tiempo_transcurrido_animacion = 0
        self.tiempo_actualizacion_frame = 50
        

    def update(self, delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if self.tiempo_transcurrido_animacion > self.tiempo_actualizacion_frame:
            self.tiempo_transcurrido_animacion = 0
            self.frame += 1
            if self.frame >= len(self.animacion_activa):
                self.frame = 0
            self.surface = self.animacion_activa[self.frame]


    def draw(self, offset_x):
        self.main_surface.blit(self.surface, self.rect)
        if get_mode():
            pygame.draw.rect(self.main_surface, color=RED,
                             rect=self.rect, width=3)
