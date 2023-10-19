import pygame

# Función para dibujar botones con una leve separación vertical
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
