from Jugador import Jugador
from Persona import Persona
# Herencia de Persona
class Coach(Persona):
    """Entrenador de un equipo."""

    def __init__(self,id, nombre: str, apellido: str, edad: int, especialidad: str):
        super().__init__(id, nombre, apellido, edad)
        self._especialidad = especialidad
        self._equipo = None  # referencia al equipo que dirige
        self.__juegos_entrenados = {}

    def get_especialidad(self):
        return self._especialidad

    def get_equipo(self):
        return self._equipo

    def asignar_equipo(self, equipo):
        self._equipo = equipo

    def __str__(self):
        equipo_nombre = self._equipo.get_nombre() if self._equipo else "Sin equipo"
        return f"Coach {self.get_nombre_completo()} | Especialidad: {self._especialidad} | Equipo: {equipo_nombre}"

    def registrar_juego_entrenado(self, juego):
        if juego not in self.__juegos_entrenados:
            self.__juegos_entrenados[juego] = 1
        else:
            self.__juegos_entrenados[juego] += 1
