class Persona:
    def __init__(self, nombre, apellido, edad,equipo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.equipo = equipo

class jugador(Persona):
    def __init__(self, nombre, apellido, edad, equipo):
        super().__init__(nombre,apellido,edad,equipo)

