from Jugador import Jugador
from Arbitro import Arbitro
from Persona import Persona

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
