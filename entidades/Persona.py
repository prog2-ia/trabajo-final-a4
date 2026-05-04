from abc import ABC, abstractmethod
import random


class Persona(ABC):
    """
    Clase abstracta que representa a cualquier persona del sistema.
    Sirve como base para Jugador y Arbitro.
    """

    def __init__(self, nombre: str, edad: int) -> None:
        # Atributo privado: el id no debería modificarse desde fuera
        self.__id: int = random.randint(1000, 9999)
        self.nombre: str = nombre

        # Validación simple: la edad debe ser positiva
        if edad <= 0:
            raise ValueError(f"La edad debe ser un número positivo, se recibió: {edad}")
        self.edad: int = edad

    @property
    def id(self) -> int:
        """Getter del id privado (solo lectura)."""
        return self.__id

    @abstractmethod
    def presentarse(self) -> str:
        pass

    @abstractmethod
    def obtener_rol(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.obtener_rol()} | {self.nombre} (ID: {self.__id})"
