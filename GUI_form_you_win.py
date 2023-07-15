import sqlite3
import pygame
from pygame.locals import *
from GUI_form_score import FormScore
from background import Background
from constantes import *
from GUI_form import Form
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormYouWin(Form):
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
            path="assets/Background/Unknown Nights/New Letter.png",
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
            text="YOU WIN",
            font="minimalPixel",
            font_size=150,
            font_color=WHITE,
        )

        self.bt_1 = Button(
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
            text="Retry",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )
        self.bt_2 = Button(
            master=self,
            x=50,
            y=200,
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
            y=250,
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
            y=300,
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
        self.bt_5 = Button(
            master=self,
            x=50,
            y=350,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton3,
            on_click_param="form_chapter_02",
            text="Next Level",
            font="minimalPixel",
            font_size=30,
            font_color=C_WHITE,
        )

        self.bt_update_score = Button(
            master=self,
            x=ANCHO_VENTANA - 300,
            y=150,
            w=200,
            h=40,
            color_background=C_PINK,
            color_border=C_RED,
            on_click=self.update_score,
            on_click_param="",
            text="Update Score",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.txt1 = TextBox(
            master=self,
            x=ANCHO_VENTANA - 300,
            y=50,
            w=240,
            h=40,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",
            text="UserName",
            font="Verdana",
            font_size=30,
            font_color=BLACK,
        )
        self.txt2 = TextBox(
            master=self,
            x=20,
            y=100,
            w=240,
            h=40,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_XL_08.png",
            text="Score",
            font="Verdana",
            font_size=30,
            font_color=BLACK,
        )

        self.label01 = Label(
            master=self,
            x=ANCHO_VENTANA - 300,
            y=100,
            w=240,
            h=40,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text="Score",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.lista_widget = [
            self.label_01,
            self.bt_1,
            self.bt_2,
            self.bt_3,
            self.bt_4,
            self.bt_5,
            self.bt_update_score,
            self.txt1,
            # self.txt2,
            self.label01,
        ]

    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update_score(self, param):
        import sqlite3

        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                conexion.execute(
                    "insert into score (nombre,value) values (?,?)",
                    (self.txt1._text, self.label01._text),
                )
                conexion.commit()  # Actualiza los datos realmente en la tabla
            except:
                print("Error al insertar el puntaje en la base de datos")

    def get_scores(self, param):
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor = conexion.execute("SELECT * FROM score")
            for fila in cursor:
                print(fila)

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
