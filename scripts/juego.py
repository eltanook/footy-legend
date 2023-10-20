import pygame
import sys
from buscar import Buscar
from button import Buttons
from screen import Screen
from game_logic import Objetos

class Game():
    def __init__(self, width, heigth):
        self.jugador = Buscar().datos_jugador()
        self.screen_width = width
        self.screen_height = heigth
        self.scrollable_area = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) #no se bien donde pija meter esta linea
        self.screen = Screen().fondo()
        self.jugador = Buscar().datos_jugador()
        self.money = float(self.jugador['dinero'])
        self.club = str(self.jugador['club'])
        self.name = str(self.jugador['nombre'])
        self.age = int(self.jugador['edad'])
        self.media = Buscar().media_jugador()
        self.felicidad = int(self.jugador['felicidad'])
        self.stamina = int(self.jugador['stamina'])
        self.value = int(self.jugador['valor'])
        self.spacing = 50


    def main(self): 
        ''' copie y pegue todo y lo meti en una funcion, tal vez habria que usar self para que sea mas consistente
        hay que llamar las funciones para que ande todo bien'''
        self.jugador = Buscar().datos_jugador
        clock = pygame.time.Clock()
        running = True
        scroll_y = 0
        # jugador_image = jugadores_disponibles[-1].imagen
        jugador_habilidad = self.jugador['media']
        while running:
            clock.tick(60) # hace que corra a 60fps para consistencia
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen
            # Screen().fondo()        #esto no estoy seguro de que funcione
            # self.screen.blit(fondo_cancha, (0, 0))

            if not nombre_jugador:
                nombre_jugador = Buscar().obtener_nombre()

            if nombre_jugador:
                menu_buttons = [
                    ("Mi Jugador", self.screen_width // 2, 180),
                    ("Ofertas de Traspaso", self.screen_width // 2, 240),
                    ("Estilo de Vida", self.screen_width // 2, 300),
                    ("Entrenamiento", self.screen_width // 2, 360),
                    ("Simular Partido", self.screen_width // 2, 420),
                    ("Salir", self.screen_width // 2, 480)
                ]

                y = 400
                for button_text, x_button, y_button in menu_buttons:
                    Buttons().draw_button(button_text, x_button, y_button + scroll_y)
                    y += self.spacing

                # Dibuja la imagen del jugador y su nivel de habilidad
                # self.screen.blit(jugador_image, (20, 10))
                Buttons().draw_button(f"{nombre_jugador}|{jugador_habilidad}|${self.money}", 250, 70)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if nombre_jugador:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        for button_text, x_button, y_button in menu_buttons:
                            button = pygame.Rect(x_button - 100, y_button - 25 + scroll_y, 200, 50)
                            if button.collidepoint(x, y):
                                if button_text == "Mi Jugador":
                                    jugador = self.jugador
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()

                                        Objetos().menu_mi_jugador()
                                        # screen.blit(fondo_cancha, (0, 0))
                                        # draw_button(f"Nombre: {nombre_jugador}", self.screen_width // 2, 150)
                                        # draw_button(f"Valor: ${valor_jugador}", screen_width // 2, 210)
                                        # draw_button(f"Habilidad: {habilidad_jugador}", screen_width // 2, 270)
                                        # draw_button(f"Salud: {jugador.salud}", screen_width // 2, 330)
                                        # draw_button(f"Felicidad: {jugador.felicidad}", screen_width // 2, 390)
                                        # draw_button(f"Edad: {jugador.edad}", screen_width // 2, 450)
                                        # draw_button(f"Club: {jugador.club}", screen_width // 2, 510)
                                        # screen.blit(jugador.imagen, (screen_width // 2 - 60, 0))
                                        volver_button = Buttons().draw_button("Volver al Menú", self.screen_width // 2, 570)
                                        # pygame.display.flip()

                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                x, y = pygame.mouse.get_pos()
                                                if volver_button.collidepoint(x, y):
                                                    break
                                elif button_text == "Ofertas de Traspaso":
                                    Objetos().mercado_de_traspaso() #nota: tenian jugadores_disponibles[-1] aca
                                elif button_text == "Estilo de Vida":
                                    Objetos().gestionar_estilo_de_vida() #nota: tenian jugadores_disponibles[-1] aca
                                elif button_text == "Entrenamiento":
                                    Objetos().entrenamiento() #nota: tenian jugadores_disponibles[-1] aca  ---> Objetos().entrenamiento() es un pass !!!
                                elif button_text == "Simular Partido":
                                    Objetos().simular_partido_en_tiempo_real() #nota: tenian jugadores_disponibles[-1] aca
                        if self.scrollable_area.collidepoint(x, y):
                            pass
                        else:
                            scroll_up_button = pygame.Rect(self.screen_width - 30, 0, 30, 30)
                            scroll_down_button = pygame.Rect(self.screen_width - 30, self.screen_height - 30, 30, 30)
                            if scroll_up_button.collidepoint(x, y):
                                scroll_y += 30
                            elif scroll_down_button.collidepoint(x, y):
                                scroll_y -= 30

        # Cerrar Pygame
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    Game(width=400, heigth=600).main()