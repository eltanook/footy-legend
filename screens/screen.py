import pygame
from data.jugadores import jugadores_disponibles
from utils.button import draw_button
from game.game_logic import simular_partido_en_tiempo_real
import sys

# Definición de colores
color_fondo = (0, 128, 0)
color_texto = (255, 255, 255)

# Función para la pantalla principal (main menu)
def main_menu(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(color_fondo)

        # Tu código para la pantalla principal aquí
        # ...

# Otras funciones para gestionar las pantallas de actividades como mercado de traspaso, estilo de vida, etc.
