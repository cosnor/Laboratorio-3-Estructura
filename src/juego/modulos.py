from __future__ import annotations
from abc import ABC
from typing import List
from random import * 
from random import shuffle
import time
import threading
import pygame
from juego.bomba import *

class Observador: 
    def enviar_error(self, mensaje):
        pass

class Modulo:
    def __init__(self, pos) -> None:
        self.estado= False #False indica que no ha sido resuelto
        self.observadores = []
        self.pos = pos
    
    def agregar_observador(self,observador): 
        self.observadores.append(observador)
    
    def equivocacion(self):
        mensaje = "Se ha equivocado"
        for observador in self.observadores:
            observador.enviar_error(mensaje)

class ModuloCablesBasicos(Modulo):
    def __init__(self, franja: str, pos:int) -> None:
        super().__init__(pos)
        self.nombre = "Cables Básicos"
        self.cables: List["Cable"]=[]
        self.franja = franja
    
    def dibujarFondo(self, pantalla):
        #self.agregar_cables()
        fondo = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Fondos/fondo_cables_simples.png")
        pantalla.blit(fondo, (0, 0))
    
    def dibujarElementos(self, pantalla): 
        for cable in self.cables: 
            pantalla.blit(cable.icono_cable, (cable.posx, cable.posy))
           # if cable.icono_cable.collidepoint(cable.posx, cable.posy):
            #    print("xd")
    def agregar_cables(self):
        #Asignación aleatoria del orden de los cables
        LISTA_COLORES = ["Rojo", "Azul", "Negro", "Blanco"]
        shuffle(LISTA_COLORES)
        for i in range(0,4):
            if i == 0: 
                if LISTA_COLORES[i] == "Rojo": 
                    self.cables.append(CableRojo(color=LISTA_COLORES[i], posx= 0, posy = 1))
                elif LISTA_COLORES[i] == "Azul":
                    self.cables.append(CableAzul(color=LISTA_COLORES[i], posx= 0, posy = 1))
                elif LISTA_COLORES[i] == "Negro":
                    self.cables.append(CableNegro(color=LISTA_COLORES[i], posx= 0, posy = 1))
                elif LISTA_COLORES[i] == "Blanco":
                    self.cables.append(CableBlanco(color=LISTA_COLORES[i], posx= 0, posy = 1))
            elif i == 1: 
                if LISTA_COLORES[i] == "Rojo": 
                    self.cables.append(CableRojo(color=LISTA_COLORES[i], posx= 0, posy = 30))
                elif LISTA_COLORES[i] == "Azul":
                    self.cables.append(CableAzul(color=LISTA_COLORES[i], posx= 0, posy = 30))
                elif LISTA_COLORES[i] == "Negro":
                    self.cables.append(CableNegro(color=LISTA_COLORES[i], posx= 0, posy = 30))
                elif LISTA_COLORES[i] == "Blanco":
                    self.cables.append(CableBlanco(color=LISTA_COLORES[i], posx= 0, posy = 30))
            elif i == 2: 
                if LISTA_COLORES[i] == "Rojo": 
                    self.cables.append(CableRojo(color=LISTA_COLORES[i], posx= 0, posy = 60))
                elif LISTA_COLORES[i] == "Azul":
                    self.cables.append(CableAzul(color=LISTA_COLORES[i], posx= 0, posy = 60))
                elif LISTA_COLORES[i] == "Negro":
                    self.cables.append(CableNegro(color=LISTA_COLORES[i], posx= 0, posy = 60))
                elif LISTA_COLORES[i] == "Blanco":
                    self.cables.append(CableBlanco(color=LISTA_COLORES[i], posx= 0, posy = 60))
            elif i == 3: 
                if LISTA_COLORES[i] == "Rojo": 
                    self.cables.append(CableRojo(color=LISTA_COLORES[i], posx= 0, posy = 90))
                elif LISTA_COLORES[i] == "Azul":
                    self.cables.append(CableAzul(color=LISTA_COLORES[i], posx= 0, posy = 90))
                elif LISTA_COLORES[i] == "Negro":
                    self.cables.append(CableNegro(color=LISTA_COLORES[i], posx= 0, posy = 90))
                elif LISTA_COLORES[i] == "Blanco":
                    self.cables.append(CableBlanco(color=LISTA_COLORES[i], posx= 0, posy = 90))
        
    def cortar_cable(self, CableBasico: object): 
        #Validación que modulo esté sin desactivar
        if self.estado == False: 
            CableBasico.set_estado_cortado()
            self.validacion(CableBasico)
        else: 
            print ("El modulo ya está desactivado")

    def validacion(self, CableBasico):
        #Comprobación de que el cable cortado sea el correcto luego de  presionar enviar o cortar un cable
        if self.franja == "amarilla": 
            if self.cables[0].color =="Rojo" and CableBasico.color == "Rojo":  
                self.estado = True
                print("Modulo desactivado")
            elif self.cables[1].color == "Azul" and CableBasico.color == self.cables[2].color:
                self.estado = True
                print("Modulo desactivado")
            elif CableBasico.color == self.cables[3].color:
                self.estado = True
                print("Modulo desactivado")
            else:             
                print("Equivocación")
                self.equivocacion()                

        if self.franja == "rosada":
            if self.cables[3].color == "Blanco" and CableBasico.color == "Blanco":
                self.estado = True
                print("Modulo desactivado")
            elif self.cables[2].color == "Azul" and CableBasico.color == self.cables.color[1]:
                self.estado = True
                print("Modulo desactivado")
            elif CableBasico.color == self.cables[2].color:
                self.estado = True
                print("Modulo desactivado")
            else: 
                print("Equivocación")
                self.equivocacion() 

        if self.franja == "verde":
            if self.cables[1].color == "Negro" and CableBasico.color == "Negro":
                self.estado = True
                print("Modulo desactivado")
            elif self.cables[3].color == "Negro" and CableBasico.color == "Negro":
                self.estado = True
                print("Modulo desactivado")
            elif CableBasico.color == self.cables[0].color: 
                self.estado = True
                print("Modulo desactivado")
            else: 
                print("Equivocación")
                self.equivocacion() 

        if self.franja == "blanca": 
            #!TO DO: Cambiar a cables normales
            if CableComplejo == None: 
                self.estado = True
                print("Modulo desactivado")
            else: 
                print("Equivocación")
                self.equivocacion() 

