import pygame
from pygame.locals import *
from GUI_form import Form
from GUI_form_chapter_01 import FormChapter01
from background import Background
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *


class FormPause(Form):
    def __init__(
        self, name, master_surface, x, y, w, h, color_background, color_border, active
    ):
        super().__init__(
            name, master_surface, x, y, w, h, color_background, color_border, active
        )

        self.tamaño_boton = (200, 40)
        self.bg = Background(
            x=0,
            y=0,
            width=self.w,
            height=self.h,
            path="assets/Background/Unknown Nights/New Letter.png",
        )

        self.bt1 = Button(
            master=self,
            x=self.w / 2 - (self.tamaño_boton[0] / 2),
            y=100,
            w=200,
            h=40,
            color_background=C_GREEEN_2,
            color_border=C_YELLOW_2,
            on_click=self.on_click_boton1,
            on_click_param="form_chapter_01",
            text="Resume",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.bt2 = Button(
            master=self,
            x=self.w / 2 - (self.tamaño_boton[0] / 2),
            y=50,
            w=200,
            h=40,
            color_background=C_GREEEN_2,
            color_border=C_YELLOW_2,
            on_click=self.on_click_boton1,
            on_click_param="form_chapter_01",
            text="Retry",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.bt3 = Button(
            master=self,
            x=self.w / 2 - (self.tamaño_boton[0] / 2),
            y=150,
            w=200,
            h=40,
            color_background=C_GREEEN_2,
            color_border=C_YELLOW_2,
            on_click=self.on_click_boton1,
            on_click_param="form_settings",
            text="Settings",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.bt4 = Button(
            master=self,
            x=self.w / 2 - (self.tamaño_boton[0] / 2),
            y=200,
            w=200,
            h=40,
            color_background=C_GREEEN_2,
            color_border=C_YELLOW_2,
            on_click=self.on_click_boton1,
            on_click_param="form_title_screen",
            text="Exit to Main Menu",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.lista_widget = [
            self.bt1,
            self.bt2,
            self.bt3,
            self.bt4,
        ]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()

        self.bg.draw(screen=self.surface)

        for aux_widget in self.lista_widget:
            aux_widget.draw()
