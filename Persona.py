class Persona:
    def __init__(self, nombre, apellido, edad,equipo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.equipo = equipo
    def mostrar_info(self):
        print(f'Nombre completo: {self.nombre} {self.apellido}, Edad: {self.edad} , Equipo: {self.equipo}')