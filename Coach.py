from Persona import Persona
# Herencia de Persona
class Coach(Persona):
    def __init__(self,ID, nombre, apellido, edad):
        super().__init__(nombre,apellido,edad)
        self.edad = edad
    def mostrar_info(self):
        print(f'Nombre completo: {self.nombre} {self.apellido}, Edad: {self.edad} , Equipo: {self.equipo}')