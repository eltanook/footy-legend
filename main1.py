import pygame
import sys
import random
import time
import calendar
import datetime

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

# Inicializar el calendario y eventos
current_date = datetime.date(2023, 1, 1)  # Fecha de inicio del juego
event_calendar = {}  # Almacenar eventos

def avanzar_dia():
    global current_date
    current_date += datetime.timedelta(days=1)

def generar_evento():
    # Generar eventos alternos: Día de Entrenamiento o Día de Partido
    if current_date.day % 2 == 0:
        return "Día de Entrenamiento"
    else:
        return "Día de Partido"


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
        self.lujo = 0

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

# Función para gestionar la sección de Lujo
def gestionar_lujo(jugador):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        # Crear un nuevo menú para la sección de Lujo
        lujo_menu = [
            ("Mansión", screen_width // 2, 250),
            ("Auto de Lujo", screen_width // 2, 320),
            ("Reloj de Oro", screen_width // 2, 390),
            ("Volver al Menú", screen_width // 2, 460)
        ]

        for button_text, x_button, y_button in lujo_menu:
            draw_button(button_text, x_button, y_button)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button_text, x_button, y_button in lujo_menu:
                    button = pygame.Rect(x_button - 100, y_button - 25, 200, 50)
                    if button.collidepoint(x, y):
                        if button_text == "Mansión":
                            # Aquí puedes implementar la lógica para comprar una mansión
                            jugador.lujo += 10  # Aumenta el nivel de lujo del jugador (por ejemplo)
                            print("Compraste una mansión. Tu nivel de lujo ha aumentado. Ahora es de: ", jugador.lujo)
                        elif button_text == "Auto de Lujo":
                            # Implementa la lógica para comprar un auto de lujo
                            jugador.lujo += 5  # Aumenta el nivel de lujo del jugador (por ejemplo)
                            print("Compraste un auto de lujo. Tu nivel de lujo ha aumentado. Ahora es de: ", jugador.lujo)
                        elif button_text == "Reloj de Oro":
                            # Implementa la lógica para comprar un reloj de oro
                            jugador.lujo += 2  # Aumenta el nivel de lujo del jugador (por ejemplo)
                            print("Compraste un reloj de oro. Tu nivel de lujo ha aumentado. Ahora es de: ", jugador.lujo)
                        elif button_text == "Volver al Menú":
                            return
# Función para gestionar el juego de ruleta en la sección de Casino

import random

# Función para simular el juego de la ruleta y obtener el resultado
def jugar_ruleta_y_obtener_resultado():
    # Simulación del juego de la ruleta
    resultados_posibles = ["Rojo", "Negro", "Verde", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
                           "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
    
    resultado = random.choice(resultados_posibles)  # Resultado aleatorio

    return resultado
# Función para calcular el resultado de la apuesta

def calcular_apuesta(resultado_ruleta, apuesta):
    # Definimos los resultados posibles de la ruleta
    resultados_posibles = ["Rojo", "Negro", "Verde", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
                           "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]
    
    # Comprobamos si el resultado de la ruleta está en los resultados posibles
    if resultado_ruleta in resultados_posibles:
        if resultado_ruleta == "Rojo":
            # Si el resultado es "Rojo", el jugador gana el doble de su apuesta
            apuesta_ganada = apuesta * 2
        else:
            # Si el resultado no es "Rojo", el jugador pierde su apuesta
            apuesta_ganada = -apuesta
    else:
        # Si el resultado no es válido, la apuesta es nula (0)
        apuesta_ganada = 0
    
    return apuesta_ganada


def jugar_ruleta(jugador):
    apuesta = 0  # Inicializa la apuesta del jugador

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        # Muestra el saldo actual del jugador y la opción para realizar una apuesta
        dinero= 1000 # no toma el real no se que onda
        draw_button(f"Dinero: ${dinero}", screen_width // 2, 100)
        draw_button(f"Apuesta: ${apuesta}", screen_width // 2, 150)

        # Botones para realizar apuestas
        apuesta_button_10 = draw_button("Apuesta $10", 100, 250)
        apuesta_button_50 = draw_button("Apuesta $50", 250, 250)
        apuesta_button_100 = draw_button("Apuesta $100", 400, 250)


        # Botón para girar la ruleta
        girar_button = draw_button("Girar la Ruleta", screen_width // 2, 350)
        draw_button("Volver al Menú", screen_width // 2, 570)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if apuesta_button_10.collidepoint(x, y):
                    apuesta += 10
                elif apuesta_button_50.collidepoint(x, y):
                    apuesta += 50
                elif apuesta_button_100.collidepoint(x, y):
                    apuesta += 100
                elif girar_button.collidepoint(x, y):
                    # Implementa la lógica del juego de ruleta aquí
                    resultado = jugar_ruleta_y_obtener_resultado()
                    apuesta_ganada = calcular_apuesta(resultado, apuesta)
                    dinero += apuesta_ganada
                    print(f"El resultado de la ruleta fue {resultado}. Ganaste ${apuesta_ganada}.")
                elif button_text == "Volver al Menú":
                    return
# Función para gestionar la sección de Relaciones
def gestionar_relaciones(jugador):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        # Crear un nuevo menú para la sección de Relaciones
        relaciones_menu = [
            ("Padres", screen_width // 2, 250),
            ("Equipo", screen_width // 2, 320),
            ("Entrenador", screen_width // 2, 390),
            ("Hinchada", screen_width // 2, 460),
            ("Volver al Menú", screen_width // 2, 530)
        ]

        for button_text, x_button, y_button in relaciones_menu:
            draw_button(button_text, x_button, y_button)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button_text, x_button, y_button in relaciones_menu:
                    button = pygame.Rect(x_button - 100, y_button - 25, 200, 50)
                    if button.collidepoint(x, y):
                        if button_text == "Padres":
                            # Implementa la funcionalidad para mejorar las relaciones con los padres
                            print("Mejora tus relaciones con tus padres aquí.")
                        elif button_text == "Equipo":
                            # Implementa la funcionalidad para mejorar las relaciones con el equipo
                            print("Mejora tus relaciones con tu equipo aquí.")
                        elif button_text == "Entrenador":
                            # Implementa la funcionalidad para mejorar las relaciones con el entrenador
                            print("Mejora tus relaciones con tu entrenador aquí.")
                        elif button_text == "Hinchada":
                            # Implementa la funcionalidad para mejorar las relaciones con la hinchada
                            print("Mejora tus relaciones con la hinchada aquí.")
                        elif button_text == "Volver al Menú":
                            return

# Función para gestionar la sección de Estilo de Vida
def gestionar_estilo_de_vida(jugador):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        # Crear un nuevo menú para Estilo de Vida
        estilo_de_vida_menu = [
            ("Lujo", screen_width // 2, 250),
            ("Casino", screen_width // 2, 320),
            ("Relaciones", screen_width // 2, 390),
            ("Volver al Menú", screen_width // 2, 460)
        ]

        for button_text, x_button, y_button in estilo_de_vida_menu:
            draw_button(button_text, x_button, y_button)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button_text, x_button, y_button in estilo_de_vida_menu:
                    button = pygame.Rect(x_button - 100, y_button - 25, 200, 50)
                    if button.collidepoint(x, y):
                        if button_text == "Lujo":
                            gestionar_lujo(jugador)
                        elif button_text == "Casino":
                            jugar_ruleta(jugador)
                        elif button_text == "Relaciones":
                            gestionar_relaciones(jugador)
                        elif button_text == "Volver al Menú":
                            return


# Función para simular un partido en tiempo real con tiempo lineal
def simular_partido_en_tiempo_real(jugador):
    tiempo_transcurrido = 0

    # Clubes rivales fijos durante todo el partido
    club_local = "Tu Club"
    club_rival = random.choice(["Riber", "San silencio", "Mostoles FC"])

    goles_local = 0
    goles_rival = 0

    # ... (código previo)

    while tiempo_transcurrido <= 95:  # Ajusta el rango de tiempo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        # Calcula el tiempo en minutos (incluso después de los 90 minutos)
        tiempo_actual = tiempo_transcurrido

        draw_button(club_local, screen_width // 2 - 100, 100)
        draw_button(f"{goles_local} - {goles_rival}", screen_width // 2, 200)
        draw_button(club_rival, screen_width // 2 + 100, 100)

        # Muestra el tiempo actual
        draw_button(f"Tiempo: {tiempo_actual} min", 200, 300)

        # Realiza eventos aleatorios durante el partido
        if tiempo_transcurrido % 5 == 0:
            evento = random.choice(["Gol", "Tarjeta Amarilla", "Tarjeta Roja", "Cambio"])
            equipo = random.choice([club_local, club_rival])

            if evento == "Gol":
                # Determina el equipo que anota un gol
                if equipo == club_local:
                    goles_local += 1
                    mensaje = f"Gol de {equipo}!"
                else:
                    goles_rival += 1
                    mensaje = f"Gol de {equipo}!"

            elif evento == "Tarjeta Amarilla":
                mensaje = f"Tarjeta Amarilla para {equipo}"

            elif evento == "Tarjeta Roja":
                mensaje = f"Tarjeta Roja para {equipo}"

            else:  # Cambio
                mensaje = f"Cambio en {equipo}"

            draw_button(mensaje, 200, 400)
            pygame.display.flip()

            # Pausa de 1.5 segundos después de mostrar el evento
            time.sleep(1.5)

        pygame.display.flip()

        tiempo_transcurrido += 1  # Aumenta el tiempo en 1 minuto para mantener la linealidad
        time.sleep(0.1)  # Hacer el partido avanzar más rápido (0.1 segundos por minuto)

    # Calcular la calificación final ficticia basada en los goles anotados
    calificacion_final = (goles_local - goles_rival) * 10

# ... (código previo)


    # Al final del partido
    resultado = "Victoria" if goles_local > goles_rival else ("Empate" if goles_local == goles_rival else "Derrota")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_cancha, (0, 0))

        draw_button(club_local, screen_width // 2 - 100, 100)
        draw_button(f"{goles_local} - {goles_rival}", screen_width // 2, 200)
        draw_button(club_rival, screen_width // 2 + 100, 100)

        draw_button(f"Resultado: {resultado}", 200, 300)
        draw_button(f"Minutos: 95", 200, 350)
        draw_button(f"Calificación: {calificacion_final:.1f}", 200, 400)

        continuar_al_menu = draw_button("Continuar", 200, 450)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if continuar_al_menu.collidepoint(x, y):
                    return

# Función para personalizar el personaje

selected_options = {
    "skin": 1,
    "nose": 1,
    "mouth": 1,
    "eye": 1,
    "hair": 1
}
def personalizar_personaje():
    # Rutas de las carpetas de opciones para personalizar el personaje
    skin_options = [f"cara/pieles/piel{i}.png" for i in range(1, 2)]
    nose_options = [f"cara/narices/nariz{i}.png" for i in range(1, 8)]
    mouth_options = [f"cara/bocas/boca{i}.png" for i in range(1, 4)]
    eye_options = [f"cara/ojos/ojos{i}.png" for i in range(1, 9)]
    hair_options = [f"cara/pelos/pelo{i}.png" for i in range(1, 9)]

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

        
def entrenamiento(jugador):
    mejora_habilidad = random.randint(1, 5)
    jugador.habilidad += mejora_habilidad
    jugador.salud -= random.randint(1, 5)
    print(f"{jugador.nombre} ha mejorado su habilidad en {mejora_habilidad} puntos durante el entrenamiento.")
    print(f"Salud actual: {jugador.salud}")
          
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


# ... (código previo)

# Bucle principal
running = True
scroll_y = 0
jugador_image = jugadores_disponibles[-1].imagen
jugador_habilidad = jugadores_disponibles[-1].habilidad
x = 0  # Definir x para evitar errores

# ... (código previo)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fondo_cancha, (0, 0))

    # Mostrar la fecha en la esquina superior derecha del menú principal
    fecha_text = font.render(current_date.strftime("%d/%m/%Y"), True, color_texto)
    screen.blit(fecha_text, (screen_width - 150, 10))

    if not nombre_jugador:
        nombre_jugador = obtener_nombre()

    if nombre_jugador:
        menu_buttons = [
            ("Mi Jugador", screen_width // 2, 180),
            ("Ofertas de Traspaso", screen_width // 2, 240),
            ("Estilo de Vida", screen_width // 2, 300),
            ("Entrenamiento", screen_width // 2, 360),
            ("Personalizar Personaje", screen_width // 2, 420),
            ("Salir", screen_width // 2, 480),
        ]

        y = 400
        for button_text, x_button, y_button in menu_buttons:
            draw_button(button_text, x_button, y_button + scroll_y)
            y += spacing

        # Dibuja la imagen del jugador personalizado y su información
        selected_skin = selected_options['skin']
        selected_nose = selected_options['nose']
        selected_mouth = selected_options['mouth']
        selected_eye = selected_options['eye']
        selected_hair = selected_options['hair']
        
        player_image = pygame.image.load(f"cara/pieles/piel{selected_skin}.png")
        player_image = pygame.transform.scale(player_image, (120, 120))
        screen.blit(player_image, (20, 10))

        draw_button(f"{nombre_jugador}|{jugador_habilidad}|${dinero}", 250, 70)
        continuar_button = draw_button("Continuar", screen_width - 100, screen_height - 30, 150, 30)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            if continuar_button.collidepoint(x, y):
                print("Botón Continuar presionado")
                avanzar_dia()
                evento = generar_evento()
                if evento == "Día de Entrenamiento":
                    entrenamiento(jugadores_disponibles[-1])  # Realizar acciones para el día de entrenamiento
                elif evento == "Día de Partido":
                    simular_partido_en_tiempo_real(jugadores_disponibles[-1])  # Realizar acciones para el día de partido

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
                        elif button_text == "Simular Partido":
                            simular_partido_en_tiempo_real(jugadores_disponibles[-1])
                        elif button_text == "Personalizar Personaje":
                            personalizar_personaje()  
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