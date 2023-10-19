import pygame
import sys
import random
import time

pygame.init()

# Configuración de la pantalla
screen_width, screen_height = 400, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Footy legend")

# Cargar imagen de fondo de la cancha de fútbol
fondo_cancha = pygame.image.load("fondo.png")
fondo_cancha = pygame.transform.scale(fondo_cancha, (screen_width, screen_height))

# Definir la fuente
font = pygame.font.Font(None, 36)

# Cargar imágenes de los jugadores
imagen_cristiano = pygame.image.load("cristiano.png")
imagen_messi = pygame.image.load("messi.png")
imagen_cristiano = pygame.transform.scale(imagen_cristiano, (120, 120))
imagen_messi = pygame.transform.scale(imagen_messi, (120, 120))

# Configuración de colores
color_fondo = (255, 255, 255)
color_texto = (0, 0, 0)

# Separación vertical entre botones
spacing = 50

# Definir el área de desplazamiento
scrollable_area = pygame.Rect(0, 0, screen_width, screen_height)

# Función para dibujar botones con un fondo deportivo
def draw_button(text, x, y, width=250, height=50):
    button = pygame.Rect(x - width / 2, y - height / 2, width, height)
    pygame.draw.rect(screen, color_fondo, button)
    pygame.draw.rect(screen, color_texto, button, 2)
    button_text = font.render(text, True, color_texto)
    text_rect = button_text.get_rect()
    text_rect.center = (x, y)
    screen.blit(button_text, text_rect)
    return button

class Jugador:
    def __init__(self, nombre, valor, habilidad, club, imagen):
        self.nombre = nombre
        self.valor = valor
        self.habilidad = habilidad
        self.salud = 100
        self.felicidad = 100
        self.edad = 16
        self.club = club
        self.imagen = imagen

nombre_jugador = ""
valor_jugador = 0
habilidad_jugador = 0
dinero = 1000

jugadores_disponibles = [
    Jugador("Cristiano Ronaldo", 100000000, 90, "Tu Club", imagen_cristiano),
    Jugador("Lionel Messi", 95000000, 92, "Tu Club", imagen_messi),
]

# Lista de contratos disponibles
contratos_disponibles = []

# Función para crear contratos aleatorios
def crear_contrato_aleatorio(jugador):
    club = random.choice(["Real Madrid", "FC Barcelona", "Manchester United", "Paris Saint-Germain", "Juventus"])
    bono = random.randint(50000, 100000)
    sueldo = random.randint(500000, 1000000)
    duracion = random.randint(1, 5)
    return {"club": club, "bono": bono, "sueldo": sueldo, "duracion": duracion}

# Inicializar algunos contratos disponibles
for _ in range(3):
    contratos_disponibles.append(crear_contrato_aleatorio(jugadores_disponibles[-1]))

