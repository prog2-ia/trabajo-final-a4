class Juego():
    def __init__(self, nombre, reglas, puntos):
        self.nombre = nombre
        self.reglas = reglas
        self.puntos = puntos

    def mostrar_info(self):
        print('Nombre del juego: ', self.nombre)
        print('Reglas del juego: ', self.reglas)
        print(f'Este juego da {self.puntos} puntos\n !Suerte¡')