from Persona import Persona

class Jugador(Persona):

    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre, edad)
        self.partidas_jugadas: int = 0
        self.victorias: int = 0
        # Atributo privado: la puntuación se controla internamente
        self.__puntuacion_total: float = 0.0

    @property
    def puntuacion_total(self) -> float:
        return self.__puntuacion_total

    @property
    def porcentaje_victorias(self) -> float:
        """Calcula el % de victorias sobre partidas jugadas."""
        if self.partidas_jugadas == 0:
            return 0.0
        return (self.victorias / self.partidas_jugadas) * 100

    def actualizar_estadisticas(self, puntos: float, victoria: bool) -> None:
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos.")
        self.__puntuacion_total += puntos
        self.partidas_jugadas += 1
        if victoria:
            self.victorias += 1

    def presentarse(self) -> str:
        return (f"Soy {self.nombre}, jugador con {self.partidas_jugadas} "
                f"partidas y {self.victorias} victorias.")

    def obtener_rol(self) -> str:
        return "Jugador"

    def __ge__(self, otro : Jugador) -> bool:
        return self.__puntuacion_total >= otro.puntuacion_total




