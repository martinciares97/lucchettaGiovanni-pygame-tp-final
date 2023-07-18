import pygame
from pygame.locals import *
import sys
from GUI_form_chapter_selection import FormChapterSelection
from GUI_form_game_over import FormGameOver
from GUI_form_init import FormInit
from GUI_form_pause import FormPause
from GUI_form_settings import FormSettings
from GUI_form_title_screen import FormTitleScreen
from GUI_form_you_win import FormYouWin
from constantes import *
from GUI_form import Form
from debug_mod import set_mode
from GUI_form_score import FormScore
from gui_form_menu_A import FormMenuA
from gui_form_menu_C import FormMenuC
from GUI_form_chapter_01 import FormChapter01
from GUI_form_chapter_02 import FormChapter02
from GUI_form_chapter_03 import FormChapter03

flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Pequeña perdicion")

form_init = FormInit(
    name="form_init",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=YELLOW,
    color_border=RED,
    active=True,
)

form_title_screen = FormTitleScreen(
    name="form_title_screen",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=BLACK,
    color_border=RED,
    active=False,
)

form_settings = FormSettings(
    name="form_settings",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=GOLD,
    color_border=MAGENTA,
    active=False,
)

form_chapter_selection = FormChapterSelection(
    name="form_chapter_selection",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=BLACK,
    color_border=RED,
    active=False,
)

form_pause = FormPause(
    name="form_pause",
    master_surface=screen,
    x=300,
    y=200,
    w=ANCHO_VENTANA * 0.60,
    h=ALTO_VENTANA * 0.60,
    color_background=(VIOLET),
    color_border=(RED),
    active=False,
)

form_chapter_01 = FormChapter01(
    name="form_chapter_01",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=(VIOLET),
    color_border=(RED),
    active=False,
)

form_chapter_02 = FormChapter02(
    name="form_chapter_02",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=(VIOLET),
    color_border=(RED),
    active=False,
)


form_score = FormScore(
    name="form_score",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=(VIOLET),
    color_border=(RED),
    active=False,
)

form_game_over = FormGameOver(
    name="form_game_over",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=BLACK,
    color_border=RED,
    active=False,
)

form_game_over = FormYouWin(
    name="form_you_win",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=BLACK,
    color_border=RED,
    active=False,
)

form_menu_C = FormMenuC(
    name="form_menu_C",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=(VIOLET),
    color_border=(RED),
    active=False,
)

form_chapter_03 = FormChapter03(
    name="form_chapter_03",
    master_surface=screen,
    x=0,
    y=0,
    w=ANCHO_VENTANA,
    h=ALTO_VENTANA,
    color_background=(VIOLET),
    color_border=(RED),
    active=False,
)

while True:
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                set_mode()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if aux_form_active != None:
        aux_form_active.update(lista_eventos, keys, delta_ms)
        aux_form_active.draw()

    pygame.display.flip()