class ModuloCablesComplejos(Modulo):
    def __init__(self, pos:int) -> None:
        super().__init__(pos)
        self.nombre = "Cables Complejos"
        self.cables: List["Cable"]=[]
    
    def dibujarFondo(self, pantalla):
        fondo = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Fondos/fondo_cables_complejos.png")
        pantalla.blit(fondo, (0, 0))
    
    def dibujarElementos(self, pantalla):
        for i, cable in enumerate(self.cables): 
            if i == 0: 
                pantalla.blit(cable.icono, (0,0))
                pantalla.blit(cable.icono_led, (0,0))
                pantalla.blit(cable.icono_letra, (0,0))
            elif i == 1: 
                pantalla.blit(cable.icono, (22,0))
                pantalla.blit(cable.icono_led, (22,0))
                pantalla.blit(cable.icono_letra, (22,0))
            elif i == 2: 
                pantalla.blit(cable.icono, (46,0))
                pantalla.blit(cable.icono_led, (46,0))
                pantalla.blit(cable.icono_letra, (46,0))
            elif i == 3: 
                pantalla.blit(cable.icono, (70,0))
                pantalla.blit(cable.icono_led, (70,0))
                pantalla.blit(cable.icono_letra, (70,0))
            
    #Asignación de cables
    def agregar_cables(self):
        LISTA_COLORES = ["Naranja", "Morado", "Naranja y Morado", "Blanco"]
        for i in range(0,4):
            indice_elegido = randint(0,3)
            self.cables.append(CableComplejo(color=LISTA_COLORES[indice_elegido]))

    #Asignación de la conexión de los cables a A y B
    def conectar_cables(self):
        LISTA_POSICIONES= ["A","B"]
        for cable in self.cables:
            indice_elegido = randint(0,1)
            cable.set_conectado_a(LISTA_POSICIONES[indice_elegido])

    #Asignación LEDs a cables  - False: LED apagado - True: LED encendido 
    def asignacion_LED(self):
        LISTA_ESTADO_LED= [True, False]
        for cable in self.cables:
            indice_elegido = randint(0,1)
            cable.set_estado_LED(LISTA_ESTADO_LED[indice_elegido])

    #Función para cortar un cable
    def cortar_cable(self, CableComplejo: object): 
        CableComplejo.set_estado_cortado()
        self.validacion(CableComplejo)
    
    #Se valida al cortar un cable
    def validacion_cable(self, CableComplejo):
        if CableComplejo.conectado_a == "A":
            if CableComplejo.color == "Naranja y Morado" and CableComplejo.LED: 
                print("Cable cortado con éxito")
            elif CableComplejo.color == "Morado" and CableComplejo.LED:
                print("Cable cortado con éxito")
            elif CableComplejo.color == "Naranja" and CableComplejo.LED == False:
                print("Cable cortado con éxito")
            elif CableComplejo.LED and CableComplejo.color =="Blanco": 
                print("Cable cortado con éxito")
            else: 
                print("Equivocación")
                self.equivocacion()

        elif CableComplejo.conectado_a == "B":
            if CableComplejo.color== "Naranja y Morado" and CableComplejo.LED == False:
                print("Cable cortado con éxito")
            elif CableComplejo.LED and CableComplejo.color== "Blanco":
                print("Cable cortado con éxito")
            elif CableComplejo.color == "Naranja" and CableComplejo.LED == False: 
                print("Cable cortado con éxito")
            else: 
                print("Equivocación")
                self.equivocacion()

        else: print("Error en la asignación de cables")
    
    #Se valida al presionar enviar
    def validacion_final(self):
        for cable in self.cables: 
            if cable.estado == False: 
                if cable.conectado_a == "A":
                    if cable.color== "Naranja y Morado" and cable.LED == False:
                        return "Equivocación"
                        self.equivocacion()
                    elif cable.LED and cable.color== "Blanco":
                        return "Equivocación"
                        self.equivocacion()
                    elif cable.color == "Naranja" and cable.LED == False: 
                        return "Equivocación"
                        self.equivocacion()
                    else: 
                       print("Cable no cortado correcto")
                elif cable.conectado_a == "B":
                    if cable.color== "Naranja y Morado" and cable.LED == False:
                        return "Equivocación"
                        self.equivocacion()
                    elif cable.LED and cable.color== "Blanco":
                        return "Equivocación"
                        self.equivocacion()
                    elif cable.color == "Naranja" and cable.LED == False: 
                        return "Equivocación"
                        self.equivocacion()
                
                    else: 
                        print("Cable no cortado correcto")
        
        print("Modulo desactivado")
        self.estado = True


