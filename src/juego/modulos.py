from __future__ import annotations
from abc import ABC
from typing import List
from random import * 

class Modulo(ABC):
    def __init__(self) -> None:
        self.estado= False #False indica que no ha sido resuelto

class ModuloCablesBasicos(Modulo):
    def __init__(self, franja: str) -> None:
        super().__init__()
        self.cables: List["Cable"]=[]
        self.franja = franja

    def agregar_cables(self):
        #Asignación aleatoria del orden de los cables
        LISTA_COLORES = ["Rojo", "Azul", "Negro", "Blanco"]
        random.shuffle(LISTA_COLORES)
        for i in range(0,3):
            self.cables.append(CableBasico(color=LISTA_COLORES[i]))

    def cortar_cable(self, CableBasico: object): 
        #Validación que modulo esté sin desactivar
        if self.estado == False: 
            CableBasico.set_estado_cortado()
            self.validacion(CableBasico)
        else: 
            print ("El modulo ya está desactivado")

    def validacion(self, CableBasico):
        #Comprobación de que el cable cortado sea el correcto luego de  presionar enviar o cortar un cable
        if self.franja == "Amarillo": 
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
                #! TO DO: Enviar equivocación                

        if self.franja == "Rosado":
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
                #! TO DO: Enviar equivocación 

        if self.franja == "Verde":
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
                #! TO DO: Enviar equivocación 

        if self.franja == "Blanco": 
            #!TO DO: Cambiar a cables normales
            if CableComplejo == None: 
                self.estado = True
                print("Modulo desactivado")
            else: 
                print("Equivocación")
                #! TO DO: Enviar equivocación 

class ModuloCablesComplejos(Modulo):
    def __init__(self) -> None:
        super().__init__()
        self.cables: List["Cable"]=[]

    #Asignación de cables
    def agregar_cables(self):
        LISTA_COLORES = ["Naranja", "Morado", "Naranja y Morado", "Blanco"]
        for i in range(0,3):
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
                #!TO DO: Enviar equivocación

        elif CableComplejo.conectado_a == "B":
            if CableComplejo.color== "Naranja y Morado" and CableComplejo.LED == False:
                print("Cable cortado con éxito")
            elif CableComplejo.LED and CableComplejo.color== "Blanco":
                print("Cable cortado con éxito")
            elif CableComplejo.color == "Naranja" and CableComplejo.LED == False: 
                print("Cable cortado con éxito")
            else: 
                print("Equivocación")
                #!TO DO: Enviar equivocación

        else: print("Error en la asignación de cables")
    
    #Se valida al presionar enviar
    def validacion_final(self):
        for cable in self.cables: 
            if cable.estado == False: 
                if cable.conectado_a == "A":
                    if cable.color== "Naranja y Morado" and cable.LED == False:
                        return "Equivocación"
                        #!TO DO: Enviar equivocación
                    elif cable.LED and cable.color== "Blanco":
                        return "Equivocación"
                        #!TO DO: Enviar equivocación
                    elif cable.color == "Naranja" and cable.LED == False: 
                        return "Equivocación"
                        #!TO DO: Enviar equivocación
                    else: 
                       print("Cable no cortado correcto")
                elif cable.conectado_a == "B":
                    if cable.color== "Naranja y Morado" and cable.LED == False:
                        return "Equivocación"
                        #!TO DO: Enviar equivocación
                    elif cable.LED and cable.color== "Blanco":
                        return "Equivocación"
                        #!TO DO: Enviar equivocación
                    elif cable.color == "Naranja" and cable.LED == False: 
                        return "Equivocación"
                        #!TO DO: Enviar equivocación
                
                    else: 
                        print("Cable no cortado correcto")
        
        print("Modulo desactivado")
        self.estado = True


class ModuloPalabras(Modulo):  #Caso memoria
    #Solo una lista. Hacer lista aleatoria que se agrega con nodos
    def __init__(self) -> None:
        super().__init__()
        self.numero_monitor:int = 0
        self.lista= None
        self.etapa= 0
        self.opciones=[1,2,3,4]
        self.seleccion=None
        self.seleccion1 = None
        self.seleccion2 = None
        self.seleccion3 = None
        self.seleccion4 = None

    #Se ejecuta una vez al principio y luego por validar()
    def pasar_etapa(self): 
        LISTA_MONITOR = [1, 2]
        indice_elegido = randint(0,1)
        self.numero_monitor = LISTA_MONITOR[indice_elegido]
        self.etapa = self.etapa +1
        self.agregar_lista() #!Revisar

    
    def agregar_lista(self): 
        random.shuffle(self.opciones)
        self.lista = self.opciones # Esto no debe pasar 

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
                    #! Enviar equivocación
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
                    #! Enviar equivocación
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
                    #! Enviar equivocación
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
                    #! Enviar equivocación
                
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
                    #! Enviar equivocación
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
                    #! Enviar equivocación
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
                    #! Enviar equivocación
                    #Validar si se equivoca y le quedan errores, volver a seleccionar
                pass
            elif self.numero_monitor == 2:
                if self.lista[2] == self.seleccion.posicion: 
                    print("Correcto, desactivó el modulo")
                    self.seleccion2 = self.seleccion
                    self.pasar_etapa()
                    
                else: 
                     print("Equivocación")
                    #! Enviar equivocación
                
        else: 
            print("Error en la asignación de etapas")
    
    
    
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
            if self.casilla1.letra == self.posicion1[-1].letra: 
                return "Ultima letra alcanzada"
            else: 
                self.casilla1.letra = self.posicion1[i1+1] #! Poner.letra
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
            if self.casilla1.letra == self.posicion1[0].letra: #!Mismo error
                return "Primera letra alcanzada"
            else: 
                self.casilla1.letra = self.posicion1[i1-1]
                i1-=1
        if columna == 2: 
            if self.casilla2.letra == self.posicion2[0]: 
                return "Primera letra alcanzada"
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
        self.opciones = ["S", "N"]
        self.timer = "Aquí va el tiempo"

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
        self.estado=False #False: no ha sido cortado

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
        self.LED=None

    def set_estado_cortado(self):
        self.estado=True
    
    def set_conectado_a(self, conexion):
        self.conectado_a= conexion
    
    def set_estado_LED(self, estado: bool):
        self.LED = estado
    
class Casilla: 
    def __init__(self, letra:str) -> None:
        self.letra=letra

class Nodo: 
    def __init__(self, posicion, etiqueta): 
        self.posicion = posicion
        self.etiqueta = etiqueta
