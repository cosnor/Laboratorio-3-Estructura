## import timer
##import time as time
class Bomba: 
    def __init__(self, tiempo, errores: int, modulos: int) -> None:
        self.tiempo = tiempo
        self.estado = "Activa"
        self.errores_restantes= errores 
        self.numero_modulos= modulos
        self.modulos_restantes= modulos

    def equivocacion(self):
        if self.estado: 
            self.errores_restantes = self.errores_restantes -1
        if self.errores_restantes <= 0:
            self.estado = "Detonada"
    
    def tiempo_agotado(self): 
        if self.tiempo == 0: 
            self.estado = "Detonada"  
    
    def victoria(self): 
        if self.estado: 
            if self.modulos_restantes == 0: 
                self.estado = "Desactivada"


                