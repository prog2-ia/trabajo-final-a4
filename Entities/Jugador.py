from Entities.Persona import Persona

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

    def __ge__(self, otro : "Jugador") -> bool:
        return self.__puntuacion_total >= otro.puntuacion_total

    def to_dict(self) -> dict:
        """Serializa el jugador a diccionario."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "partidas_jugadas": self.partidas_jugadas,
            "victorias": self.victorias,
            "puntuacion_total": self._Jugador__puntuacion_total,  # name mangling
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Jugador":
        """Deserializa un diccionario a objeto Jugador."""
        jugador = cls(
            nombre=datos["nombre"],
            edad=datos["edad"]
        )
        jugador.partidas_jugadas = datos["partidas_jugadas"]
        jugador.victorias = datos["victorias"]
        jugador._Jugador__puntuacion_total = datos["puntuacion_total"]
        return jugador





