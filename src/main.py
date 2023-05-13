from __future__ import annotations
import pygame
from juego.manejodearchivos import *
from pygame.locals import *
from juego.button import *
from juego.bomba import Bomba
from juego.modulos import *
import os
import random
from juego.listadoble import *
import time

pygame.init()
screen = pygame.display.set_mode((1000,562))
pygame.display.set_caption("Binary Bomb Squad")

clock = pygame.time.Clock()

BLACK = pygame.Color("#0a100d")
ORANGE = pygame.Color("#f34213")
GREEN = pygame.Color('#588157')
GOLD = pygame.Color('#fcbf49')
VANILLA = pygame.Color('#e9eb9e')
WHITE = pygame.Color("#ffffff")
GOLDEN = pygame.Color('#fcbf49')
SILVER = pygame.Color('#dbd4d3')
VINOTINTO = pygame.Color('#9b1d20')
font = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 20)
font1 = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 40)

#background = pygame.image.load('graphics/background.png')

frame = pygame.Surface((680,460))
module1 = pygame.Surface((202,202))
module2 = pygame.Surface((202,202))
module3 = pygame.Surface((202,202))
module4 = pygame.Surface((202,202))
module5 = pygame.Surface((202,202))
timer = pygame.Surface((202,202))

frame.fill(GREEN)
module1.fill(VANILLA)
module2.fill(VANILLA)
module3.fill(VANILLA)
module4.fill(VANILLA)
module5.fill(VANILLA)
timer.fill(VANILLA)

click = False
def main_menu():
     while True:
        fondo = pygame.image.load("Laboratorio-3-Estructura/src/graphics/fondo_Inicio.jpg")
        screen.blit(fondo, (0, 0))
        image = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Bynary Bomb logo nobg.png")
        resized_image = pygame.transform.scale(image, (400, 400))
        screen.blit(resized_image, (320, 0))
        play_button = Button(screen, 100, 430, 200, 50, "JUGAR", (VINOTINTO))
        play_button.draw()
        credits_button = Button(screen, 400, 430, 200, 50, "CRÉDITOS", (VINOTINTO))
        credits_button.draw()
        exit_button = Button(screen, 700, 430, 200, 50, "SALIR", (VINOTINTO))
        exit_button.draw()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            play_button.handle_event(event, lambda: opcJugar())
            credits_button.handle_event(event, lambda: creditos())
            exit_button.handle_event(event, lambda: exit())

        pygame.display.update()
        clock.tick(60)
click = False

def opcJugar():
    global a1
    global b1
    global n1
    global a2  
    global b2
    global n2
    list1 = DoublyLinkedList()
    list2 = DoublyLinkedList()
    font2 = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 10)
    for i in [0, 1, 2, 3]:
        list1.add_node(i)
    for i in [3, 4, 5]:
        list2.add_node(i)    
    a1 = list1.head
    b1 = list1.head.prev
    n1 = list1.head.next
    a2 = list2.head
    b2 = list2.head.prev
    n2 = list2.head.next
    while True:
        screen.fill(GOLDEN)
        play_button = Button(screen, 150, 430, 200, 50, "JUGAR", (255,0,0), 20)
        play_button.draw()
        manual_button = Button(screen, 650, 430, 200, 50, "MANUAL", (255,0,0), 20)
        manual_button.draw()
        font1 = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 20)
        text_surface = font1.render("AJUSTE DE BOMBA", True, (255, 255, 255))
        screen.blit(text_surface, (370, 35))
        atras1_button = Button(screen, 300, 150, 40, 40, "<", (255, 0, 0), 20)
        adelante1_button = Button(screen, 650, 150, 40, 40, ">", (255, 0, 0), 20)
        adelante1_button.draw()
        atras1_button.draw()
        atras2_button = Button(screen, 300, 290, 40, 40, "<", (255, 0, 0), 20)
        adelante2_button = Button(screen, 650, 290, 40, 40, ">", (255, 0, 0), 20)
        adelante2_button.draw()
        atras2_button.draw()
       #listica de errores
        textE = font1.render("ERRORES", True, (255, 255, 255))
        screen.blit(textE, (440, 90))
        text_1 = font1.render(str(a1.data), True, (255, 255, 255))
        screen.blit(text_1, (495, 135))
        if a1.prev == None:
            text11 = font2.render("", True, (255, 255, 255))
            screen.blit(text11, (475, 150))
        else:
            text11 = font2.render(str(a1.prev.data), True, (255, 255, 255))
            screen.blit(text11, (475, 150))
        if a1.next == None:
            text21 = font2.render("", True, (255, 255, 255))
            screen.blit(text21, (525, 150))
        else:
            text21 = font2.render(str(a1.next.data), True, (255, 255, 255))
            screen.blit(text21, (525, 150))

        #listica de modulos
        textM = font1.render("MODULOS", True, (255, 255, 255))
        screen.blit(textM, (440, 230))
        text_2 = font1.render(str(a2.data), True, (255, 255, 255))
        screen.blit(text_2, (495, 280))
        if a2.prev == None:
            text12 = font2.render("", True, (255, 255, 255))
            screen.blit(text12, (475, 295))
        else:
            text12 = font2.render(str(a2.prev.data), True, (255, 255, 255))
            screen.blit(text12, (475, 295))
        if a2.next == None:
            text22 = font2.render("", True, (255, 255, 255))
            screen.blit(text22, (525, 295))
        else:
            text22 = font2.render(str(a2.next.data), True, (255, 255, 255))
            screen.blit(text22, (525, 295))
    
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            play_button.handle_event(event, lambda: game())
            manual_button.handle_event(event, lambda: archivo())
            adelante1_button.handle_event(event, lambda: moverLista1(True))
            atras1_button.handle_event(event, lambda: moverLista1(False))
            adelante2_button.handle_event(event, lambda: moverLista2(True))
            atras2_button.handle_event(event, lambda: moverLista2(False))

        pygame.display.update()
        clock.tick(60)

