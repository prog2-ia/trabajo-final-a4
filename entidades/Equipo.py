from typing import List
from Jugador import Jugador

class Equipo:
    def __init__(self, nombre_equipo: str, coach=None):
        self.__nombre_equipo = nombre_equipo
        self.__coach = coach
        self.__integrantes: List[Jugador] = []  # Lista de objetos Jugador

    def añadir_jugador(self, jugador: Jugador):
        if jugador not in self.__integrantes:
            self.__integrantes.append(jugador)
            # Actualizamos el atributo 'equipo' del jugador para que coincida
            jugador.equipo = self.__nombre_equipo
        else:
            print(f"El jugador {jugador.nombre} ya está en el equipo.")

    def mostrar_plantilla(self):
        print(f"\n--- Equipo: {self.__nombre_equipo} ---")
        if self.__coach:
            print(f"Coach: {self.__coach.nombre} {self.__coach.apellido}")
        print("Jugadores:")
        for j in self.__integrantes:
            print(f"- {j.nombre} ({j.puntos} pts)")

    @property
    def nombre(self):
        return self.__nombre_equipo

    @property
    def integrantes(self):
        return self.__integrantes
