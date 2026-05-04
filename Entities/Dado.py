import random
from ElementoJuego import ElementoJuego


class Dado(ElementoJuego):

    def __init__(self, num_caras: int = 6) -> None:
        super().__init__(nombre=f"Dado D{num_caras}")

        if num_caras < 2:
            raise ValueError("Un dado debe tener al menos 2 caras.")
        self.num_caras: int = num_caras
        self.__valor_actual: int = 1 # Al inicializar

    @property
    def valor_actual(self) -> int:
        # Getter del valor que muestra el dado tras el último lanzamiento.
        return self.__valor_actual

    def lanzar(self) -> int:
        self.__valor_actual = random.randint(1, self.num_caras)
        return self.__valor_actual

    def reiniciar(self) -> None:
        # Resetea el dado a su valor inicial (cara 1).
        self.__valor_actual = 1
        self.en_uso = False

    def obtener_estado(self) -> str:
        return f"{self.nombre} → valor actual: {self.__valor_actual}"