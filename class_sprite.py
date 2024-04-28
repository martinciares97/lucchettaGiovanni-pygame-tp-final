import pygame
from pygame.sprite import _Group


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color) -> None:
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect(x=x, y=y, w=w, h=h)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
