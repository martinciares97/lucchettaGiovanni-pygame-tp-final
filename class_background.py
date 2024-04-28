import pygame
from pygame.locals import *
from constantes import *
from auxiliar import Auxiliar
from os import listdir
from os.path import join, isfile

from object import Block


class Background:
    def __init__(self, x=0, y=0, w=None, h=None, path=None):
        if path is not None:
            self.image = pygame.image.load(path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (w, h))
        else:
            self.image = pygame.Surface((w, h), pygame.SRCALPHA)
            
        self.rect = self.image.get_rect(x=x, y=y, w=w, h=h)
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
