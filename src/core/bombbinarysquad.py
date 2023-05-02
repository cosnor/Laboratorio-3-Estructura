from juego.bomba import Bomba

class Juego: 
    def __init__(self) -> None:
        self.registro_bombas = []

    def empezar_juego(self, tiempo, errores, modulo): 
        self.registro_bombas.append(Bomba(tiempo, errores, modulo))