class ModuloPalabras(Modulo):  #Caso memoria
    #Solo una lista. Hacer lista aleatoria que se agrega con nodos
    def __init__(self, pos: int) -> None:
        super().__init__(pos)
        self.nombre = "Memoria"
        self.numero_monitor:int = 0
        self.lista= None
        self.etapa= 0
        self.opciones=[1,2,3,4]
        self.seleccion=None
        self.seleccion1 = None
        self.seleccion2 = None
        self.seleccion3 = None
        self.seleccion4 = None

    def dibujarFondo(self, pantalla):
        fondo = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Fondos/fondo_memoria.png")
        pantalla.blit(fondo, (0, 0))
    
    def dibujarElementos(self, pantalla):
        pass

    def agregar_lista(self): 
        shuffle(self.opciones)
        self.lista = self.opciones

    #Se ejecuta una vez al principio y luego por validar()
    def pasar_etapa(self): 
        LISTA_MONITOR = [1, 2]
        indice_elegido = randint(0,1)
        self.numero_monitor = LISTA_MONITOR[indice_elegido]
        self.etapa = self.etapa +1
        shuffle(self.opciones)

    def seleccionar(self, posicion: int, opcion: int):
        self.seleccion = Nodo(posicion, opcion)
        self.validar(self.etapa)


    def validar(self, etapa):
        if etapa == 1: 
            if self.numero_monitor == 1: 
                if self.lista[0] == self.seleccion.etiqueta : 
                    print("Correcto, pasó a la etapa 2")
                    self.seleccion1 = self.seleccion
                    self.pasar_etapa()
                    self.seleccionar(int, int)
                else: 
                    print("Equivocación")
                    self.equivocacion()
                    #Validar si se equivoca y le quedan errores, volver a seleccionar
                pass
            elif self.numero_monitor == 2:
                if self.lista[0] == self.seleccion.posicion: 
                    print("Correcto, pasó a la etapa 2")
                    self.seleccion1 = self.seleccion
                    self.pasar_etapa()
                    self.seleccionar(int, int)
                else: 
                    print("Equivocación")
                    self.equivocacion()
                pass
            else: 
                print("Error en el número del monitor")
            
        elif etapa == 2: 
            if self.numero_monitor == 1: 
                if self.seleccion1.etiqueta == self.seleccion.etiqueta : 
                    print("Correcto, pasó a la etapa 3")
                    self.seleccion2 = self.seleccion
                    self.pasar_etapa()
                    self.seleccionar(int, int)
                else: 
                    print("Equivocación")
                    self.equivocacion()
                    #Validar si se equivoca y le quedan errores, volver a seleccionar
                pass
            elif self.numero_monitor == 2:
                if self.lista[2] == self.seleccion.etiqueta: 
                    print("Correcto, pasó a la etapa 3")
                    self.seleccion2 = self.seleccion
                    self.pasar_etapa()
                    self.seleccionar(int, int)
                else: 
                    print("Equivocación")
                    self.equivocacion()
                
            else: 
                print("Error en el número del monitor")

        elif etapa == 3: 
            if self.numero_monitor == 1: 
                if self.lista[3] == self.seleccion.etiqueta : 
                    print("Correcto, pasó a la etapa 4")
                    self.seleccion3 = self.seleccion
                    self.pasar_etapa()
                    self.seleccionar(int, int)
                else: 
                    print("Equivocación")
                    self.equivocacion()
                    #Validar si se equivoca y le quedan errores, volver a seleccionar
                pass
            elif self.numero_monitor == 2:
                if self.seleccion1.posicion == self.seleccion.posicion: 
                    print("Correcto, pasó a la etapa 4")
                    self.seleccion3 = self.seleccion
                    self.pasar_etapa()
                    self.seleccionar(int, int)
                else: 
                    print("Equivocación")
                    self.equivocacion()
                pass
            else: 
                print("Error en el número del monitor")
            
        elif etapa == 4: 
            if self.numero_monitor == 1: 
                if self.seleccion1.posicion == self.seleccion.posicion : 
                    print("Correcto, desactivó el modulo")
                    self.seleccion4 = self.seleccion
                    self.pasar_etapa()
                    
                else: 
                    print("Equivocación")
                    self.equivocacion()
                    #Validar si se equivoca y le quedan errores, volver a seleccionar
                pass
            elif self.numero_monitor == 2:
                if self.lista[2] == self.seleccion.posicion: 
                    print("Correcto, desactivó el modulo")
                    self.seleccion2 = self.seleccion
                    self.pasar_etapa()
                    
                else: 
                    print("Equivocación")
                    self.equivocacion()
                
        else: 
            print("Error en la asignación de etapas")
    
    
    
