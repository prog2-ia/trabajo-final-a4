from Persona import Persona
class Ranking(Persona):
    def __init__(self, nombre, apellido, equipo,puesto):
        super().__init__(self,nombre,apellido,equipo)
        self.puesto = puesto

    def mostrar_posicion(self):
        print(f'Este jugadir está en el puesto {self.puesto}')

