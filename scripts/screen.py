import pygame
# from data.jugadores import jugadores_disponibles
from button import draw_button
from game_logic import simular_partido_en_tiempo_real
import sys

# Definición de colores
# color_fondo = (0, 128, 0)
# color_texto = (255, 255, 255)

class Menus(object):
    '''Diria que aca solo tendria que llamar funciones de Game aunque no estoy de todo seguro de eso
    esta parte es la que menos ideas tengo de como hacer para que quede bien bien'''

    pygame.display.set_caption("Footy legend")
    

    def __innit__(self, width, heigth):
        self.font = pygame.font.Font(None, 36)
        self.color_fondo = (0, 128, 0)
        self.color_texto = (255, 255, 255)
        self.screen_width = width
        self.screen_height = heigth
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) #no se bien donde pija meter esta linea

    def fondo(self):
        fondo_cancha = pygame.image.load("fondo.png")
        fondo_cancha = pygame.transform.scale(fondo_cancha, (self.screen_width, self.screen_height))
        self.screen.fill(self.color_fondo)
        self.screen.blit(fondo_cancha)


    def main_menu(screen, self):
        # no se que tan actualizado este esto pero lo dejo igual
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(self.color_fondo)

            # Tu código para la pantalla principal aquí
            # ...

    # Otras funciones para gestionar las pantallas de actividades como mercado de traspaso, estilo de vida, etc.