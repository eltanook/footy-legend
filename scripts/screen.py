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
    

    def __innit__(self, width=400, heigth=600, color_texto=(255, 255, 255), color_fondo=(0, 128, 0)):
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
        self.screen.blit(fondo_cancha)


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

# class Objetos(object):
#     def __init__(self, width, heigth):
#         # self.jugador = jugador()
#         self.screen_width = width
#         self.screen_height = heigth
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) #no se bien donde pija meter esta linea

#     def menu_mi_jugador(self):
#         jugador = self.jugador
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

#             self.screen.blit(self.fondo_cancha, (0, 0))
#             draw_button(f"Nombre: {self.nombre_jugador}", self.screen_width // 2, 150)
#             draw_button(f"Valor: ${self.valor_jugador}", self.screen_width // 2, 210)
#             draw_button(f"Habilidad: {self.habilidad_jugador}", self.screen_width // 2, 270)
#             draw_button(f"Salud: {jugador.salud}", self.screen_width // 2, 330)
#             draw_button(f"Felicidad: {jugador.felicidad}", self.screen_width // 2, 390)
#             draw_button(f"Edad: {jugador.edad}", self.screen_width // 2, 450)
#             draw_button(f"Club: {jugador.club}", self.screen_width // 2, 510)
#             self.screen.blit(jugador.imagen, (self.screen_width // 2 - 60, 0))
#             volver_button = draw_button("Volver al Menú", self.screen_width // 2, 570)
#             pygame.display.flip()

#             for event in pygame.event.get():
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     x, y = pygame.mouse.get_pos()
#                     if volver_button.collidepoint(x, y):
#                         break
    
#     # def menu_mercado_pases():
#     #     mercado_de_traspaso(jugadores_disponibles[-1])
    
#     # def menu_estilo_de_vida():
#     #     gestionar_estilo_de_vida(jugadores_disponibles[-1])
    
#     # def menu_entrenamiento():
#     #     entrenamiento(jugadores_disponibles[-1])
    
#     # def menu_personalizar_personaje():
    #     personalizar_personaje(jugadores_disponibles[-1])