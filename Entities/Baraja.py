import random
from Entities.ElementoJuego import ElementoJuego


class Baraja(ElementoJuego):
    """
    Representa una baraja estándar de 52 cartas.
    Permite barajar, robar y gestionar el descarte.
    """

    PALOS: list[str] = ["Picas", "Corazones", "Diamantes", "Tréboles"]
    VALORES: list[str] = ["A", "2", "3", "4", "5", "6", "7",
                          "8", "9", "10", "J", "Q", "K"]

    def __init__(self) -> None:
        super().__init__(nombre="Baraja francesa (52 cartas)")
        # Cartas privadas: la gestión interna no debe exponerse directamente
        self.__cartas: list[str] = [
            f"{v} de {p}" for p in self.PALOS for v in self.VALORES
        ]
        self.__descartadas: list[str] = []

    @property
    def cartas_restantes(self) -> int:
        return len(self.__cartas)

    def barajar(self) -> None:
        random.shuffle(self.__cartas)

    def robar_carta(self) -> str:
        """
        Saca la carta superior del mazo.

        :return: Carta robada como cadena de texto
        :raises IndexError: Si el mazo está vacío
        """
        if not self.__cartas:
            raise IndexError("No quedan cartas en el mazo.")
        carta = self.__cartas.pop()
        self.__descartadas.append(carta)
        return carta

    def reiniciar(self) -> None:
        """Reconstruye el mazo completo y limpia el descarte."""
        self.__cartas = [
            f"{v} de {p}" for p in self.PALOS for v in self.VALORES
        ]
        self.__descartadas = []
        self.en_uso = False

    def obtener_estado(self) -> str:
        return (f"{self.nombre} → {self.cartas_restantes} cartas restantes, "
                f"{len(self.__descartadas)} descartadas")