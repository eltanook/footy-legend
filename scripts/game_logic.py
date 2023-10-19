import pygame
import random
import time
from data.jugadores import Jugador
from button import draw_button
import sys

'''
Funciones que tendrian que estar aca: 
 - simualcion de partidos
 - cambio de club
 - compra de articulos (estilo de vida)
 - ...
'''
# Función para simular un partido en tiempo real
def simular_partido_en_tiempo_real(screen, jugador):
    color_fondo = (0, 128, 0)
    color_texto = (255, 255, 255)
    
    tiempo_inicial = time.time()
    tiempo_transcurrido = 0
    
    while tiempo_transcurrido < 20:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(color_fondo)

        tiempo_transcurrido = time.time() - tiempo_inicial

        if tiempo_transcurrido >= 1:
            evento = random.choice(["Gol", "Tarjeta Amarilla", "Tarjeta Roja", "Cambio"])
            draw_button(screen, f"Evento: {evento}", 200, 300)
        if tiempo_transcurrido >= 5:
            goles_jugador = random.randint(0, 3)
            draw_button(screen, f"Goles: {goles_jugador}", 200, 400)

        tiempo_transcurrido = round(tiempo_transcurrido, 2)
        draw_button(screen, f"Tiempo: {tiempo_transcurrido}s", 200, 500)
        pygame.display.flip()

    resultado = random.choice(["Victoria", "Empate", "Derrota"])
    goles_jugador = random.randint(0, 3)
    calificacion_final = round(1 + (random.random() * 9), 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(color_fondo)

        draw_button(screen, "Tu Club", 200, 100)
        draw_button(screen, "VS", 200, 200)
        club_rival = random.choice(["Club A", "Club B", "Club C"])
        draw_button(screen, club_rival, 200, 300)

        draw_button(screen, f"Resultado: {resultado}", 200, 400)
        draw_button(screen, f"Goles: {goles_jugador}", 200, 450)
        draw_button(screen, f"Minutos: 90", 200, 500)
        draw_button(screen, f"Calificación: {calificacion_final:.1f}", 200, 550)

        simular_otro_partido_button = draw_button(screen, "Simular otro partido", 200, 600)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if simular_otro_partido_button.collidepoint(x, y):
                    return
def cambio_club(self):
    pass
def compra_articulos(self):
    pass
# Otras funciones para la lógica del juego
