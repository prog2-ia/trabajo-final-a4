from Arbitro import Arbitro
from Jugador import Jugador
from typing import Union

class Partida:
    # Estados posibles de una partida
    ESTADOS: tuple[str, ...] = ("pendiente", "en_curso", "finalizada")

    def __init__(self, juego: str, arbitro: Arbitro) -> None:
        self.juego: str = juego
        self.arbitro: Arbitro = arbitro
        self.__estado: str = "pendiente"   # Privado: se controla con métodos
        self.jugadores: list[Jugador] = []
        self.ganador: Union[Jugador, None] = None

    @property
    def estado(self) -> str:
        return self.__estado

    def añadir_jugador(self, jugador: Jugador) -> None:
        """
        Añade un jugador a la partida si aún no ha comenzado.

        :raises RuntimeError: Si la partida ya está en curso o finalizada
        :raises ValueError: Si el jugador ya estaba añadido
        """
        if self.__estado != "pendiente":
            raise RuntimeError("No se pueden añadir jugadores una vez iniciada la partida.")
        if jugador in self.jugadores:
            raise ValueError(f"{jugador.nombre} ya está en esta partida.")
        self.jugadores.append(jugador)

    def iniciar(self) -> None:
        """
        Cambia el estado a 'en_curso'.

        :raises RuntimeError: Si no hay al menos 2 jugadores
        """
        if len(self.jugadores) < 2:
            raise RuntimeError("Se necesitan al menos 2 jugadores para iniciar la partida.")
        self.__estado = "en_curso"
        self.arbitro.partidas_arbitradas += 1

    def finalizar(self, puntuaciones: dict[Jugador, float]) -> None:
        """
        Finaliza la partida, registra puntuaciones y declara ganador.

        :param puntuaciones: Diccionario {jugador: puntos_obtenidos}
        :raises RuntimeError: Si la partida no está en curso
        """
        if self.__estado != "en_curso":
            raise RuntimeError("Solo se puede finalizar una partida que esté en curso.")

        for jugador, puntos in puntuaciones.items():
            victoria = (puntos == max(puntuaciones.values()))
            jugador.actualizar_estadisticas(puntos, victoria)

        self.ganador = self.arbitro.declarar_ganador(self.jugadores)
        self.__estado = "finalizada"

    def __str__(self) -> str:
        return (f"Partida de {self.juego} | Estado: {self.__estado} | "
                f"Jugadores: {len(self.jugadores)} | "
                f"Ganador: {self.ganador.nombre if self.ganador else 'sin determinar'}")