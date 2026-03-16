"""""
from Juego import Juego
class JuegoCooperativo(Juego):
    def __init__(self, nombre, reglas, puntos,personas): # personas es un diccionario con los jugadores y los equipos a los que corresponden
        super().__init__(nombre, reglas,puntos)
        self.personas = personas

"""

