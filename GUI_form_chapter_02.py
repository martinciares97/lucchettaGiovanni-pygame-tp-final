import pygame
from pygame.locals import *
from class_platform import Platform
from class_player import Character
from constantes import *
from GUI_form import Form
from debug_mod import *
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from loot import Loot
from object import Block
from player import Player
from enemigo import Enemy
from background import Background, Parallax
from bullet import Bullet
from os import listdir
from os.path import join, isfile

from support import Support


class FormChapter02(Form):
    def __init__(
        self, name, master_surface, x, y, w, h, color_background, color_border, active
    ):
        super().__init__(
            name, master_surface, x, y, w, h, color_background, color_border, active
        )

        # --- GUI WIDGET ---
        self.game_over = False
        self.you_win = False
        self.in_game = False
        self.tiempo_juego = 60000

        self.items_looteados = 0

        self.platform_list = []
        self.bullet_list = []
        self.items_list = []
        self.enemy_list = []
        self.block_list = []

        self.SPRITES = Support.load_sprite_sheets("MainCharacters", "MaskDude", 32, 32)
        self.SPRITES_P2 = Support.load_sprite_sheets("MainCharacters", "1x", 64, 64)
        self.items = Support.load_sprite_sheets(
            dir1="Items", dir2="Fruits", width=32, height=32, direction=False
        )
        self.block_size = 96

        for row_num, row in enumerate(MAPA):
            for column_num, column in enumerate(row):
                x = column_num * 25
                y = row_num * 25
                if column == "c":
                    self.jugador = Player(
                        sprites=self.SPRITES_P2,
                        x=x,
                        y=y,
                        speed_walk=6,
                        speed_run=12,
                        gravity=14,
                        jump_power=30,
                        frame_rate_ms=100,
                        move_rate_ms=50,
                        jump_height=140,
                        p_scale=1,
                        interval_time_jump=300,
                    )
                if column == "b":
                    self.platform_list.append(
                        Platform(
                            main_surface=self.surface,
                            path_image=PATH_BLOCKS,
                            x=x,
                            y=y,
                            width=25,
                            height=25,
                            row=32,
                            column=32,
                            type=328,
                        )
                    )
                if column == "f":
                    self.platform_list.append(
                        Platform(
                            main_surface=self.surface,
                            path_image=PATH_BLOCKS,
                            x=x,
                            y=y,
                            width=25,
                            height=25,
                            row=32,
                            column=32,
                            type=938,
                        )
                    )
                if column == "p":
                    self.platform_list.append(
                        Platform(
                            main_surface=self.surface,
                            path_image=PATH_BLOCKS,
                            x=x,
                            y=y,
                            width=25,
                            height=25,
                            row=32,
                            column=32,
                            type=937,
                        )
                    )
                if column == "i":
                    self.items_list.append(
                        Loot(
                            main_surface=self.surface,
                            items=self.items,
                            x=x,
                            y=y,
                            width=25,
                            height=25,
                        )
                    )
                if column == "e":
                    self.enemy_list.append(
                        Enemy(
                            x=x,
                            y=y,
                            speed_walk=6,
                            speed_run=5,
                            gravity=14,
                            jump_power=30,
                            frame_rate_ms=150,
                            move_rate_ms=50,
                            jump_height=140,
                            p_scale=0.08,
                            interval_time_jump=300,
                        )
                    )

    def init_level(self):
        self.bg_parallax = Parallax(
            0, 0, ANCHO_VENTANA, ALTO_VENTANA, None, "assets/Background/The Dawn/"
        )
        self.tiempo_transcurrido = 0
        self.score = 0
        self.dir_shoot_x = 0

        self.bt_pause = Button(
            master=self,
            x=ANCHO_VENTANA - 140,
            y=0,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_boton1,
            on_click_param="form_pause",
            text="Pause",
            font="Verdana",
            font_size=30,
            font_color=C_WHITE,
        )

        self.bt_shoot = Button(
            master=self,
            x=ANCHO_VENTANA - 140,
            y=ALTO_VENTANA - 400,
            w=140,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",
            on_click=self.on_click_shoot,
            on_click_param="",
            text="SHOOT",
            font="Verdana",
            font_size=30,
            font_color=C_WHITE,
        )

        self.label_score = Label(
            master=self,
            x=ANCHO_VENTANA / 2 - 100,
            y=20,
            w=200,
            h=80,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text=f"Score {self.score}",
            font="minimalPixel",
            font_size=90,
            font_color=WHITE,
        )

        self.label_time = Label(
            master=self,
            x=ANCHO_VENTANA / 2 - 100,
            y=20,
            w=200,
            h=80,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text=f"Tiempo {self.tiempo_transcurrido}",
            font="minimalPixel",
            font_size=90,
            font_color=WHITE,
        )

        self.label_items = Label(
            master=self,
            x=10,
            y=80,
            w=200,
            h=60,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text=f"Items {self.items_looteados}",
            font="minimalPixel",
            font_size=90,
            font_color=WHITE,
        )

        self.label_lives = Label(
            master=self,
            x=260,
            y=20,
            w=50,
            h=50,
            color_background=BLACK,
            color_border=RED,
            image_background=None,
            text=f"5",
            font="minimalPixel",
            font_size=90,
            font_color=WHITE,
        )

        self.pb_lives = ProgressBar(
            master=self,
            x=10,
            y=20,
            w=240,
            h=50,
            color_background=None,
            color_border=None,
            image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",
            image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",
            value=5,
            value_max=5,
        )

        self.widget_list = [
            self.bt_pause,
            self.pb_lives,
            self.bt_shoot,
            self.label_score,
            self.label_time,
            self.label_items,
            self.label_lives,
        ]

        # --- GAME ELEMNTS ---

        self.static_background = Background(
            x=0,
            y=0,
            width=self.w,
            height=self.h,
            path="images/locations/set_bg_01/forest/all.png",
        )

        self.main_char = Character(
            main_surface=self.surface,
            x=SCREEN_WIDTH - 100,
            y=400,
            width=100,
            height=100,
            sprites=self.SPRITES,
            animation_delay=3,
        )

        # MAPEADO

        self.floor = [
            Block(
                self.surface,
                i * self.block_size,
                ALTO_VENTANA - self.block_size,
                self.block_size,
            )
            for i in range(
                -ANCHO_VENTANA // self.block_size, ANCHO_VENTANA * 2 // self.block_size
            )
        ]

        self.offset_x = 0  # compensacion desplazmiento en x
        self.scroll_area_width = 200

    def set_score(self, score):
        self.score += score

    def colision_player(self):
        contador = 0
        for enemigo in self.enemy_list:
            if self.jugador.collition_rect.colliderect(enemigo.rect):
                print("IMPACTO ENEMY")
                self.enemy_list.pop(contador)
                self.score += 100
                print(self.score)
                contador += 1

    def colision_items(self):
        contador = 0
        for item in self.items_list:
            if self.jugador.collition_rect.colliderect(item.rect):
                self.items_list.pop(contador)
                self.score += 100
                print(self.score)
                contador += 1

    def check_impact(self, plataform_list, enemy_list, player):
        for aux_enemy in enemy_list:
            if (
                self.is_active
                and self.owner != aux_enemy
                and self.collide_rect.colliderect(aux_enemy.rect)
            ):
                print("IMPACTO ENEMY")
                self.is_active = False

    def retry_level(self):
        if self.game_over:
            self.jugador.lives = 5

    def you_win_metod(self):
        if len(self.enemy_list) == 0:
            self.you_win = True
            self.in_game = False
            self.set_active("form_you_win")

    def game_over_metod(self):
        if self.jugador.lives <= 0:
            self.game_over = True
            self.in_game = False
            self.set_active("form_game_over")

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        for enemy in self.enemy_list:
            self.bullet_list.append(
                Bullet(
                    owner=enemy,
                    x_init=enemy.rect.centerx,
                    y_init=enemy.rect.centery,
                    x_end=self.jugador.rect.centerx,
                    y_end=self.jugador.rect.centery,
                    speed=20,
                    path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",
                    frame_rate_ms=100,
                    move_rate_ms=20,
                    width=5,
                    height=5,
                )
            )

    def get_position(self):
        pos = []
        pos.append(self.jugador.collition_rect.centerx)
        pos.append(self.jugador.collition_rect.centery)
        return pos

    def on_click_shoot_player(self):
        flip_shoot = False
        if self.jugador.direction == DIRECTION_R:
            self.dir_shoot_x = ANCHO_VENTANA
        elif self.jugador.direction == DIRECTION_L:
            self.dir_shoot_x = 0
            flip_shoot = True

        self.bullet_list.append(
            Bullet(
                owner=self.jugador,
                x_init=self.jugador.collition_rect.centerx,
                y_init=self.jugador.collition_rect.centery,
                x_end=self.dir_shoot_x,
                y_end=self.get_position()[1],
                speed=10,
                path="assets/MainCharacters/1x/range-projectile.png",
                frame_rate_ms=80,
                move_rate_ms=40,
                width=200,
                height=200,
                flip_x=flip_shoot,
            )
        )

    def harly_events(self, lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and self.jugador.is_shoot == False:
                    self.on_click_shoot_player()
                    self.jugador.is_shoot = True
                if event.key == pygame.K_a:
                    self.colision_player()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    self.jugador.is_shoot = False

            self.colision_items()

    def update(self, lista_eventos, keys, delta_ms):
        if self.active and self.in_game == False:
            self.in_game = True
            self.init_level()

        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido >= self.tiempo_juego:
            self.jugador.lives = 0
            self.game_over_metod()

        self.harly_events(lista_eventos)
        self.game_over_metod()
        self.you_win_metod()

        self.bg_parallax.handle_move(keys)
        self.bg_parallax.update()

        for widget in self.widget_list:
            widget.update(lista_eventos)

        for bullet in self.bullet_list:
            bullet.update(delta_ms, self.platform_list, self.enemy_list, self.jugador)

        for enemy in self.enemy_list:
            enemy.update(delta_ms, self.platform_list)

        self.main_char.handle_move(lista_eventos, keys, self.floor)
        self.main_char.update(delta_ms)

        self.jugador.events(
            delta_ms,
            keys,
        )
        self.jugador.update(delta_ms, self.platform_list)

        self.pb_lives.value = self.jugador.lives

        for item in self.items_list:
            item.update(delta_ms)

    def draw(self):
        super().draw()

        if (
            self.main_char.rect.right - self.offset_x
            >= ANCHO_VENTANA - self.scroll_area_width
            and self.main_char.x_vel > 0
        ) or (
            self.main_char.rect.left - self.offset_x <= self.scroll_area_width
            and self.main_char.x_vel < 0
        ):
            self.offset_x += self.main_char.x_vel

        self.bg_parallax.draw(self.surface)

        for block in self.block_list:
            block.draw(self.offset_x)

        for widget in self.widget_list:
            widget.draw()

        for block in self.floor:
            block.draw(self.offset_x)

        for platform in self.platform_list:
            platform.draw(self.offset_x)

        for enemy in self.enemy_list:
            enemy.draw(self.surface, self.offset_x)

        for bullet in self.bullet_list:
            bullet.draw(self.surface)

        for item in self.items_list:
            item.draw(self.offset_x)

        self.main_char.draw()

        self.jugador.draw(self.surface)

        if get_mode():
            print("rect.x", self.main_char.rect.x, "rect.y", self.main_char.rect.y)
            pygame.draw.rect(self.surface, RED, self.main_char.rect, 3)
