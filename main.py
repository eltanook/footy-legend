import pygame
from screens.screen import main_menu

# Configuración de Pygame
pygame.init()

# Configuración de la pantalla
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Football Legend")

if __name__ == "__main__":
    main_menu(screen)
