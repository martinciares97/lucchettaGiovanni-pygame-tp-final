import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import Button


class Form:
    forms_dict = {}

    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w, h))
        self.slave_rect = self.surface.get_rect(x=x, y=y, w=w, h=h)

        self.active = active
        self.x = x
        self.y = y

        # self.title = "form"
        # self.controles = []

        if self.color_background != None:
            self.surface.fill(self.color_background)

    @staticmethod
    def set_active(name):
        for aux_form in Form.forms_dict.values():
            aux_form.active = False
        Form.forms_dict[name].active = True

    @staticmethod
    def get_active():
        for aux_form in Form.forms_dict.values():
            if aux_form.active:
                return aux_form
        return None

    @staticmethod
    def get_clave_active():
        for clave, valor in Form.forms_dict.items():
            if valor.active:
                return clave
        return None

    def render(self):
        pass

    def update(self, lista_eventos):
        pass

    def draw(self):
        self.master_surface.blit(self.surface, self.slave_rect)
