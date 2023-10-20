import pygame

# Función para dibujar botones con una leve separación vertical
class Buttons():
    def __init__(self):
        self.screen_width
        self.screen_height
        self.spacing = 50

    def draw_button(screen, text, x, y, width=200, height=50, spacing=10):
        button = pygame.Rect(x - width / 2, y - height / 2, width, height)
        
        color_fondo = (0, 128, 0)
        color_texto = (255, 255, 255)
        
        pygame.draw.rect(screen, color_fondo, button)
        pygame.draw.rect(screen, color_texto, button, 2)
        
        font = pygame.font.Font(None, 36)
        button_text = font.render(text, True, color_texto)
        text_rect = button_text.get_rect()
        text_rect.center = (x, y)
        screen.blit(button_text, text_rect)
        return button

    def botones_personalizacion_personaje(self, parte_cuerpo, selected_option=0): #nombre placeholder
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
            botones = [self.draw_button(f'{parte_cuerpo.capitalise()} {i+1}', self.screen_width//2, 250 + i*self.spacing, 100) for i in opciones]
        for i,boton in enumerate(botones):
            if boton.collidepoint(0, 250 + i*self.spacing):     #cambie x por 0
                selected_option[parte_cuerpo] = i+1
        return selected_option