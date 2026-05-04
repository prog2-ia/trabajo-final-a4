from Entities.Jugador import Jugador
from Entities.Arbitro import Arbitro
from Entities.Persona import Persona

class JugadorArbitro(Jugador, Arbitro):
    """
    Persona que puede actuar tanto como jugador como árbitro.
    Útil en ligas pequeñas donde los roles se solapan.

    Herencia múltiple: resuelve el MRO (Method Resolution Order)
    dando prioridad a Jugador para los métodos compartidos.
    MRO resultante: JugadorArbitro → Jugador → Arbitro → Persona → ABC
    """

    def __init__(self, nombre: str, edad: int, certificacion: str) -> None:
        # Llamamos directamente a Persona para evitar el conflicto del MRO:
        # Jugador.__init__ llamaría a super() que llevaría a Arbitro.__init__,
        # el cual exige 'certificacion' y no lo tiene en ese punto de la cadena.
        Persona.__init__(self, nombre, edad)
        # Atributos propios de Jugador
        self.partidas_jugadas: int = 0
        self.victorias: int = 0
        self._Jugador__puntuacion_total: float = 0.0  # name mangling manual
        # Atributos propios de Árbitro
        self.certificacion: str = certificacion
        self.partidas_arbitradas: int = 0

    def presentarse(self) -> str:
        return (f"Soy {self.nombre}, jugador y árbitro certificado "
                f"en '{self.certificacion}' con {self.partidas_jugadas} partidas jugadas.")

    def obtener_rol(self) -> str:
        return "Jugador/Árbitro"

    def to_dict(self) -> dict:
        """Serializa el jugador/árbitro a diccionario."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "certificacion": self.certificacion,
            "partidas_arbitradas": self.partidas_arbitradas,
            "partidas_jugadas_jugador": self.partidas_jugadas,
            "victorias": self.victorias,
            "puntuacion_total": self._Jugador__puntuacion_total,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "JugadorArbitro":
        """Deserializa un diccionario a objeto JugadorArbitro."""
        ja = cls(
            nombre=datos["nombre"],
            edad=datos["edad"],
            certificacion=datos["certificacion"]
        )
        ja.partidas_arbitradas = datos["partidas_arbitradas"]
        ja.partidas_jugadas = datos["partidas_jugadas_jugador"]
        ja.victorias = datos["victorias"]
        ja._Jugador__puntuacion_total = datos["puntuacion_total"]
        return ja