class ModuloCodigo(Modulo):
    i1 = 0; i2 = 0;  i3 = 0;  i4 = 0; i5 = 0 
    def __init__(self, codigo:str, pos:int) -> None:
        super().__init__(pos)
        self.nombre = "Código"
        self.codigo = codigo
        self.casilla1 = None
        self.casilla2 = None 
        self.casilla3 = None 
        self.casilla4 = None
        self.casilla5 = None 
        self.posicion1 = []
        self.posicion2 = []
        self.posicion3 = []
        self.posicion4 = []
        self.posicion5 = []
        self.font = pygame.font.Font("Laboratorio-3-Estructura/src/font/Pixeled.ttf", 12)

    def dibujarFondo(self, pantalla):
        fondo = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Fondos/fondo_codigo.png")
        pantalla.blit(fondo, (0, 0))
    
    def dibujarElementos(self, pantalla): 
        letra1 = self.font.render(self.casilla1.letra, True, (0,0,0))
        letra2 = self.font.render(self.casilla2.letra, True, (0,0,0))
        letra3 = self.font.render(self.casilla3.letra, True, (0,0,0))
        letra4 = self.font.render(self.casilla4.letra, True, (0,0,0))
        letra5 = self.font.render(self.casilla5.letra, True, (0,0,0))
        pantalla.blit(letra1, (47,80))
        pantalla.blit(letra2, (72,80))
        pantalla.blit(letra3, (96,80))
        pantalla.blit(letra4, (121,80))
        pantalla.blit(letra5, (147,80))
    def set_casillas_inicial(self):
        LISTA_LETRAS= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P","Q",
                       "R", "S", "T", "U", "V", "X", "Y","Z"]
    
        self.posicion1.append(Casilla(self.codigo[0]))
        self.posicion2.append(Casilla(self.codigo[1]))
        self.posicion3.append(Casilla(self.codigo[2]))
        self.posicion4.append(Casilla(self.codigo[3]))
        self.posicion5.append(Casilla(self.codigo[4]))

        for i in range(0,6):
            letra = LISTA_LETRAS[randint(0, 24)]
            while(letra == self.codigo[0]):
                letra = LISTA_LETRAS[randint(0, 24)]
            self.posicion1.append(Casilla(letra))
            letra = LISTA_LETRAS[randint(0, 24)]
            while(letra == self.codigo[1]):
                letra = LISTA_LETRAS[randint(0, 24)]
            self.posicion2.append(Casilla(letra))
            letra = LISTA_LETRAS[randint(0, 24)]
            while(letra == self.codigo[2]):
                letra = LISTA_LETRAS[randint(0, 24)]
            self.posicion3.append(Casilla(letra))
            letra = LISTA_LETRAS[randint(0, 24)]
            while(letra == self.codigo[3]):
                letra = LISTA_LETRAS[randint(0, 24)]
            self.posicion4.append(Casilla(letra))
            letra = LISTA_LETRAS[randint(0, 24)]
            while(letra == self.codigo[4]):
                letra = LISTA_LETRAS[randint(0, 24)]
            self.posicion5.append(Casilla(letra))
        
        shuffle(self.posicion1)
        shuffle(self.posicion2)
        shuffle(self.posicion3)
        shuffle(self.posicion4)
        shuffle(self.posicion5)

        self.casilla1 = self.posicion1[0]
        self.casilla2 = self.posicion2[0] 
        self.casilla3 = self.posicion3[0] 
        self.casilla4 = self.posicion4[0]
        self.casilla5 = self.posicion5[0]

    def siguiente_posicion(self, columna:int, i1, i2, i3, i4, i5):
        if columna == 1: 
            if self.casilla1.letra == self.posicion1[-1].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla1.letra = self.posicion1[i1+1]
                i1+=1
        if columna == 2: 
            if self.casilla2.letra == self.posicion2[-1].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla2.letra = self.posicion2[i2+1]
                i2+=1
        if columna == 3: 
            if self.casilla3.letra == self.posicion3[-1].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla3.letra = self.posicion3[i3+1]
                i3+=1
        if columna == 4: 
            if self.casilla4.letra == self.posicion4[-1].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla4.letra = self.posicion4[i4+1]
                i4+=1
        if columna == 5: 
            if self.casilla5.letra == self.posicion5[-1].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla5.letra = self.posicion5[i5+1]
                i5+=1
    
    def anterior_posicion(self, columna:int, i1, i2, i3, i4, i5):
        if columna == 1: 
            if self.casilla1.letra == self.posicion1[0].letra: 
                return "Primera letra alcanzada"
            else: 
                self.casilla1.letra = self.posicion1[i1-1]
                i1-=1
        if columna == 2: 
            if self.casilla2.letra == self.posicion2[0].letra: 
                return "Primera letra alcanzada"
            else: 
                self.casilla2.letra = self.posicion2[i2-1]
                i2-=1
        if columna == 3: 
            if self.casilla3.letra == self.posicion3[0].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla3.letra = self.posicion3[i3-1]
                i3-=1
        if columna == 4: 
            if self.casilla4.letra == self.posicion4[0].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla4.letra = self.posicion4[i4-1]
                i4-=1
        if columna == 5: 
            if self.casilla5.letra == self.posicion5[0].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla5.letra = self.posicion5[i5-1]
                i5-=1

    def validar(self):
        if (self.casilla1 == self.codigo[0] and self.casilla2 == self.codigo[1] and self.casilla3 == self.codigo[2]
            and self.casilla4 == self.codigo[3] and self.casilla5 == self.codigo[4]): 
            print("Módulo resuelto")
            self.estado = True 

        else: 
            print("Equivocación")
            self.equivocacion()


