from typing import Optional
from Persona import Persona
# Herencia de Persona
class Jugador(Persona):
    def __init__(self,id, nombre, apellido, edad, equipo,puntos: Optional[int] = None):
        super().__init__(id,nombre,apellido,edad)
        self.equipo = equipo
        self.puntos = puntos if puntos is not None and puntos > 0 else 0
        self.juegos = {}

    # Metodo especial
    def __str__(self):
        return f"[Jugador #{self.id}] {self.nombre} {self.apellido} | Equipo: {self.equipo} | Puntos: {self.puntos}"
    # Sobrecarga de operadores matemáticos
    # Permite sumar los puntos de dos objetos Jugador
    def __add__(self, otro):
        if isinstance(otro, Jugador):
            return self.puntos + otro.puntos
        return self.puntos + otro
    # Metodo especial (mayor que)
    def __gt__(self, otro):
        if isinstance(otro, Jugador):
            return self.puntos > otro.puntos
        return self.puntos > otro

    def mostrar_info(self):
        print(self.__str__())

    def anadir_puntos(self,valor: int):
        self.puntos += valor if valor > 0 else 0

    def registrar_juego(self, juego):
        if juego not in self.juegos:
            self.juegos[juego] = 1
        else:
            self.juegos[juego] += 1

