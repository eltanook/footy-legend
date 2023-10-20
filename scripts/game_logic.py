import pygame
import random
import time
from button import Buttons
import sys
from buscar import Buscar
from screen import Screen

'''
Funciones que tendrian que estar aca: 
 - simualcion de partidos
 - cambio de club
 - compra de articulos (estilo de vida)
 - ...
'''
# Función para simular un partido en tiempo real
class Objetos(object):
    def __init__(self, width, heigth):
        self.jugador = Buscar().datos_jugador()
        self.screen_width = width
        self.screen_height = heigth
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

    def menu_mi_jugador(self):
        jugador = self.jugador
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            Screen().fondo()
            #screen.blit(self.fondo_cancha, (0, 0))

            Buttons().draw_button(f"Nombre: {self.name}", self.screen_width // 2, 150)
            Buttons().draw_button(f"Valor: ${self.value}", self.screen_width // 2, 210)
            Buttons().draw_button(f"Habilidad: {self.media}", self.screen_width // 2, 270)
            Buttons().draw_button(f"Salud: {self.stamina}", self.screen_width // 2, 330)
            Buttons().draw_button(f"Felicidad: {self.felicidad}", self.screen_width // 2, 390)
            Buttons().draw_button(f"Edad: {self.age}", self.screen_width // 2, 450)
            Buttons().draw_button(f"Club: {self.club}", self.screen_width // 2, 510)
            self.screen.blit(jugador.imagen, (self.screen_width // 2 - 60, 0))
            volver_button = Buttons().draw_button("Volver al Menú", self.screen_width // 2, 570)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if volver_button.collidepoint(x, y):
                        break   
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
                Buttons().draw_button(screen, f"Evento: {evento}", 200, 300)
            if tiempo_transcurrido >= 5:
                goles_jugador = random.randint(0, 3)
                Buttons().draw_button(screen, f"Goles: {goles_jugador}", 200, 400)

            tiempo_transcurrido = round(tiempo_transcurrido, 2)
            Buttons().draw_button(screen, f"Tiempo: {tiempo_transcurrido}s", 200, 500)
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

            Buttons().draw_button(screen, "Tu Club", 200, 100)
            Buttons().draw_button(screen, "VS", 200, 200)
            club_rival = random.choice(["Club A", "Club B", "Club C"])
            Buttons().draw_button(screen, club_rival, 200, 300)

            Buttons().draw_button(screen, f"Resultado: {resultado}", 200, 400)
            Buttons().draw_button(screen, f"Goles: {goles_jugador}", 200, 450)
            Buttons().draw_button(screen, f"Minutos: 90", 200, 500)
            Buttons().draw_button(screen, f"Calificación: {calificacion_final:.1f}", 200, 550)

            simular_otro_partido_button = Buttons().draw_button(screen, "Simular otro partido", 200, 600)

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
    
    def entrenamiento():
        pass

    def gestionar_estilo_de_vida(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            Screen().fondo()
            # screen.blit(fondo_cancha, (0, 0))

            ejercicio_button = Buttons().draw_button("Hacer ejercicio", self.screen_width // 2, 250)
            relajarse_button = Buttons().draw_button("Relajarse", self.screen_width // 2, 350)
            volver_button = Buttons().draw_button("Volver al Menú", self.screen_width // 2, 450)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if ejercicio_button.collidepoint(x, y):
                        self.stamina += 10
                        self.felicidad -= 5
                    elif relajarse_button.collidepoint(x, y):
                        self.stamina -= 5
                        self.felicidad += 10
                    elif volver_button.collidepoint(x, y):
                        return

    def personalizar_personaje(self):
        # Rutas de las carpetas de opciones para personalizar el personaje
        skin_options = [f"cara/pieles/piel{i}.png" for i in range(1, 2)]
        nose_options = [f"cara/narices/nariz{i}.png" for i in range(1, 8)]  #esto hay que sacarlo y ponerlo en algun self o algo asi
        mouth_options = [f"cara/bocas/boca{i}.png" for i in range(1, 4)]
        eye_options = [f"cara/ojos/ojos{i}.png" for i in range(1, 9)]
        hair_options = [f"cara/pelos/pelo{i}.png" for i in range(1, 9)]

        # Diccionario para rastrear las opciones seleccionadas
        selected_options = {        #esto hay que sacarlo y ponerlo en algun self o algo asi
            "skin": 1,
            "nose": 1,
            "mouth": 1,
            "eye": 1,
            "hair": 1
        }

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            Screen().fondo()
            # screen.blit(fondo_cancha, (0, 0))
            part_images = []
            y = 50
            for part_name, options in [("skin", skin_options), ("nose", nose_options), ("mouth", mouth_options), ("eye", eye_options), ("hair", hair_options)]:
                selected_part = selected_options[part_name]
                part_images.append(pygame.image.load(options[selected_part - 1]))

                y += 150

            part_image_skin = pygame.transform.scale(part_images[0], (150, 150))
            self.screen.blit(part_image_skin, (125, 50))

            part_image_nose = pygame.transform.scale(part_images[1], (30, 30))
            self.screen.blit(part_image_nose, (185, 115))

            part_image_mouth = pygame.transform.scale(part_images[2], (35, 35))
            self.screen.blit(part_image_mouth, (185, 125))

            part_image_eye = pygame.transform.scale(part_images[3], (60, 60))
            self.screen.blit(part_image_eye, (170, 85))

            part_image_hair = pygame.transform.scale(part_images[4], (90, 90))
            self.screen.blit(part_image_hair, (155, 50))

            pygame.display.flip()
    
    def mercado_de_traspaso(self):
        ''' hay que incluir la funcion que busca los jugadores relevantes para que cambie la lista si es que el jugador cambia de liga'''
        dinero = self.money
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            # Screen().fondo()
            # self.screen.blit(self.fondo_cancha, (0, 0))

            y = 50
            for i, contrato in enumerate(self.contratos_disponibles):
                if y > self.scrollable_area.height:
                    break

                texto_contrato = f"Club: {contrato['club']}\nBono por Gol: ${contrato['bono']}\nSueldo: ${contrato['sueldo']}\nDuración: {contrato['duracion']} años"
                lineas = texto_contrato.split('\n')  # Divide el texto en líneas

                # Renderiza el texto en líneas
                y_temp = y
                for linea in lineas:
                    texto_renderizado = self.font.render(linea, True, self.color_texto)
                    self.screen.blit(texto_renderizado, (10, y_temp))
                    y_temp += self.font.get_height()

                button = Buttons().draw_button("Firmar contrato", self.screen_width // 2, y_temp + self.spacing)
                y = y_temp + self.spacing + button.height

                if button.collidepoint(0, y_temp + self.spacing):       # cambie x por 0
                    if dinero >= contrato['sueldo']:
                        dinero -= contrato['sueldo']
                        self.club = contrato['club']
                        contrato['club'] = "Tu Club"
                        self.contratos_disponibles.remove(contrato)
                        self.contratos_disponibles.append(self.crear_contrato_aleatorio(self.jugador))


            volver_button = Buttons().draw_button("Volver al Menú", self.screen_width // 2, 550)
            dinero_button = Buttons().draw_button(f"Dinero: ${dinero}", self.screen_width // 2, 30)  # por que no usa esto?

            pygame.display.flip()
