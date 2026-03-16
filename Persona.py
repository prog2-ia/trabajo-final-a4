from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, id,nombre, apellido, edad):
        self.__id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    @abstractmethod
    def mostrar_info(self):
        pass
        #print(f'Nombre completo: {self.nombre} {self.apellido}, Edad: {self.edad} , Equipo: {self.equipo}')
    @property
    def id(self):
        return self.__id