import time
from random import randint
from juego.modulos import *


class Bomba(Observador): 
    def __init__(self, tiempo, errores: int, modulos: int, id: int) -> None:
        self.id = id 
        self.tiempo = tiempo
        self.estado = "Activa"
        self.errores = errores
        self.equivocaciones= 0 
        self.numero_modulos= modulos
        self.modulos_restantes= modulos
        self.modulos = []
        self.linea_tiempo= None
        self.registro = None

    def notificar_equivocacion(self):
        if self.estado: 
            self.equivocaciones = self.equivocaciones + 1
            print("equivocacion")
        if self.equivocaciones <= self.errores:
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
        POSICIONES = [1, 2, 3, 4, 5]
        POSICIONESSELEC = []
        if self.modulos == []: 
            for i in range(0, self.numero_modulos):
                indice_elegido = randint(0, self.numero_modulos - i-1)
                LISTA_MODULOS_SELECCIONADOS.append(LISTA_MODULOS.pop(indice_elegido))
                
            for i in range(0, self.numero_modulos):
                indice_elegido = randint(0, self.numero_modulos - i-1)
                POSICIONESSELEC.append(POSICIONES.pop(indice_elegido))
            print(LISTA_MODULOS_SELECCIONADOS)

            for modulo in LISTA_MODULOS_SELECCIONADOS: 
                print(modulo)
                if modulo == "Cables simples": 
                    FRANJAS = ["Amarillo", "Rosado", "Verde", "Blanco"]
                    indice_elegido = randint(0, 3)
                    posicion = i
                    nuevo_modulo = ModuloCablesBasicos(FRANJAS[indice_elegido], 1)
                    nuevo_modulo.agregar_cables()
                    self.modulos.append(nuevo_modulo)


                elif modulo == "Cables complejos":
                        nuevo_modulo = ModuloCablesComplejos(4)
                        nuevo_modulo.agregar_cables()
                        nuevo_modulo.conectar_cables()
                        nuevo_modulo.asignacion_LED()
                        self.modulos.append(nuevo_modulo)
                        posicion = i

                elif modulo == "Memoria":
                        nuevo_modulo = ModuloPalabras(4)
                        nuevo_modulo.agregar_lista()
                        self.modulos.append(nuevo_modulo)
                        posicion = i

                elif modulo == "Código":
                        LISTA_CODIGOS = ["ARBOL", "PUNTO", "GRAFO", "PILAS", "COLAS", 
                                        "LISTA", "NODOS", "CELDA", "DOBLE", "DATOS",
                                        "ORDEN", "TABLA", "CAMPO", "INDEX", "FILAS", 
                                        "GRUPO", "ERROR", "TEXTO", "BYTES", "VISTA",
                                        "AYUDA", "CLASE", "FILES", "EXCEL", "CICLO",
                                        "TEMAS", "NOTAS", "CREAR", "POINT", "ANTES",
                                        "TUPLA", "ARRAY", "BOMBA", "LINEA", "RUTAS"]
                        indice_elegido = randint(0, 34)
                        nuevo_modulo = ModuloCodigo(LISTA_CODIGOS[indice_elegido], 3)
                        nuevo_modulo.set_casillas_inicial()
                        self.modulos.append(nuevo_modulo)
                        posicion = i

                elif modulo == "Exigente":
                        nuevo_modulo = ModuloExigente(2)
                        self.modulos.append(nuevo_modulo)
                        posicion = i
                        #! Hacer métodos de asignaciones y revisarlos




                