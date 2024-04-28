import pygame

from class_background import Background

class Nivel:
    def __init__(self, pantalla_bliteo: pygame.Surface, surface:pygame.Surface, x, y, w, h) -> None:
        self.pantalla_bliteo = pantalla_bliteo
        self.rect = surface.get_rect(x=x, y=y, w=w, h=h)
        
        self.background = Background(x, y, w, h, "assets\Background\The Dawn\Reference-Image.png")
        
        
    def update(self):
        pass
    
    def draw(self):
        self.background.draw(self.pantalla_bliteo)
    