def moverLista1(modo): #modo: False-Retroceso, True-Avance
    global a1
    if modo:
        if a1.next != None:
            a1 = a1.next
    else:
        if a1.prev !=None:
            a1 = a1.prev
def moverLista2(modo): #modo: False-Retroceso, True-Avance
    global a2
    if modo:
        if a2.next != None:
            a2 = a2.next
    else:
        if a2.prev !=None:
            a2 = a2.prev

def archivo():
    nombre_archivo = 'Laboratorio-3-Estructura/src/files/BINARY BOMB SQUAD MANUAL borrador.pdf'
    ruta_proyecto = os.path.abspath(os.curdir)
# Obtiene la ruta completa del archivo dentro de la carpeta del proyecto
    ruta_archivo = os.path.join(ruta_proyecto, nombre_archivo)
    if os.path.exists(ruta_archivo):
    # Abre el archivo PDF en la aplicación predeterminada del sistema
        if os.name == 'nt':
            os.startfile(ruta_archivo)
        elif os.name == 'posix':
            subprocess.Popen(['open', archivo_pdf])
    else:
        print(f'El archivo {ruta_archivo} no existe.')

def creditos():
    creditos_movibles = [
    "BINARY BOMB SQUAD",
    "",
    "INTEGRANTES DEL GRUPO:",
    "1. MARÍA CAMILA OSORNO",
    "2. JUAN FELIPE SANTOS",
    "3. SAMUEL MATIZ",
    "4. ALBERTO JOSÉ SANDOVAL",
    "",
    "DIRECTOR DEL PROYECTO:",
    "1. MARÍA CAMILA OSORNO",
    "",
    "DIRECTOR ASISTENTE:",
    "1. JUAN FELIPE SANTOS",
    "",
    "LÍDER DE DISEÑO:",
    "1. SAMUEL MATIZ",
    "",
    "LÍDER DE PROGRAMACIÓN:",
    "1. ALBERTO JOSÉ SANDOVAL",
    ]
    start_time = time.time()
    duration = 10
    fuente_titulo = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 36)
    fuente_creditos = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 24)
    
    posicionbajada = 0
    while True:
        screen.fill(SILVER)
        posicion_y = 15
        # Dibuja cada línea de crédito
        for linea in creditos_movibles:
            credito_superficie = fuente_creditos.render(linea, True, (BLACK))
            credito_rect = credito_superficie.get_rect(center=(1000 // 2, posicion_y-posicionbajada))
            screen.blit(credito_superficie, credito_rect)
            posicion_y += 40
        # Actualiza la pantalla
        current_time = time.time()
        print(current_time - start_time)
        if current_time - start_time >= 0.5:
            posicionbajada += 40 # Incrementar la posición vertical
            start_time = current_time  # Reiniciar el tiempo de inicio
        if posicionbajada >= 800:
            main_menu()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def game():
    # Duración del temporizador en segundos
    duration = 300

    # Obtener el tiempo de inicio
    start_time = time.time()
    
    global a1 #errores
    global a2 #modulos
    running = True
    escribir = ManejoDeArchivos()
    escribir.limpiarArchivo()
    escribir.escribirConfiguracion(str(a1.data))
    escribir.escribirConfiguracion(str(a2.data))
    image1 = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Bynary Bomb logo nobg.png")
    bombita = Bomba(duration, int(a1.data), int(a2.data), 10)
    bombita.asignar_modulos()
    pos = [module1, module2, module3, module4, module5]

    
    while running:
        x = 0
        for modulo in bombita.modulos:
            modulo.dibujarFondo(pos[x])
            if x < a2.data -1:
                x= x+1
        bombita.colocarFranja(timer)
        x = 0
        screen.fill(BLACK)
        for modulo in bombita.modulos:
            if modulo.nombre == "Cables Básicos":
                if pos[x] == module1:
                    posCB = (180,71)
                elif pos[x] == module2:
                    posCB = (402,71)
                elif pos[x] == module3:
                    posCB = (625,71)
                elif pos[x] == module4:
                    posCB = (180,293)
                elif pos[x] == module5:
                    posCB = (402,293)
                modulo.dibujarElementos(pos[x], screen, posCB)
            elif modulo.nombre == "Cables Complejos": 
                if pos[x] == module1:
                    posCC = (180,71)
                elif pos[x] == module2:
                    posCC = (402,71)
                elif pos[x] == module3:
                    posCC = (625,71)
                elif pos[x] == module4:
                    posCC = (180,293)
                elif pos[x] == module5:
                    posCC = (402,293)
                modulo.dibujarElementos(pos[x], screen, posCC)
            elif modulo.nombre == "Código": 
                if pos[x] == module1:
                    posC = (180,71)
                elif pos[x] == module2:
                    posC = (402,71)
                elif pos[x] == module3:
                    posC = (625,71)
                elif pos[x] == module4:
                    posC = (180,293)
                elif pos[x] == module5:
                    posC = (402,293)
                modulo.dibujarElementos(pos[x], screen, posC)
            elif modulo.nombre == "Memoria":
                if pos[x] == module1:
                    posM = (180,71)
                elif pos[x] == module2:
                    posM = (402,71)
                elif pos[x] == module3:
                    posM = (625,71)
                elif pos[x] == module4:
                    posM = (180,293)
                elif pos[x] == module5:
                    posM = (402,293)
                modulo.dibujarElementos(pos[x], posM)
            elif modulo.nombre == "Exigente":
                if pos[x] == module1:
                    posexigente = (180,71)  
                elif pos[x] == module2:
                    posexigente = (402,71)
                elif pos[x] == module3:
                    posexigente = (625,71)
                elif pos[x] == module4:
                    posexigente = (180,293)
                elif pos[x] == module5:
                    posexigente = (402,293)
                modulo.dibujarElementos(pos[x], posexigente)
            if x < a2.data -1:
                x= x+1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        #screen.blit(background, (0,0))
        screen.blit(frame, (165,56))
        screen.blit(module1, (180,71))
        screen.blit(module2, (402,71))
        screen.blit(module3, (625,71))
        screen.blit(module4, (180,293))
        screen.blit(module5, (402,293))
        screen.blit(timer, (625,293))
        
         # Calcular el tiempo restante
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = max(duration - elapsed_time, 0)
        bombita.tiempo_agotado()
        # Formatear el tiempo restante en formato mm:ss
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        time_text = f"{minutes:02d}:{seconds:02d}"

        # Renderizar el tiempo en la ventana
        text_surface = font.render(time_text, True, WHITE)
        text_rect = text_surface.get_rect(center=(730,390))
        screen.blit(text_surface, text_rect)
        fondotimer = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Timer/fondo_timer.png")
        timer.blit(fondotimer,(0,0))
        
        pygame.display.update()
        clock.tick(60)

main_menu()