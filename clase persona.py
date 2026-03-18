class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
class Jugador(Persona):
    def __init__(self, nombre, apellido, edad):
        Persona.__init__(self, nombre, apellido, edad)
