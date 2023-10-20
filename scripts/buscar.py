#%%
import csv
import numpy as np
import pygame
import sys
#%%
class Buscar(object):

    def __init__(self):
        self.fuerza = 0
        self.velocidad = 0
        self.resistencia = 0
        self.tecnica = 0
        self.vision = 0
        self.int_tactica = 0
        self.defensa = 0
        self.toma_decisiones = 0
        self.teamwork = 0
        self.caracter = 0
        self.resistencia_lesiones = 0
        self.mentalidad = 0
        self.fisico = 0        
        self.liderazgo = 0
        self.age = 0
        self.stamina = 0
        self.media = 0
        self.liga = ''
        self.rival = ''
        # self.club = 'Manchester City'
        
    def datos_jugador(self, archivo='resources\player\data\datos_jugador.csv'):
            '''recopila los datos del jugador relevantes para el partido (stamina, felicidad, habilidades) para que influyan en el juego
            archivo (diria que un csv xq es lo que se manejar) es un nombre placeholder, 
                debería buscar siempre el mismo (a no ser que queramos que se puedan guardar varios jugadores)
            esta solo se usaria una vez (cuando recien entras al juego) para buscar del csv y despues buscaria de los self
            pienso que se puede hacer de otra forma mas util pero para arrancar debiria andar bien algo de este estilo'''
            with open(archivo, 'rt') as f:
                lista = []
                datos = csv.reader(f)
                headers = next(datos)
                for fila in datos:
                    lista.append(dict(zip(headers,fila)))
                for i in lista:
                    self.nombre = str(i['nombre'])
                    self.stamina = int(i['stamina'])
                    self.felicidad = int(i['felicidad'])
                    self.age = int(i['age'])
                    self.club = str(i['club'])
                    self.valor = int(i['valor'])
                    self.money = float(i['dinero'])
                    self.popularidad = int(i['popularidad'])
                    self.fuerza = int(i['fuerza'])
                    self.velocidad = int(i['velocidad'])
                    self.resistencia = int(i['resistencia'])
                    self.tecnica = int(i['tecnica'])
                    self.vision = int(i['vision'])
                    self.int_tactica = int(i['inteligencia tactica'])
                    self.defensa = int(i['defensa'])
                    self.toma_decisiones = int(i['toma decisiones'])
                    self.teamwork = int(i['teamwork'])
                    self.caracter = int(i['caracter'])
                    self.resistencia_lesiones = int(i['resistencia lesiones'])
                    self.mentalidad = int(i['mentalidad'])
                    self.fisico = int(i['fisico'])
                    self.liderazgo = int(i['liderazgo'])
            return lista

    def media_jugador(self):
        attribute_list = [int(self.fuerza), int(self.velocidad), int(self.resistencia), int(self.tecnica), int(self.vision), 
                                int(self.int_tactica), int(self.defensa), int(self.toma_decisiones), int(self.teamwork), int(self.caracter), 
                                int(self.resistencia_lesiones), int(self.mentalidad), int(self.fisico), int(self.liderazgo)]       
        self.media = round(np.mean(attribute_list))
        return round(np.mean(attribute_list))

    def traer_equipos_archivo(self, archivo='..\data\Football teams.csv'):
        '''hace una lista de diccionarios de todos los equipos del archivo parecida a:
        [{'Team': 'Arsenal', 'Tournament': 'Premier League'}, 
        {'Team': 'Bayern Munich', 'Tournament': 'Bundesliga'}] pero con mas atributos por equipo

        :param archivo: archivo csv con datos de equipos
        :return : lista de diccionarios
        '''
        with open(archivo, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            equipos=[dict(zip(headers, row)) for row in rows]
        return equipos
    
    def obtener_equipos_por_ligas(self, lista_ligas=None):
        '''busca los equipos en la/s liga/s que se le pide y devuelve una lista de diccionarios 
        con una lista de tuplas -> [{liga1: [(equipo1, rating), (equipo2, rating)]},
                                    {liga2: [(equipo1, rating), (equipo2, rating)]}]

        :param lista_ligas: lista de strings con los nombres de las ligas
        :return : lista de diccionarios de lista de tuplas'''
        # la idea es usar el rating para que el juego sepa como les deberia ir a cada equipo en su liga
            # y que tan bien deberia jugar contra el equipo del jugador
        # lo podemos randomizar despues de cada liga para que haya variedad
        if lista_ligas is None:
            lista_ligas=[self.liga]

        equipos = self.traer_equipos_archivo()
        equipos_por_liga = []
        for liga in lista_ligas:
            equipos_de_la_liga = []
            for equipo in equipos:
                if equipo['Tournament'] == liga:
                    equipos_de_la_liga.append((equipo['Team'], float(equipo['Rating'])))
            equipos_por_liga.append({liga:equipos_de_la_liga})
        return equipos_por_liga

    def liga_jugador(self, ligas):
        '''busca en la lista de ligas y devuelve en la que esta jugando actualmente el jugador'''
        #esta no debe andar de momento pero creo que se va a parecer mucho a esto
        for liga in ligas:
            if self.club in liga:
                self.liga = liga
                break
    
    def obtener_jugadores(self, archivo='archivo_jugadores'):
        '''busca los jugadores del archivo de jugadores'''
        lista_jugadores=[]
        with open(archivo, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            lista_jugadores=[dict(zip(headers, row)) for row in rows]
        return lista_jugadores

    def jugadores_en_liga(self, lista_jugadores):
        '''limpia la lista de jugadores para quedarse solo con los de una liga determinada'''
        jugadores_relevantes = []
        for i in lista_jugadores:
            if i['liga'] == self.liga:
                jugadores_relevantes.append(i)
        return jugadores_relevantes
    
    def resto_partido(self, lista_jugadores):
        '''busca los jugadores involucrados en el partido y los devuelve para que se balancee el partido acorde a las capacidades de los equipos
        lista_juagdores deberia tener solo los jugadores de la liga en la que juega el jugador o algo asi'''
        resto=[]
        for i in lista_jugadores:
            if i['club'] == self.rival:
                resto.append(i)
        return resto

    def actualizar_habilidad(self, habilidad_entrenada, entrenando=True):
        '''actualiza las habilidades del jugador desp de entrenamientos
        se puede implementar tambien que empiezen a bajar segun la edad
        entrenando es para chequear si es que el jugador entreno o si hay que bajarle stats xq no lo entrena hace mucho
        :param habilidad_entrenada: int
        :param entrenando: bool
        :return : int'''
        edad = self.age
        if entrenando:
            if 16<=edad<=24:
                habilidad_entrenada += 5 #estos valores habria que balancearlos, son placeholders
            elif 25<=edad<=32:
                habilidad_entrenada += 2
            else:
                habilidad_entrenada += 1
        else:
            if 16<=edad<=24:
                habilidad_entrenada -= 1 #estos valores habria que balancearlos, son placeholders
            elif 25<=edad<=32:
                habilidad_entrenada -= 2
            else:
                habilidad_entrenada -= 5
        return habilidad_entrenada

    def obtener_nombre(self):
        ''' hay que hacer que esto lo escriba en el csv'''
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

            self.screen.blit(self.fondo_cancha, (0, 0))

            txt_surface = self.font.render(nombre, True, color) #aca font con self? creo q si
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.screen, color, input_box, 2)
            pygame.display.flip()

        return nombre

#%%

