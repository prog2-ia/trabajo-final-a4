from Juego import Juego
class PiedraPapelTijera(Juego):
    def __init__(self,nombre,reglas,puntos,jugador1,juagador2=None):
        super().__init__(id, nombre,reglas,puntos)
        self.jugador1 = jugador1
        self.jugador2 = juagador2

    def empate(self):
        # Bucle para seguir jugando o no luego de un empate
        while True:
            opcion = int(input('Habéis empatado. Pulsa 1 para volver a jugar o 0 para salir: '))
            if opcion in (0, 1):
                return opcion
            else:
                print('Opción inválida, vuelve a introducir una opción')
    def gana(self,jugador):
        # Suma de puntos a el jugador que ha ganado, también incluye que la suma se realiza a un jugador válido
        while True:
            print('Comprobación de jugador válido en proceso')
            if jugador in (self.jugador1, self.jugador2):
                print(f'Jugador válido, se te sumarán {self.puntos}, por haber ganado')
                return jugador.puntos + self.puntos
            else:
                print('Este jugador no ha participado en esta partida, porfavor inserta un jugador válido')

    def pierde(self,jugador):
        # Resta de puntos al jugador que ha perdido, incluye la autenticidad del jugador para evitar errores
        while True:
            print('Comprobación de jugador válido en proceso')
            if jugador in (self.jugador1, self.jugador2):
                print(f'Jugador válido, se te restarán {self.puntos} por haber perdido')
                return jugador.puntos - self.puntos
            else:
                print('Este jugador no ha participado en esta partida, porfavor inserta un jugador válido')