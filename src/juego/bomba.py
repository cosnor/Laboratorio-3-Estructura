import time
from random import randint
from modulos import *


class Bomba: 
    def __init__(self, tiempo, errores: int, modulos: int, id: int) -> None:
        self.id = id 
        self.tiempo = tiempo
        self.estado = "Activa"
        self.errores_restantes= errores 
        self.numero_modulos= modulos
        self.modulos_restantes= modulos
        self.modulos = None
        self.linea_tiempo= None

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
    
    def asignar_modulos(self): 
        LISTA_MODULOS = ["Cables simples", "Cables complejos", "Memoria", "Código", "Exigente"]
        LISTA_MODULOS_SELECCIONADOS = []
        if self.modulos is None: 
            for i in range(0, self.numero_modulos - 1):
                indice_elegido = randint(0, 5 - i)
                LISTA_MODULOS_SELECCIONADOS.append(LISTA_MODULOS.pop(indice_elegido))
            
            for modulo in LISTA_MODULOS_SELECCIONADOS: 
                if modulo == "Cables simples": 
                    FRANJAS = ["Amarillo", "Rosado", "Verde", "Blanco"]
                    indice_elegido = randint(0, 3)
                    nuevo_modulo = ModuloCablesBasicos(FRANJAS[indice_elegido])
                    nuevo_modulo.agregar_cables()
                    self.modulos.append(nuevo_modulo)

                elif modulo == "Cables complejos":
                    nuevo_modulo = ModuloCablesComplejos()
                    nuevo_modulo.agregar_cables()
                    nuevo_modulo.conectar_cables()
                    nuevo_modulo.asignacion_LED()
                    self.modulos.append(nuevo_modulo)

                elif modulo == "Memoria":
                    nuevo_modulo = ModuloPalabras()
                    nuevo_modulo.agregar_lista()
                    self.modulos.append(nuevo_modulo)

                elif modulo == "Código":
                    LISTA_CODIGOS = ["ARBOL", "PUNTO", "GRAFO", "PILAS", "COLAS", 
                                     "LISTA", "NODOS", "CELDA", "DOBLE", "DATOS",
                                     "ORDEN", "TABLA", "CAMPO", "INDEX", "FILAS", 
                                     "GRUPO", "ERROR", "TEXTO", "BYTES", "VISTA",
                                     "AYUDA", "CLASE", "FILES", "EXCEL", "CICLO",
                                     "TEMAS", "NOTAS", "CREAR", "POINT", "ANTES",
                                     "TUPLA", "ARRAY", "BOMBA", "LINEA", "RUTAS"]
                    indice_elegido = randint(0, 34)
                    nuevo_modulo = ModuloCodigo(LISTA_CODIGOS[indice_elegido])
                    nuevo_modulo.set_casillas_inicial()
                    self.modulos.append(nuevo_modulo)

                elif modulo == "Exigente":
                    nuevo_modulo = ModuloExigente()
                    self.modulos.append(nuevo_modulo)
                    #! Hacer métodos de asignaciones y revisarlos



                