class ModuloExigente(Modulo):
    def __init__(self, pos:int) -> None:
        super().__init__(pos)
        self.nombre = "Exigente"
        self.estado=False
        self.enunciados = ["", "", "", "", ""]
        self.enunciado = None
        self.opciones = ["S", "N"]
        self.tiempo_restante = 20
        self.tiempo_intermedio = 45
        self.hilo_temporizador = None
        self.hilo_reposo = None
    
    def dibujarFondo(self, pantalla):
        fondo = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Fondos/fondo_exigente.png")
        pantalla.blit(fondo, (0, 0))

    def activar(self):
        self.estado=True
        self.hilo_temporizador = threading.Thread(target=self._temporizador)
        self.hilo_temporizador.start
    
    def activar_intermedio(self): 
        self.hilo_reposo = threading.Thread(target=self._temporizador)
        self.hilo_reposo.start

    def seleccionar_enunciado(self):
        indice_elegido = randint(0, len(self.enunciados)-1)
        self.enunciado = self.enunciados[indice_elegido]
        print(self.enunciado)

    #!Revisar la desactivación
    def desactivar(self):
        self.estado=False
        if self.hilo_temporizador:
            self.hilo_temporizador.join()
            self.tiempo_restante = 20

    def _iniciar_tiempo(self):
        while self.tiempo_restante > 0:
            print("Tiempo restante:", self.tiempo_restante, "segundos")
            time.sleep(1)
            self.tiempo_restante -= 1
        print("Tiempo finalizado")
        return "La bomba ha explotado"
    
    def _iniciar_intermedio(self):
        self.activar_intermedio()
        while self.tiempo_intermedio > 0:
            time.sleep(1)
            self.tiempo_restante -= 1
        if self.hilo_reposo:
            self.hilo_reposo.join()
            self.tiempo_intermedio = 40
        self.activar()


    def validar(self, respuesta):
        if self.estado == False: 
            ## Ejemplo
            if respuesta == "S": 
                print("Correcto")
                self.desactivar()
            else: 
                return "La bomba ha explotado"

        

