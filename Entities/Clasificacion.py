from Entities.Jugador import Jugador
from typing import Union

class Clasificacion:
    """
    Gestiona el ranking de jugadores de la liga ordenado por puntuación.
    """

    def __init__(self) -> None:
        self.__tabla: list[Jugador] = []  # Privado: se accede mediante métodos

    def registrar_jugador(self, jugador: Jugador) -> None:
        """
        Añade un jugador a la clasificación si no está ya registrado.

        :raises ValueError: Si el jugador ya existe en la tabla
        """
        if jugador in self.__tabla:
            raise ValueError(f"{jugador.nombre} ya está registrado en la clasificación.")
        self.__tabla.append(jugador)

    def obtener_ranking(self) -> list[tuple[int, Jugador]]:
        """
        Devuelve la lista ordenada de jugadores con su posición.

        :return: Lista de tuplas (posición, jugador) ordenadas por puntuación
        """
        ordenados = sorted(self.__tabla,
                           key=lambda j: j.puntuacion_total,
                           reverse=True)
        return [(pos + 1, jugador) for pos, jugador in enumerate(ordenados)]

    def obtener_lider(self) -> Union[Jugador, None]:
        # Devuelve el jugador con mayor puntuación o None si está vacía.
        if not self.__tabla:
            return None
        return max(self.__tabla, key=lambda j: j.puntuacion_total)

    def __len__(self) -> int:
        return len(self.__tabla)
