import pygame
from pygame.locals import *
from background import Background
from constantes import *
from GUI_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormChapterSelection(Form):
    def __init__(
        self, name, master_surface, x, y, w, h, color_background, color_border, active
    ):
        super().__init__(
            name, master_surface, x, y, w, h, color_background, color_border, active
        )

        self.bg = Background(
            x=0,
            y=0,
            width=self.w,
            height=self.h,
            path="assets/Background/Unknown Nights/Beauty Potion V2.png",
        )

        self.bt_1 = Button(
            master=self,
            x=50,
            y=100,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_chapter_01",
            text="Chapter 01",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_2 = Button(
            master=self,
            x=50,
            y=150,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_chapter_01",
            text="Chapter 02",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_3 = Button(
            master=self,
            x=50,
            y=200,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_chapter_01",
            text="Chapter 03",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_4 = Button(
            master=self,
            x=50,
            y=300,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_title_screen",
            text="Back",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )

        self.lista_widget = [
            self.bt_1,
            self.bt_2,
            self.bt_3,
            self.bt_4,
        ]

    def on_click_boton1(self, parametro):
        if self.pb1.value < self.pb1.value_max:
            self.pb1.value += 1

    def on_click_boton2(self, parametro):
        if self.pb1.value > 0:
            self.pb1.value -= 1

    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.bg.draw(screen=self.surface)
        for aux_widget in self.lista_widget:
            aux_widget.draw()
