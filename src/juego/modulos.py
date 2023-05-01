from __future__ import annotations
from abc import ABC
from typing import List
from random import * 

class Modulo(ABC):
    def __init__(self) -> None:
        self.estado= False #False indica que no ha sido resuelto

class ModuloCablesBasicos(Modulo):
    def __init__(self) -> None:
        super().__init__()
        self.cables: List["Cable"]=[]
    
    def agregar_cables(self):
        LISTA_COLORES = ["Rojo", "Azul", "Negro", "Blanco"]
        for i in range(0,3):
            indice_elegido = randint(0,3)
            self.cables.append(CableBasico(color=LISTA_COLORES[indice_elegido]))

    def cortar_cable(self, CableBasico: object): 
        CableBasico.set_estado_cortado()
        self.validacion(CableBasico)
    
    def validacion(self):
        pass 

class ModuloCablesComplejos(Modulo):
    def __init__(self) -> None:
        super().__init__()
        self.cables: List["Cable"]=[]
    
    def agregar_cables(self):
        LISTA_COLORES = ["Naranja", "Morado"]
        for i in range(0,3):
            indice_elegido = randint(0,1)
            self.cables.append(CableComplejo(color=LISTA_COLORES[indice_elegido]))

    def conectar_cables(self):
        LISTA_POSICIONES= ["A","B"]
        for cable in self.cables:
            indice_elegido = randint(0,1)
            cable.set_conectado_a(LISTA_POSICIONES[indice_elegido])

    def cortar_cable(self, CableComplejo: object): 
        CableComplejo.set_estado_cortado()
        self.validacion(CableBasico)
    
    def validacion(self):
        pass 

class ModuloPalabras(Modulo): 
    NODOS=[["Lista enlazada 1"],["Lista enlazada 2"], ["Lista enlazada 3"],["Lista enlazada 4"], ["Lista enlazada 5"], ["Lista enlazada 6"],
                    ["Lista enlazada 7"], ["Lista enlazada 8"], ["Lista enlazada 9"]]
    def __init__(self, id:str, NODOS) -> None:
        super().__init__()
        self.id= id
        self.numero_monitor:int = 0
        self.lista=NODOS[id]
        self.etapa=1
        self.opciones=[1,2,3,4]
        self.seleccion=None
    def validar(self):
        pass
    
    def seleccionar(self, opcion):
        pass

    def avanzar_etapa(self): 
        self.etapa = self.etapa + 1
    
class ModuloCodigo(Modulo):
    i1 = 0; i2 = 0;  i3 = 0;  i4 = 0; i5 = 0 
    def __init__(self, codigo:str) -> None:
        super().__init__()
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

    
    def set_casillas_inicial(self):
        LISTA_LETRAS= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P","Q",
                       "R", "S", "T", "U", "V", "X", "Y","Z"]
    
        self.posicion1.append(Casilla(self.codigo[0]))
        self.posicion2.append(Casilla(self.codigo[1]))
        self.posicion3.append(Casilla(self.codigo[2]))
        self.posicion4.append(Casilla(self.codigo[3]))
        self.posicion5.append(Casilla(self.codigo[4]))

        for i in range(1,4):
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
        
        random.shuffle(self.posicion1)
        random.shuffle(self.posicion2)
        random.shuffle(self.posicion3)
        random.shuffle(self.posicion4)
        random.shuffle(self.posicion5)

        self.casilla1 = self.posicion1[0]
        self.casilla2 = self.posicion2[0] 
        self.casilla3 = self.posicion3[0] 
        self.casilla4 = self.posicion4[0]
        self.casilla5 = self.posicion5[0]

    def siguiente_posicion(self, columna:int, i1, i2, i3, i4, i5):
        if columna == 1: 
            if self.casilla1.letra == self.posicion1[-1]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla1.letra = self.posicion1[i1+1]
                i1+=1
        if columna == 2: 
            if self.casilla2.letra == self.posicion2[-1]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla2.letra = self.posicion2[i2+1]
                i2+=1
        if columna == 3: 
            if self.casilla3.letra == self.posicion3[-1]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla3.letra = self.posicion3[i3+1]
                i3+=1
        if columna == 4: 
            if self.casilla4.letra == self.posicion4[-1]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla4.letra = self.posicion4[i4+1]
                i4+=1
        if columna == 5: 
            if self.casilla5.letra == self.posicion5[-1]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla5.letra = self.posicion5[i5+1]
                i5+=1
    
    def anterior_posicion(self, columna:int, i1, i2, i3, i4, i5):
        if columna == 1: 
            if self.casilla1.letra == self.posicion1[0]: 
                return "Primera letra alcanzada"
            else: 
                self.casilla1.letra = self.posicion1[i1-1]
                i1-=1
        if columna == 2: 
            if self.casilla2.letra == self.posicion2[0]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla2.letra = self.posicion2[i2-1]
                i2-=1
        if columna == 3: 
            if self.casilla3.letra == self.posicion3[0]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla3.letra = self.posicion3[i3-1]
                i3-=1
        if columna == 4: 
            if self.casilla4.letra == self.posicion4[0]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla4.letra = self.posicion4[i4-1]
                i4-=1
        if columna == 5: 
            if self.casilla5.letra == self.posicion5[0]: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla5.letra = self.posicion5[i5-1]
                i5-=1

class ModuloExigente(Modulo):
    def __init__(self) -> None:
        super().__init__()
        self.estado=False
        self.enunciados = ["", "", "", "", ""]
        self.opciones = ["V", "F"]

    def activar(self):
        self.estado=True    

    def desactivar(self):
        self.estado=False

    def preguntar(self):
        indice_elegido = randint(0,10)
        print(self.enunciados[indice_elegido])
        self.validar()
        self.desactivar()

    def validar(self):
        pass

class Cable(ABC):
    def __init__(self) -> None:
        self.estado=False

class CableBasico(Cable):
    def __init__(self, color: str) -> None:
        super().__init__()
        self.color = color
    
    def set_estado_cortado(self):
        self.estado=True

class CableComplejo(Cable):
    def __init__(self, color: str) -> None:
        super().__init__()
        self.color= color
        self.conectado_a= None

    def set_estado_cortado(self):
        self.estado=True
    
    def set_conectado_a(self, conexion):
        self.conectado_a= conexion
    
class Casilla: 
    def __init__(self, letra:str) -> None:
        self.letra=letra