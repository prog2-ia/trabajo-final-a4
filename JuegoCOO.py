from Juego import Juego

class JuegoCooperativo(Juego):
    def __init__(self, nombre, reglas, puntos, equipos: dict):
        # Equipos: un diccionario donde la clave es el nombre del equipo y el valor es una lista de objetos Jugador
        super().__init__(nombre, reglas, puntos)
        self.__equipos = equipos

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Modo: Cooperativo por equipos ({len(self.__equipos)} equipos compitiendo)")

    def mostrar_integrantes_equipo(self, nombre_equipo):
        if nombre_equipo in self.__equipos:
            integrantes = ", ".join([j.nombre for j in self.__equipos[nombre_equipo]])
            print(f"Equipo {nombre_equipo}: {integrantes}")


