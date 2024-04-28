import pygame
from constantes import *


class Character(pygame.sprite.Sprite):
    def __init__(
            self, main_surface: pygame.Surface, x, y, width, height, sprites, animation_delay=3) -> None:
        super().__init__()
        self.main_surface = main_surface
        self.secondary_surface = pygame.Surface((width, height))
        self.rect = self.secondary_surface.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.sprites = sprites
        self.direction = "right"
        self.frame = 0
        self.state = "idle"
        self.animacion_activa = self.sprites[self.state + "_" + self.direction]
        self.secondary_surface = self.animacion_activa[self.frame]

        self.x_vel = 0
        self.y_vel = 0
        self.mask = pygame.mask.from_surface(self.secondary_surface)

        self.fall_count = 0

        self.count = 0
        self.jump_count = 0

        self.animation_delay = animation_delay

        self.GRAVITY = GRAVITY

    def handle_move(self, lista_eventos, keys, objects):
        keys = pygame.key.get_pressed()

        self.x_vel = 0

        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.jump_count < 2:
                    self.jump()

        if keys[pygame.K_LEFT]:
            self.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT]:
            self.move_right(PLAYER_VEL)

        self.handle_vertical_collision(objects, self.y_vel)

    def handle_vertical_collision(self, objects, delta_y):
        collided_objects = []
        for obj in objects:
            if pygame.sprite.collide_mask(self, obj):
                if delta_y > 0:  # Movimiento hacia abajo
                    self.rect.bottom = obj.rect.top
                    self.landed()
                elif delta_y < 0:  # Movimiento hacia arriba
                    self.rect.top = obj.rect.bottom
                    self.hit_head()
                    self.y_vel = 0  # Detener el movimiento vertical

            collided_objects.append(obj)
        return collided_objects

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0

        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.frame = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.frame = 0

    def update_sprite(self):
        self.state = "idle"
        if self.y_vel < 0:
            if self.jump_count == 1:
                self.state = "jump"
            elif self.jump_count == 2:
                self.state = "double_jump"
        elif (
            self.y_vel > 0 and self.jump_count > 0
        ):  # elif self.y_vel > self.GRAVITY * 2
            self.state = "fall"
        elif self.x_vel != 0:
            self.state = "run"

        sprite_sheet_name = self.state + "_" + self.direction
        self.animacion_activa = self.sprites[sprite_sheet_name]
        sprite_index = (
            self.frame // self.animation_delay) % len(self.animacion_activa)

        self.secondary_surface = self.animacion_activa[sprite_index]
        self.frame += 1

        self.update_pos()

    def update(self, delta_ms):
        self.y_vel += min(1, self.fall_count / delta_ms) * self.GRAVITY
        self.move(self.x_vel, self.y_vel, delta_ms)
        # self.GRAVITY
        self.fall_count += 1
        self.update_sprite()
        self.rect.clamp_ip(self.main_surface.get_rect())

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.frame = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, delta_x, delta_y, delta_ms):
        self.apply_delta_x(delta_x)
        self.apply_delta_y(delta_y)

    def apply_delta_x(self, delta_x):
        self.rect.move_ip(delta_x, 0)

    def apply_delta_y(self, delta_y):
        self.rect.move_ip(0, delta_y)

    def update_pos(self):
        self.rect = self.secondary_surface.get_rect(
            topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.secondary_surface)

    def draw(self):
        self.main_surface.blit(self.secondary_surface, self.rect)
