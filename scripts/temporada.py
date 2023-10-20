import pygame
import random
import sys
from buscar import Buscar
from button import draw_button
from screen import Screen


class Temporada(object):

    def __init__(self, width, heigth): #esto esta medio dudoso, ya nos ocuparemos de resolver bien esto
        self.font = pygame.font.Font(None, 36)
        self.screen_width = width
        self.screen_height = heigth
        self.spacing = 50
        self.scrollable_area = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.screen = Screen().fondo()
        self.jugador = Buscar().datos_jugador
        self.money = float(self.jugador['dinero'])
        self.club = str(self.jugador['club'])
        self.name = str(self.jugador['nombre'])
        self.age = int(self.jugador['edad'])
        # self.habilidades = habilidades
        # self.propiedades = propiedades
        # self.socials = socials
        # self.objectives = objectives

    def inicio_temporada(self):
        '''Crea una termporada nueva, aleatorizando los rivales y los partidos'''
        pass
    
    def guardar(archivo='ruta_archivo_datos'):
        with open (archivo, 'wt') as f:
            # no estoy seguro de como se haria para que cambie cosas en un csv y no es importante en esta etapa
            pass
    
    def fin_temporada(self):
        '''Reinicia la temporada
        deberia llamar varias funciones para que guarde toda la data
        se me ocurre que nos conviene tener (al menos) 2 archivos de datos del jugador: uno de cosas actuales (habilidades, stamina, etc) 
            y otro de la historia (titulos, goles, clubes, etc)'''
        pass
    
    # jugadores_disponibles = [
    #     Jugador("Cristiano Ronaldo", 100000000, 90, "Tu Club", imagen_cristiano),
    #     Jugador("Lionel Messi", 95000000, 92, "Tu Club", imagen_messi),
    # ]     # no se como incluir esto, creo que estaria ligado a la funcion de busqueda de jugadores (veremos como lo implementamos)

    # 
    def crear_contrato_aleatorio(self):
        '''Función para crear contratos aleatorios'''
        club = random.choice(["Real Madrid", "FC Barcelona", "Manchester United", "Paris Saint-Germain", "Juventus"])
        bono = random.randint(50000, 100000)
        sueldo = random.randint(500000, 1000000)
        duracion = random.randint(1, 5)
        return {"club": club, "bono": bono, "sueldo": sueldo, "duracion": duracion}

    # 
    def contratos_disponibles(self):
        '''Funcion para inicializar algunos contratos disponibles'''
        jugadores_disponibles = random.choice(Buscar().obtener_jugadores)
        contratos_disponibles = []
        for _ in range(3):
            contratos_disponibles.append(self.crear_contrato_aleatorio(jugadores_disponibles[-1]))
        return contratos_disponibles

    