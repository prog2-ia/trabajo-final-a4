from abc import ABC, abstractmethod


class ElementoJuego(ABC):
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.en_uso: bool = False  # Indica si el elemento está en una partida activa

    @abstractmethod
    def reiniciar(self) -> None:
        #Restaura el elemento a su estado inicial.
        pass

    @abstractmethod
    def obtener_estado(self) -> str:
        # Devuelve una descripción del estado actual del elemento.
        pass

    def __str__(self) -> str:
        estado = "en uso" if self.en_uso else "disponible"
        return f"{self.nombre} [{estado}]"

