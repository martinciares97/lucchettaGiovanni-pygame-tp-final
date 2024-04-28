import pygame
from os.path import join
from class_background import Background
from constantes import *

from sys import exit
from os.path import join

class Mosaico(Background):
    def __init__(self, main_surface: pygame.Surface, surface: pygame.Surface, x, y, nombre_img) -> None:
        super().__init__(main_surface, surface, x, y)
        self.image = pygame.image.load(join("assets", "Background", nombre_img))
        self.coordenadas_mosaicos = self.obtener_posiciones_mosaicos()
        
        
    def obtener_posiciones_mosaicos(self):
        coordenada_mosaicos = []
        # self.image = pygame.image.load(join("assets", "Background", nombre_img))
        _, _, w, h = self.image.get_rect() #la _ descarta el valor de x e y
        
        
        for x in range(SCREEN_WIDTH // w +1): #divido el ancho de la pantalla por el ancho de la imagen
            for y in range(SCREEN_HEIGHT // h +1): #divido el ancho de la pantalla por el ancho de la imagen
                coordenada = (x * w, y * h) # lo defino como tupla para pasarlo como parametro en el draw
                coordenada_mosaicos.append(coordenada)
                
        return coordenada_mosaicos
    
    def draw(self):
        for coordenada in self.coordenadas_mosaicos:
            self.main_surface.blit(self.surface, coordenada) #podria convertir la posicion del mosaico en una tupla
                