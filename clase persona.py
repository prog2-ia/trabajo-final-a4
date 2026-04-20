class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
class Jugador(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int):
        Persona.__init__(self, nombre, apellido, edad)
