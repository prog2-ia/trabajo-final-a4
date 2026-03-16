from typing import Optional
from Persona import Persona
# Herencia de Persona
class Jugador(Persona):
    def __init__(self,id, nombre, apellido, edad, equipo,puntos: Optional[int] = None):
        super().__init__(id,nombre,apellido,edad)
        self.equipo = equipo
        self.puntos = puntos if puntos is not None and puntos > 0 else 0
        self.juegos = {}
    def mostrar_info(self):
        print(f'Nombre completo: {self.nombre} {self.apellido}, Edad: {self.edad} , Equipo: {self.equipo}')

    def anadir_puntos(self,valor):
        self.equipo += valor if valor > 0 else 0

    def registrar_juego(self, juego):
        if juego not in self.juegos:
            self.juegos[juego] = 1
        else:
            self.juegos[juego] += 1

