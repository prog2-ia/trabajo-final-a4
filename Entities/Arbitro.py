from Entities.Persona import Persona
from Entities.Jugador import Jugador

class Arbitro(Persona):

    def __init__(self, nombre: str, edad: int, certificacion: str) -> None:
        super().__init__(nombre, edad)
        self.certificacion: str = certificacion
        self.partidas_arbitradas: int = 0

    @staticmethod
    def validar_movimiento(movimiento: str) -> bool:
        """
        Valida si un movimiento cumple el formato esperado.
        En un sistema real aplicaría las reglas concretas de cada juego.

        :param movimiento: Cadena con el movimiento a validar
        :return: True si el movimiento es válido
        """
        if not movimiento or not movimiento.strip():
            raise ValueError("El movimiento no puede estar vacío.")
        # Simulación: cualquier movimiento no vacío se acepta
        return True

    @staticmethod
    def declarar_ganador(jugadores: list) -> Jugador:
        """
        Declara al ganador entre una lista de jugadores según su puntuación.

        :param jugadores: Lista de jugadores participantes
        :return: El jugador con mayor puntuación
        """
        if not jugadores:
            raise ValueError("La lista de jugadores no puede estar vacía.")
        return max(jugadores)
        #return max(jugadores, key=lambda j: j.puntuacion_total)

    def presentarse(self) -> str:
        return (f"Soy {self.nombre}, árbitro certificado en '{self.certificacion}'. "
                f"He arbitrado {self.partidas_arbitradas} partidas.")

    def obtener_rol(self) -> str:
        return "Árbitro"

    def to_dict(self) -> dict:
        """Serializa el árbitro a diccionario."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "certificacion": self.certificacion,
            "partidas_arbitradas": self.partidas_arbitradas,
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Arbitro":
        """Deserializa un diccionario a objeto Arbitro."""
        arbitro = cls(
            nombre=datos["nombre"],
            edad=datos["edad"],
            certificacion=datos["certificacion"]
        )
        # Restauramos el atributo que no va en el constructor
        arbitro.partidas_arbitradas = datos["partidas_arbitradas"]
        return arbitro
