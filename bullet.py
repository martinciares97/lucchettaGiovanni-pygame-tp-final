from player import *
from constantes import *
from auxiliar import Auxiliar
import math
from class_support import Support


class Bullet:
    def __init__(
        self,
        owner,
        x_init,
        y_init,
        x_end,
        y_end,
        speed,
        path,
        frame_rate_ms,
        move_rate_ms,
        width=5,
        height=5,
        flip_x=False,
    ) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0

        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.transform.flip(self.image, flip_x=flip_x, flip_y=False)
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(
            y_end - y_init, x_end - x_init
        )  # Obtengo el angulo en radianes
        print("El angulo engrados es:", int(angle * 180 / math.pi))

        self.move_x = math.cos(angle) * speed
        self.move_y = math.sin(angle) * speed

        self.frame = 0

        self.is_active = True

        self.collition_rect = pygame.Rect(
            self.rect.centerx - 25,
            self.rect.centery - 25,
            50,
            50,
        )

    def change_x(self, delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)
        self.collition_rect.x = int(self.x) + self.rect.width / 2 - 25

    def change_y(self, delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)
        self.collition_rect.y = int(self.y) + self.rect.height / 2 - 25

    def do_movement(self, delta_ms, plataform_list, enemy_list, player):
        self.tiempo_transcurrido_move += delta_ms
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(plataform_list, enemy_list, player)

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            pass

    def check_impact(self, plataform_list, enemy_list, player):
        if (
            self.is_active
            and self.owner != player
            and self.collition_rect.colliderect(player.collition_rect)
        ):
            print("IMPACTO PLAYER")
            player.receive_shoot()
            self.is_active = False
        contador = 0
        for enemy in enemy_list:
            if (
                self.is_active
                and self.owner != enemy
                and self.collition_rect.colliderect(enemy.collition_rect)
            ):
                print("IMPACTO ENEMY")
                enemy_list.pop(contador)
                # self.score += 100
                self.is_active = False
            contador += 1

    def update(self, delta_ms, plataform_list, enemy_list, player):
        self.do_movement(delta_ms, plataform_list, enemy_list, player)
        self.do_animation(delta_ms)

    def draw(self, screen):
        if self.is_active:
            screen.blit(self.image, self.rect)
