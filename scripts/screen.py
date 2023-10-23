import pygame
from button import Buttons
import sys

# Definición de colores
# color_fondo = (0, 128, 0)
# color_texto = (255, 255, 255)

class Screen(object):
    '''Diria que aca solo tendria que llamar funciones de Game aunque no estoy de todo seguro de eso
    esta parte es la que menos ideas tengo de como hacer para que quede bien bien'''

    pygame.display.set_caption("Footy legend")
    

    def __init__(self, width=400, heigth=600, color_texto=(255, 255, 255), color_fondo=(0, 128, 0)):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.color_fondo = color_fondo
        self.color_texto = color_texto
        self.screen_width = width
        self.screen_height = heigth
        self.scroll_y = 0
        self.spacing = 50
        self.scrollable_area = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) #no se bien donde pija meter esta linea

    def fondo(self):
        fondo_cancha = pygame.image.load("fondo.png")
        fondo_cancha = pygame.transform.scale(fondo_cancha, (self.screen_width, self.screen_height))
        self.screen.fill(self.color_fondo)
        self.screen.blit(fondo_cancha, dest=(0, 0))


    def main_menu(self):
        # no se que tan actualizado este esto pero lo dejo igual
        if not self.nombre:
            pass
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.color_fondo)
            menu_buttons = [
            ("Mi Jugador", self.screen_width // 2, 180),
            ("Ofertas de Traspaso", self.screen_width // 2, 240),
            ("Estilo de Vida", self.screen_width // 2, 300),
            ("Entrenamiento", self.screen_width // 2, 360),
            ("Simular Partido", self.screen_width // 2, 420),
            ("Personalizar Personaje", self.screen_width // 2, 480),  # Nueva opción
            ("Salir", self.screen_width // 2, 540),
            ]

            y = 400
            for button_text, x_button, y_button in menu_buttons:
                Buttons().draw_button(button_text, x_button, y_button + self.scroll_y)
                y += self.spacing

            # Tu código para la pantalla principal aquí
            # ...

    # Otras funciones para gestionar las pantallas de actividades como mercado de traspaso, estilo de vida, etc.

