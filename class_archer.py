import pygame
from debug_mod import get_mode
from support import Support
from constantes import *
from auxiliar import Auxiliar


class Archer:
    def __init__(
        self,
        sprites,
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
        """
        self.run_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/run.png",15,1,scale=p_scale)[:12]
        """
        self.sprite_sheets = sprites

        self.frame = 0
        self.state = "idle"
        self.direction = "right"
        self.key = "{0}_{1}".format(self.state, self.direction)

        self.idle_r = self.sprite_sheets["idle_right"]
        self.idle_l = self.sprite_sheets["idle_left"]
        self.jump_r = self.sprite_sheets["jump_right"]
        self.jump_l = self.sprite_sheets["jump_left"]
        self.run_r = self.sprite_sheets["run_right"]
        self.run_l = self.sprite_sheets["run_left"]
        self.shoot_r = self.sprite_sheets["light_atk_right"]
        self.shoot_l = self.sprite_sheets["light_atk_left"]
        self.light_atk_r = self.sprite_sheets["light_atk_right"]
        self.light_atk_l = self.sprite_sheets["light_atk_left"]

        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_run = speed_run
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power

        self.animation = self.idle_r

        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collision_rect = pygame.Rect(
            self.rect.left + 32, self.rect.bottom - 64, 64, 64
        )
        self.ground_collision_rect = pygame.Rect(self.collision_rect)
        self.ground_collision_rect.height = GROUND_COLLIDE_H
        self.ground_collision_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_attack = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0  # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump

    def run(self, direction):
        if self.is_jump == False and self.is_fall == False:
            if self.direction != direction or (
                self.animation != self.run_r and self.animation != self.run_l
            ):
                self.frame = 0
                self.direction = direction
                if direction == DIRECTION_R:
                    self.move_x = self.speed_run
                    self.animation = self.run_r
                else:
                    self.move_x = -self.speed_run
                    self.animation = self.run_l

    def shoot(self, on_off=True):
        self.is_shoot = on_off
        if on_off == True and self.is_jump == False and self.is_fall == False:
            if self.animation != self.shoot_r and self.animation != self.shoot_l:
                self.frame = 0
                self.is_shoot = True
                if self.direction == DIRECTION_R:
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l

    def receive_shoot(self):
        self.lives -= 1

    def attack(self, on_off=True):
        self.is_attack = on_off
        if on_off == True and self.is_jump == False and self.is_fall == False:
            if (
                self.animation != self.light_atk_r
                and self.animation != self.light_atk_l
            ):
                self.frame = 0
                if self.direction == DIRECTION_R:
                    self.animation = self.light_atk_r
                else:
                    self.animation = self.light_atk_l

    def jump(self, on_off=True):
        if on_off and self.is_jump == False and self.is_fall == False:
            self.y_start_jump = self.rect.y
            if self.direction == DIRECTION_R:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if on_off == False:
            self.is_jump = False
            self.idle()

    def idle(self):
        if self.is_attack or self.is_shoot:
            return

        if self.animation != self.idle_r and self.animation != self.idle_l:
            if self.direction == DIRECTION_R:
                self.animation = self.idle_r
            else:
                self.animation = self.idle_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self, delta_x):
        self.rect.x += delta_x
        self.collision_rect.x += delta_x
        self.ground_collision_rect.x += delta_x

    def change_y(self, delta_y):
        self.rect.y += delta_y
        self.collision_rect.y += delta_y
        self.ground_collision_rect.y += delta_y

    def handle_move(self, delta_ms, plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0

            if abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump:
                self.move_y = 0

            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if not self.esta_en_plataforma(plataform_list):
                if self.move_y == 0:
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if self.is_jump:
                    self.jump(False)
                self.is_fall = False

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

    def colision_enemigo():
        pass

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    def update(self, delta_ms, plataform_list):
        self.handle_move(delta_ms, plataform_list)
        self.do_animation(delta_ms)

    def events(self, delta_ms, keys):
        self.tiempo_transcurrido += delta_ms

        if (
            keys[pygame.K_LEFT]
            and not keys[pygame.K_RIGHT]
            and not keys[pygame.K_a]
            and not keys[pygame.K_s]
        ):
            self.run(DIRECTION_L)
        if (
            keys[pygame.K_RIGHT]
            and not keys[
                pygame.K_LEFT and not keys[pygame.K_a] and not keys[pygame.K_s]
            ]
        ):
            self.run(DIRECTION_R)

        if (
            not keys[pygame.K_LEFT]
            and not keys[pygame.K_RIGHT]
            and not keys[pygame.K_SPACE]
        ):
            self.idle()
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]:
            self.idle()

        if keys[pygame.K_SPACE]:
            if (
                self.tiempo_transcurrido - self.tiempo_last_jump
            ) > self.interval_time_jump:
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if not keys[pygame.K_a]:
            self.shoot(False)

        if not keys[pygame.K_a]:
            self.attack(False)

        if (
            keys[pygame.K_s]
            and not keys[pygame.K_a]
            and not keys[pygame.K_RIGHT]
            and not keys[pygame.K_LEFT]
        ):
            self.shoot()

        if (
            keys[pygame.K_a]
            and not keys[pygame.K_s]
            and not keys[pygame.K_RIGHT]
            and not keys[pygame.K_LEFT]
        ):
            self.attack()

    def draw(self, screen):
        if get_mode():
            pygame.draw.rect(screen, color=RED, rect=self.collision_rect, width=3)
            pygame.draw.rect(
                screen, color=RED, rect=self.ground_collision_rect, width=3
            )
            pygame.draw.rect(screen, color=RED, rect=self.rect, width=3)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
