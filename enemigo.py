from debug_mod import get_mode
from player import *
from constantes import *
from auxiliar import Auxiliar


class Enemy:
    def __init__(
        self,
        s_sheet,
        x,
        y,
        speed_walk,
        speed_run,
        gravity,
        jump_power,
        frame_rate_ms,
        move_rate_ms,
        jump_height,
        p_scale=1,
        interval_time_jump=100,
    ) -> None:
        self.s_sheets = s_sheet

        self.frame = 0
        self.estado = "idle"
        self.direction = "right"
        self.key = f"{self.estado}_{self.direction}"

        self.idle_r = self.s_sheets["idle_right"]
        self.idle_l = self.s_sheets["idle_left"]
        self.walk_r = self.s_sheets["walk_right"]
        self.walk_l = self.s_sheets["walk_left"]
        self.attack_r = self.s_sheets["attack_fail_right"]
        self.attack_l = self.s_sheets["attack_fail_left"]
        self.animation = self.idle_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = pygame.Rect(self.image.get_rect())
        self.rect.x = x
        self.rect.y = y

        self.collision_rect = pygame.Rect(
            x + self.rect.width / 3, y, self.rect.width / 3, self.rect.height
        )
        self.ground_collision_rect = pygame.Rect(self.collision_rect)
        self.ground_collision_rect.height = GROUND_COLLIDE_H
        self.ground_collision_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.contador = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0  # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    def move_axis_x(self, delta_x):
        self.rect.x += delta_x
        self.collision_rect.x += delta_x
        self.ground_collision_rect.x += delta_x

    def move_axis_y(self, delta_y):
        self.rect.y += delta_y
        self.collision_rect.y += delta_y
        self.ground_collision_rect.y += delta_y

    def handle_move(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0

            if not self.esta_en_plataforma(plataform_list):
                if self.move_y == 0:
                    self.is_fall = True
                    self.move_axis_y(self.gravity)
            else:
                self.is_fall = False
                self.move_axis_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.contador += 1
                else:
                    self.contador = 0

    def esta_en_plataforma(self, plataform_list):
        retorno = False

        if self.ground_collision_rect.bottom >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in plataform_list:
                if self.ground_collision_rect.colliderect(
                    plataforma.ground_collision_rect
                ):
                    retorno = True
                    break
        return retorno

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0

            self.frame += 1
            if self.frame >= len(self.animation):
                self.frame = 0

    def receive_shoot(self):
        self.lives -= 1

    def update(self, delta_ms, plataform_list):
        self.handle_move(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def draw(self, screen, offset_x):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
