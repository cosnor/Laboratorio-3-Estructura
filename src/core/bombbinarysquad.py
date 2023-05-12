from juego.bomba import Bomba
from juego.modulos import *

class Juego(): 
    def __init__(self) -> None:
        self.bomba = None
        

    def empezar_juego(self, tiempo, errores, modulo): 
        nueva_bomba = Bomba(tiempo, errores, modulo, 1)
        self.bomba =nueva_bomba
        self.bomba.asignar_modulos()

        #Crear observadores
        for modulo in nueva_bomba.modulos:
            modulo.agregar_observador(nueva_bomba)
            modulo.agregar_observador(Juego)

