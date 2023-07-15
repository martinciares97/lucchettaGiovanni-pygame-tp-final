import pygame
from os import listdir
from os.path import join, isfile
from constantes import *


class Support:
    @staticmethod
    def get_background(file_name):
        image = pygame.image.load(join("assets", "Background", file_name))
        _, _, width, height = image.get_rect()
        tiles = []
        rows = SCREEN_HEIGHT // height + 1
        columns = SCREEN_WIDTH // width + 1

        for r in range(rows):
            for c in range(columns):
                coord = (c * width, r * height)
                tiles.append(coord)
        return tiles, image

    @staticmethod
    def flipear(sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

    @staticmethod
    def load_sprite_sheets(dir1, dir2, width, height, direction=True):
        path = join("assets", dir1, dir2)
        images = [f for f in listdir(path) if isfile(join(path, f))]

        all_sprites = {}
        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            columns = sprite_sheet.get_width() // width
            rows = sprite_sheet.get_height() // height

            for row in range(rows):
                sprites = []
                for column in range(columns):
                    x = column * width
                    y = row * height

                    surface_sprite = sprite_sheet.subsurface(x, y, width, height)
                    sprites.append(pygame.transform.scale2x(surface_sprite))

                if direction:
                    all_sprites[image.replace(".png", "") + "_right"] = sprites
                    all_sprites[image.replace(".png", "") + "_left"] = Support.flipear(
                        sprites
                    )
                else:
                    all_sprites[image.replace(".png", "")] = sprites
        return all_sprites

    def get_parallax(path):
        images = [f for f in listdir(path) if isfile(join(path, f))]
        sprite_list = []
        for image in images:
            surface_sprite = pygame.image.load(join(path, image)).convert_alpha()
            sprite_list.append(surface_sprite)
        return sprite_list()
