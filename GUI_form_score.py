import pygame
from pygame.locals import *
from GUI_form import Form
from background import Background
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *

import sqlite3


class FormScore(Form):
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
            path="assets/Background/Unknown Nights/Lovecraftian Train V2.png",
        )

        self.bt_update_score = Button(
            master=self,
            x=20,
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

        self.bt_create_table = Button(
            master=self,
            x=20,
            y=200,
            w=200,
            h=40,
            color_background=C_PINK,
            color_border=C_RED,
            on_click=self.create_table,
            on_click_param="",
            text="Create Table",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.bt_get_scores = Button(
            master=self,
            x=20,
            y=250,
            w=200,
            h=40,
            color_background=C_PINK,
            color_border=C_RED,
            on_click=self.get_scores,
            on_click_param="",
            text="Show Score",
            font="Verdana",
            font_size=30,
            font_color=BLACK,
        )

        self.bt_delete_score = Button(
            master=self,
            x=25,
            y=300,
            w=200,
            h=40,
            color_background=C_PINK,
            color_border=C_RED,
            on_click=self.delete_score,
            on_click_param="",
            text="Borrar datos",
            font="Verdana",
            font_size=30,
            font_color=BLACK,
        )

        self.bt_back = Button(
            master=self,
            x=20,
            y=350,
            w=200,
            h=40,
            color_background=C_GREEEN_2,
            color_border=C_YELLOW_2,
            on_click=self.on_click_boton1,
            on_click_param="form_title_screen",
            text="Back",
            font="minimalPixel",
            font_size=30,
            font_color=BLACK,
        )

        self.txt1 = TextBox(
            master=self,
            x=20,
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
            x=20,
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
            self.bt_back,
            self.bt_update_score,
            self.bt_create_table,
            self.bt_get_scores,
            self.bt_delete_score,
            self.txt1,
            self.txt2,
        ]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    # def update_score(self, nombre, valor):
    #     with sqlite3.connect("db/db_score.db") as conexion:
    #         try:
    #             conexion.execute(
    #                 "INSERT INTO score (nombre, value) VALUES (?, ?)",
    #                 (nombre, valor)
    #             )
    #             conexion.commit()
    #         except:
    #             print("Error al insertar el puntaje en la base de datos")

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

    def delete_score(self, param):
        import sqlite3

        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                conexion.execute("DELETE FROM score")
                conexion.commit()  # Actualiza los datos realmente en la tabla
            except:
                print("Error al borrar los datos")

    def create_table(self, param):
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                sentencia = """ create  table score
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        value real
                                )
                            """
                conexion.execute(sentencia)
                print("Se creo la tabla personajes")
            except sqlite3.OperationalError:
                print("La tabla ya existe")

    def get_scores(self, param):
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor = conexion.execute("SELECT * FROM score")
            for fila in cursor:
                print(fila)

    def update(self, lista_eventos, keys, delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.bg.draw(screen=self.surface)
        for aux_widget in self.lista_widget:
            aux_widget.draw()
