import pygame
from pygame.locals import *
from auxiliar import Auxiliar
from class_background import Background
from class_mosaico import Mosaico
from class_parallax import Parallax
from constantes import *
from GUI_form import Form
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from object import Block

from sys import exit
from os.path import join


class FormInit(Form):
    def __init__(
        self, name, master_surface, x, y, w, h, color_background, color_border, active
    ):
        super().__init__(
            name, master_surface, x, y, w, h, color_background, color_border, active
        )

        # self.bg_parallax = Auxiliar.get_parallax("assets/Background/The Dawn/")
        self.bg_parallax = Parallax(
            0, 0, ANCHO_VENTANA, ALTO_VENTANA, None, "assets/Background/The Dawn/Layers")
        
        self.background = Background(x=0,y=0,w=w,h=h,path="assets/Background/Blue.png")
        
        self.label_01 = Label(
            master=self,
            x=ANCHO_VENTANA / 2 - 200,
            y=ALTO_VENTANA - 100,
            w=400,
            h=60,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text="Presione Enter para comenzar",
            font="minimalPixel",
            font_size=30,
            font_color=WHITE,
        )
        
        self.lista_widget = [self.label_01]
        
        
        # superficie_mosaico = pygame.image.load(join("assets", "Background", "Yellow.png")).convert_alpha()
        # background_mosaico = Mosaico(self.master_surface, superficie_mosaico, 0, 0, "Yellow.png")

    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos, keys, delta_ms):
        if keys[pygame.K_SPACE]:
            Form.set_active("form_title_screen")
        self.bg_parallax.handle_move(keys)
        self.bg_parallax.update()

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
            
            
    def draw(self):
        super().draw()
        self.bg_parallax.draw(self.surface)

        for aux_widget in self.lista_widget:
            aux_widget.draw()
