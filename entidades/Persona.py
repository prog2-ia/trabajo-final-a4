from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, id,nombre, apellido, edad):
        self.__id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def id(self):
        return self.__id
