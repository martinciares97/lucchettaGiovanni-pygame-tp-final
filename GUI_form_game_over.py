import pygame
from pygame.locals import *
from class_background import Background
from constantes import *
from GUI_form import Form
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormGameOver(Form):
    def __init__(
        self, name, master_surface, x, y, w, h, color_background, color_border, active
    ):
        super().__init__(
            name, master_surface, x, y, w, h, color_background, color_border, active
        )

        self.bg = Background(
            x=0,
            y=0,
            w=self.w,
            h=self.h,
            path="assets/Background/Unknown Nights/Puppet King.png",
        )

        self.label_01 = Label(
            master=self,
            x=ANCHO_VENTANA / 2 - 250,
            y=ALTO_VENTANA / 2,
            w=500,
            h=200,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text="Game Over",
            font="minimalPixel",
            font_size=150,
            font_color=WHITE,
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
            text="Retry",
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
            on_click_param="form_title_screen",
            text="Return to main menu",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_3 = Button(
            master=self,
            x=50,
            y=300,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_score",
            text="Score",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_4 = Button(
            master=self,
            x=50,
            y=450,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.quit,
            on_click_param="Quit",
            text="Quit Game",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )

        self.lista_widget = [
            self.label_01,
            self.bt_1,
            self.bt_2,
            self.bt_3,
            self.bt_4,
        ]

    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def quit(self, param):
        pygame.quit()

    def draw(self):
        super().draw()

        self.bg.draw(screen=self.surface)

        for aux_widget in self.lista_widget:
            aux_widget.draw()
