import pygame
class Button:
    def __init__(self, screen, x, y, width, height, text, color, size):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 20)
        self.size = size

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event, funcion):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                funcion()
    

class ButtonJ:
    def __init__(self, screen1, screen2, x, y, width, height, text, color, size):
        self.screen1 = screen1 #screen
        self.screen2 = screen2 #modulo (coords)
        self.rect = pygame.Rect(x+ screen2[0], y+ screen2[1], width, height)
        self.text = text
        self.color = color
        self.size = size
        self.font = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", self.size)

    def draw(self):
        pygame.draw.rect(self.screen1, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen1.blit(text_surface, text_rect)

    def handle_event(self, event, funcion):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                funcion()
                
                
class ButtonM:
    def __init__(self, screen, x, y, width, height, text, color):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 20)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def handle_event(self, event, funcion):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                funcion()
                
    def handle_event1(self, event, posicionreal, funcion):
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect_cambio = pygame.Rect(self.rect.x + posicionreal[0], self.rect.y + posicionreal[1], self.rect.width, self.rect.height)
            if rect_cambio.collidepoint(event.pos):
                funcion()