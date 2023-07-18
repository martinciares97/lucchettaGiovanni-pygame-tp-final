import sys
import pygame
from pygame.locals import *
from background import Background
from constantes import *
from GUI_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormTitleScreen(Form):
    def __init__(
        self, name, master_surface, x, y, w, h, color_background, color_border, active
    ):
        super().__init__(
            name, master_surface, x, y, w, h, color_background, color_border, active
        )

        self.active_button_index = (
            0  # Variable para rastrear el índice del botón activo
        )

        self.bt_1 = Button(
            master=self,
            x=50,
            y=300,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_chapter_01",
            text="New Game",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_2 = Button(
            master=self,
            x=50,
            y=350,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_chapter_selection",
            text="Chapter Selection",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_3 = Button(
            master=self,
            x=50,
            y=400,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_settings",
            text="Settings",
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
            on_click=self.on_click_boton3,
            on_click_param="form_score",
            text="Score",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_5 = Button(
            master=self,
            x=50,
            y=500,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.quit_game,
            on_click_param="form_settings",
            text="Quit Game",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )

        self.lista_widget = [
            self.bt_1,
            self.bt_2,
            self.bt_3,
            self.bt_4,
            self.bt_5,
        ]

        self.bg = Background(
            x=0,
            y=0,
            width=self.w,
            height=self.h,
            path="assets/Background/Unknown Nights/Abandoned Hardware.png",
        )

    def quit_game(self, param):
        pygame.quit()
        sys.exit()

    def on_click_boton1(self, parametro):
        if self.pb1.value < self.pb1.value_max:
            self.pb1.value += 1

    def on_click_boton2(self, parametro):
        if self.pb1.value > 0:
            self.pb1.value -= 1

    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos, keys, delta_ms):
        for event in lista_eventos:
            if event.type == KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.active_button_index = (self.active_button_index + 1) % len(
                        self.lista_widget
                    )
                elif event.key == pygame.K_UP:
                    self.active_button_index = (self.active_button_index - 1) % len(
                        self.lista_widget
                    )
                if event.key == pygame.K_SPACE:
                    self.set_active(
                        self.lista_widget[self.active_button_index].on_click_param
                    )

        for indice_wid, aux_widget in enumerate(self.lista_widget):
            aux_widget.set_bt_active(indice_wid == self.active_button_index)
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.bg.draw(screen=self.surface)
        for aux_widget in self.lista_widget:
            aux_widget.draw()
