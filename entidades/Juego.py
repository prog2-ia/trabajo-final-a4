from abc import ABC, abstractmethod


class Juego(ABC):
    """Clase abstracta que representa un juego de mesa."""

    def __init__(self, nombre: str, min_jugadores: int, max_jugadores: int):
        self.nombre = nombre
        self._min_jugadores = min_jugadores
        self._max_jugadores = max_jugadores
        self._historial = []  # lista de tuplas (ganador, perdedor)

    # Getters
    def get_min_jugadores(self):
        return self._min_jugadores

    def get_max_jugadores(self):
        return self._max_jugadores

    def get_historial(self):
        return list(self._historial)

    # Métodos abstractos
    @abstractmethod
    def jugar(self, jugador1, jugador2):
        """
        Ejecuta una partida entre jugador1 y jugador2.
        Devuelve el objeto Jugador ganador (o None en caso de empate).
        Recibe las decisiones ya tomadas como parámetros, sin usar input().
        """
        pass

    @abstractmethod
    def es_valida_decision(self, decision) -> bool:
        """Comprueba si una decisión/movimiento es válido para este juego."""
        pass

    @abstractmethod
    def obtener_decisiones_posibles(self) -> list:
        """Devuelve la lista de decisiones posibles para mostrar en el menú."""
        pass

    # ── Métodos comunes ───────────────────────────────────────
    def registrar_resultado(self, ganador, perdedor):
        """Guarda el resultado en el historial interno del juego."""
        self._historial.append((ganador, perdedor))

    def __str__(self):
        return f"Juego: {self._nombre} ({self._min_jugadores}-{self._max_jugadores} jugadores)"