class Cable(ABC):
    def __init__(self) -> None:
        self.estado=False #False: no ha sido cortado


class CableBasico(Cable):
    def __init__(self, color: str) -> None:
        super().__init__()
        self.color = color
    
    def set_estado_cortado(self):
        self.estado=True

class CableRojo(CableBasico): 
    def __init__(self, color, posx, posy) -> None:
        super().__init__(color)
        self.icono_cable = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_rojo.png")
        self.icono_cable_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_rojo_cortado.png")
        self.posx = posx 
        self.posy = posy

class CableBlanco(CableBasico): 
    def __init__(self, color, posx, posy) -> None:
        super().__init__(color)
        self.icono_cable = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_blanco.png")
        self.icono_cable_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_blanco_cortado.png")
        self.posx = posx 
        self.posy = posy

class CableNegro(CableBasico): 
    def __init__(self, color, posx, posy) -> None:
        super().__init__(color)
        self.icono_cable = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_negro.png")
        self.icono_cable_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_negro_cortado.png")
        self.posx = posx 
        self.posy = posy

class CableAzul(CableBasico): 
    def __init__(self, color, posx, posy) -> None:
        super().__init__(color)
        self.icono_cable = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_azul.png")
        self.icono_cable_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Simples/cable_simple_azul_cortado.png")
        self.posx = posx 
        self.posy = posy

class CableComplejo(Cable):
    def __init__(self, color: str) -> None:
        super().__init__()
        self.color= color
        self.conectado_a= None
        self.LED=None
        self.icono = None
        self.icono_cortado = None
        self.icono_led = None
        self.icono_letra = None

        if color == "Naranja":
            self.icono = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_naranja.png")
            self.icono_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_naranja_cortado.png")
        elif color == "Morado": 
            self.icono = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_morado.png")
            self.icono_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_morado_cortado.png")
        elif color == "Naranja y Morado": 
            self.icono = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_naranja_morado.png")
            self.icono_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_naranja_morado_cortado.png")
        elif color == "Blanco": 
            self.icono = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_blanco.png")
            self.icono_cortado = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/cable_complejo_blanco_cortado.png")
        
    def set_estado_cortado(self):
        self.estado=True

    def set_conectado_a(self, conexion):
        self.conectado_a= conexion
        if self.conectado_a == "A": 
            self.icono_letra = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/letra_a.png")
            
        elif self.conectado_a == "B": 
            self.icono_letra = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/letra_b.png")
            

    def set_estado_LED(self, estado: bool):
        self.LED = estado
        if self.LED: 
            self.icono_led = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/led_cables_encendido.png")
        else: 
            self.icono_led = pygame.image.load("Laboratorio-3-Estructura/src/graphics/Modulo Cables Complejos/led_cables_apagado.png")

    
class Casilla: 
    def __init__(self, letra:str) -> None:
        self.letra=letra

class Nodo: 
    def __init__(self, posicion, etiqueta): 
        self.posicion = posicion
        self.etiqueta = etiqueta
