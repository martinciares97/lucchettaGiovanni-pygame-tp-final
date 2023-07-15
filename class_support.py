import pygame
from constantes import *

class Support:
    @staticmethod
    def getSurfaceFromSpriteSheet_v1(path,columns,rows,width,height,flip=False):
        lista = []
        surface_image = pygame.image.load(path).convert_alpha()
        fotograma_ancho = surface_image.get_width() // columns
        fotograma_alto = surface_image.get_height() // rows
        
        w_scale = width
        h_scale = height
        
        _, _, width, height = surface_image.get_rect()
        rows = SCREEN_HEIGHT // height + 1
        columns = SCREEN_WIDTH // width + 1
        
        
        
        for row in range(rows):
            for column in range(columns):
                x = column * fotograma_ancho
                y = row * fotograma_alto
                
                surface_fotograma = surface_image.subsurface(x, y, fotograma_ancho, fotograma_alto)
                surface_fotograma = pygame.transform.flip(surface_fotograma,flip,False)
                surface_fotograma = pygame.transform.scale(surface_fotograma,(25,25))
                lista.append(surface_fotograma)
        return lista

    @staticmethod
    def getSurfaceFromSpriteSheet_v2(path,columnas,filas,flip=False, step = 1,scale=1):
        lista = []
        surface_image = pygame.image.load(path)
        fotograma_ancho = int(surface_image.get_width()/columnas)
        fotograma_alto = int(surface_image.get_height()/filas)
        fotograma_ancho_scaled = int(fotograma_ancho*scale)
        fotograma_alto_scaled = int(fotograma_alto*scale)
        x = 0
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_image.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(scale != 1):
                    surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled))
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def getSurfaceCompact(path,columns,rows,width,height):
        lista = []
        surface_image = pygame.image.load(path).convert_alpha()
        fotograma_ancho = int(surface_image.get_width() / columns)
        fotograma_alto = int(surface_image.get_height() / rows)
        
        for row in range(rows):
            for column in range(columns):
                x = column * fotograma_ancho
                y = row * fotograma_alto
                surface_fotograma = surface_image.subsurface(x, y, fotograma_ancho, fotograma_alto)
                surface_fotograma = pygame.transform.scale(surface_fotograma,(width,height))
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista