import pygame
from pygame.locals import *
from background import Background
from constantes import *
from GUI_form import Form
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormSettings(Form):
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
            path="assets/Background/Unknown Nights/Coop Intruder V2.png",
        )

        self.volume = 0.2
        self.flag_play = True

        pygame.mixer.init()
        pygame.mixer.music.load("assets/Sound/24-prison-toys/01 Lure Of The Maw.mp3")
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)

        self.bt_1 = Button(
            master=self,
            x=50,
            y=200,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_subir_vol,
            on_click_param="",
            text="Volumen +",
            font="minimalPixel",
            font_size=50,
            font_color=C_WHITE,
        )
        self.bt_2 = Button(
            master=self,
            x=50,
            y=250,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_bajar_volume,
            on_click_param="",
            text="Volumen -",
            font="minimalPixel",
            font_size=50,
            font_color=C_WHITE,
        )
        self.label01 = Label(
            master=self,
            x=50,
            y=400,
            w=140,
            h=50,
            color_background=BLACK,
            color_border=RED,
            text="Sound Effects Volume",
            font="minimalPixel",
            font_size=50,
            font_color=WHITE,
        )
        self.label02 = Label(
            master=self,
            x=50,
            y=400,
            w=140,
            h=50,
            color_background=BLACK,
            color_border=RED,
            text="Music Volume",
            font="minimalPixel",
            font_size=50,
            font_color=WHITE,
        )

        # self.bt_3 = Button(
        #     master=self,
        #     x=50,
        #     y=300,
        #     w=140,
        #     h=50,
        #     color_background=None,
        #     color_border=None,
        #     image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
        #     on_click=self.on_click_boton3,
        #     on_click_param="form_menu_B",
        #     text="SQL",
        #     font="minimalPixel",
        #     font_size=50,
        #     font_color=C_WHITE,
        # )
        # self.bt_4 = Button(
        #     master=self,
        #     x=50,
        #     y=350,
        #     w=140,
        #     h=50,
        #     color_background=None,
        #     color_border=None,
        #     image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
        #     on_click=self.on_click_boton3,
        #     on_click_param="form_menu_C",
        #     text="Vector",
        #     font="minimalPixel",
        #     font_size=50,
        #     font_color=C_WHITE,
        # )

        self.bt_sound_onoff = Button(
            master=self,
            x=750,
            y=150,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_off_volume,
            on_click_param="",
            text="Master Volume",
            font="minimalPixel",
            font_size=50,
            font_color=C_WHITE,
        )

        self.bt_5 = Button(
            master=self,
            x=50,
            y=450,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_title_screen",
            text="Back",
            font="minimalPixel",
            font_size=50,
            font_color=C_WHITE,
        )

        self.txt1 = TextBox(
            master=self,
            x=500,
            y=50,
            w=400,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",
            text="Text",
            font="minimalPixel",
            font_size=50,
            font_color=C_BLACK,
        )
        self.pb1 = ProgressBar(
            master=self,
            x=500,
            y=150,
            w=240,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",
            image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",
            value=2,
            value_max=10,
        )

        self.lista_widget = [
            self.bt_1,
            self.bt_2,
            self.label01,
            self.label02,
            self.bt_5,
            self.bt_sound_onoff,
            self.txt1,
            self.pb1,
        ]

    # def sound_onoff(self):
    #     pygame.mixer.Sound()

    def on_off_volume(self, parametro):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.bt_sound_onoff._text = "ON"
            self.bt_sound_onoff._font_color = "Red"
            self.flag_play = False
        else:
            pygame.mixer.music.unpause()
            self.bt_sound_onoff._text = "OFF"
            self.bt_sound_onoff._font_color = "Brown"
            self.flag_play = True

    def stop_volume(self, param):
        if self.flag_play:
            pygame.mixer.music.stop()
            self.flag_play = False

    def on_click_subir_vol(self, parametro):
        self.volume += 0.1
        if self.pb1.value < self.pb1.value_max:
            self.pb1.value += 1
            pygame.mixer.music.set_volume(self.volume)

    def on_click_bajar_volume(self, parametro):
        self.volume -= 0.1
        if self.pb1.value > 0:
            self.pb1.value -= 1
            pygame.mixer.music.set_volume(self.volume - 0.1)

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