# Función para la ventana de mercado de traspaso
def mercado_de_traspaso(jugador):
    global dinero
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        y = 50
        for i, contrato in enumerate(contratos_disponibles):
            if y > scrollable_area.height:
                break

            texto_contrato = f"Club: {contrato['club']}\nBono por Gol: ${contrato['bono']}\nSueldo: ${contrato['sueldo']}\nDuración: {contrato['duracion']} años"
            lineas = texto_contrato.split('\n')  # Divide el texto en líneas

            # Renderiza el texto en líneas
            y_temp = y
            for linea in lineas:
                texto_renderizado = font.render(linea, True, color_texto)
                screen.blit(texto_renderizado, (10, y_temp))
                y_temp += font.get_height()

            button = draw_button("Firmar contrato", screen_width // 2, y_temp + spacing)
            y = y_temp + spacing + button.height

            if button.collidepoint(x, y_temp + spacing):
                if dinero >= contrato['sueldo']:
                    dinero -= contrato['sueldo']
                    jugador.club = contrato['club']
                    contrato['club'] = "Tu Club"
                    contratos_disponibles.remove(contrato)
                    contratos_disponibles.append(crear_contrato_aleatorio(jugador))


        volver_button = draw_button("Volver al Menú", screen_width // 2, 550)
        dinero_button = draw_button(f"Dinero: ${dinero}", screen_width // 2, 30)

        pygame.display.flip()

# Función para obtener el nombre del jugador
def obtener_nombre():
    nombre = ""
    input_box = pygame.Rect(100, 250, 200, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False

    nombre_ingresado = False

    while not nombre_ingresado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        nombre_ingresado = True
                    elif event.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        nombre += event.unicode

        screen.blit(fondo_cancha, (0, 0))

        txt_surface = font.render(nombre, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

    return nombre

# Función para gestionar el estilo de vida
def gestionar_estilo_de_vida(jugador):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        ejercicio_button = draw_button("Hacer ejercicio", screen_width // 2, 250)
        relajarse_button = draw_button("Relajarse", screen_width // 2, 350)
        volver_button = draw_button("Volver al Menú", screen_width // 2, 450)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if ejercicio_button.collidepoint(x, y):
                    jugador.salud += 10
                    jugador.felicidad -= 5
                elif relajarse_button.collidepoint(x, y):
                    jugador.salud -= 5
                    jugador.felicidad += 10
                elif volver_button.collidepoint(x, y):
                    return

# Función para simular un partido en tiempo real
def simular_partido_en_tiempo_real(jugador):
    tiempo_inicial = time.time()
    tiempo_transcurrido = 0

    while tiempo_transcurrido < 20:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        tiempo_transcurrido = time.time() - tiempo_inicial

        if tiempo_transcurrido >= 1:
            evento = random.choice(["Gol", "Tarjeta Amarilla", "Tarjeta Roja", "Cambio"])
            draw_button(f"Evento: {evento}", 200, 300)
        if tiempo_transcurrido >= 5:
            goles_jugador = random.randint(0, 3)
            draw_button(f"Goles: {goles_jugador}", 200, 400)

        tiempo_transcurrido = round(tiempo_transcurrido, 2)
        draw_button(f"Tiempo: {tiempo_transcurrido}s", 200, 500)
        pygame.display.flip()

    resultado = random.choice(["Victoria", "Empate", "Derrota"])
    goles_jugador = random.randint(0, 3)
    calificacion_final = round(1 + (random.random() * 9), 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        draw_button("Tu Club", 200, 100)
        draw_button("VS", 200, 200)
        club_rival = random.choice(["Club A", "Club B", "Club C"])
        draw_button(club_rival, 200, 300)

        draw_button(f"Resultado: {resultado}", 200, 400)
        draw_button(f"Goles: {goles_jugador}", 200, 450)
        draw_button(f"Minutos: 90", 200, 500)
        draw_button(f"Calificación: {calificacion_final:.1f}", 200, 550)

        simular_otro_partido_button = draw_button("Simular otro partido", 200, 600)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if simular_otro_partido_button.collidepoint(x, y):
                    return

# Función para personalizar el personaje
def personalizar_personaje():
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

        screen.blit(fondo_cancha, (0, 0))
        part_images = []
        y = 50
        for part_name, options in [("skin", skin_options), ("nose", nose_options), ("mouth", mouth_options), ("eye", eye_options), ("hair", hair_options)]:
            selected_part = selected_options[part_name]
            part_images.append(pygame.image.load(options[selected_part - 1]))

            y += 150

        part_image_skin = pygame.transform.scale(part_images[0], (150, 150))
        screen.blit(part_image_skin, (125, 50))

        part_image_nose = pygame.transform.scale(part_images[1], (30, 30))
        screen.blit(part_image_nose, (185, 115))

        part_image_mouth = pygame.transform.scale(part_images[2], (35, 35))
        screen.blit(part_image_mouth, (185, 125))

        part_image_eye = pygame.transform.scale(part_images[3], (60, 60))
        screen.blit(part_image_eye, (170, 85))

        part_image_hair = pygame.transform.scale(part_images[4], (90, 90))
        screen.blit(part_image_hair, (155, 50))

        pygame.display.flip()

def botones_personalizacion_personaje(parte_cuerpo, selected_option=0): #nombre placeholder
    ''' hace los botones de las opciones de personalizacion del personaje y cambia cuando toca el jugador
    hay que revisar que esto funcione porque no estoy del todo seguro, siento que puede tirar algun error
    :param parte_cuerpo: parte del cuerpo que se quiere cambiar (str)
    :param selected_option: posicion de la opcion seleccionada de la parte del cuerpo a cambiar (int)
    :return : nueva posicion de la parte del cuerpo'''
    part_images = {'skin' : [f"cara/pieles/piel{i}.png" for i in range(1, 2)],
                'nose' : [f"cara/narices/nariz{i}.png" for i in range(1, 8)],  #esto hay que sacarlo y ponerlo en algun self o algo asi
                'mouth' : [f"cara/bocas/boca{i}.png" for i in range(1, 4)],       # SI O SI LO DE ARRIBA xq labura al pedo sino
                'eye' : [f"cara/ojos/ojos{i}.png" for i in range(1, 9)],
                'hair' : [f"cara/pelos/pelo{i}.png" for i in range(1, 9)]}      #esta distinto que en la otra funcion xq es mas facil que ande asi aca
    if parte_cuerpo in part_images:
        opciones = part_images['parte_cuerpo']
        botones = [draw_button(f'{parte_cuerpo.capitalise()} {i+1}', screen_width//2, 250 + i*spacing, 100) for i in opciones]
    for i,boton in enumerate(botones):
        if boton.collidepoint(x, 250 + i*spacing):
            selected_option[parte_cuerpo] = i+1
    return selected_option


# Bucle principal
running = True
scroll_y = 0
jugador_image = jugadores_disponibles[-1].imagen
jugador_habilidad = jugadores_disponibles[-1].habilidad
x = 0  # Definir x para evitar errores

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fondo_cancha, (0, 0))

    if not nombre_jugador:
        nombre_jugador = obtener_nombre()

    if nombre_jugador:
        menu_buttons = [
            ("Mi Jugador", screen_width // 2, 180),
            ("Ofertas de Traspaso", screen_width // 2, 240),
            ("Estilo de Vida", screen_width // 2, 300),
            ("Entrenamiento", screen_width // 2, 360),
            ("Simular Partido", screen_width // 2, 420),
            ("Personalizar Personaje", screen_width // 2, 480),  # Nueva opción
            ("Salir", screen_width // 2, 540),
        ]

        y = 400
        for button_text, x_button, y_button in menu_buttons:
            draw_button(button_text, x_button, y_button + scroll_y)
            y += spacing

        # Dibuja la imagen del jugador y su nivel de habilidad
        screen.blit(jugador_image, (20, 10))
        draw_button(f"{nombre_jugador}|{jugador_habilidad}|${dinero}", 250, 70)

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
                            jugador = jugadores_disponibles[-1]
                            while True:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        sys.exit()

                                screen.blit(fondo_cancha, (0, 0))
                                draw_button(f"Nombre: {nombre_jugador}", screen_width // 2, 150)
                                draw_button(f"Valor: ${valor_jugador}", screen_width // 2, 210)
                                draw_button(f"Habilidad: {habilidad_jugador}", screen_width // 2, 270)
                                draw_button(f"Salud: {jugador.salud}", screen_width // 2, 330)
                                draw_button(f"Felicidad: {jugador.felicidad}", screen_width // 2, 390)
                                draw_button(f"Edad: {jugador.edad}", screen_width // 2, 450)
                                draw_button(f"Club: {jugador.club}", screen_width // 2, 510)
                                screen.blit(jugador.imagen, (screen_width // 2 - 60, 0))
                                volver_button = draw_button("Volver al Menú", screen_width // 2, 570)
                                pygame.display.flip()

                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x, y = pygame.mouse.get_pos()
                                        if volver_button.collidepoint(x, y):
                                            break
                        elif button_text == "Ofertas de Traspaso":
                            mercado_de_traspaso(jugadores_disponibles[-1])
                        elif button_text == "Estilo de Vida":
                            gestionar_estilo_de_vida(jugadores_disponibles[-1])
                        elif button_text == "Entrenamiento":
                            entrenamiento(jugadores_disponibles[-1])  # ¿Qué es esto?
                        elif button_text == "Simular Partido":
                            simular_partido_en_tiempo_real(jugadores_disponibles[-1])
                        elif button_text == "Personalizar Personaje":
                            personalizar_personaje()  # Nueva opción
                if scrollable_area.collidepoint(x, y):
                    pass
                else:
                    scroll_up_button = pygame.Rect(screen_width - 30, 0, 30, 30)
                    scroll_down_button = pygame.Rect(screen_width - 30, screen_height - 30, 30, 30)
                    if scroll_up_button.collidepoint(x, y):
                        scroll_y += 30
                    elif scroll_down_button.collidepoint(x, y):
                        scroll_y -= 30

# Cerrar Pygame
pygame.quit()
sys.exit()
