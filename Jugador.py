from Persona import Persona
# Herencia de Persona
class Jugador(Persona):
    def __init__(self,ID, nombre, apellido, edad, equipo):
        super().__init__(ID,nombre,apellido,edad)
        self.equipo = equipo
    def mostrar_info(self):
        print(f'Nombre completo: {self.nombre} {self.apellido}, Edad: {self.edad} , Equipo: {self.equipo}')