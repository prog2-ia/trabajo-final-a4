from Persona import Persona
# Herencia de Persona
class Coach(Persona):
    def __init__(self, nombre, apellido, edad, equipo):
        super().__init__(nombre,apellido,edad,equipo)