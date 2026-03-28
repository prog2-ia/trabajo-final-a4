from Persona import Persona
# Herencia de Persona
class Coach(Persona):
    def __init__(self,id, nombre, apellido, edad,equipo):
        super().__init__(id,nombre,apellido,edad)
        self.equipo = equipo
        self.__juegos_entrenados = {}

    def mostrar_info(self):
        print(f'Nombre completo: {self.nombre} {self.apellido}, Edad: {self.edad} , Equipo: {self.equipo}')

    def registrar_juego_entrenado(self, juego):
        if juego not in self.__juegos_entrenados:
            self.__juegos_entrenados[juego] = 1
        else:
            self.__juegos_entrenados[juego] += 1
