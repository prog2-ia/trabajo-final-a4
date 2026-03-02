from Juego import Juego
class JuegoCOO(Juego):
    def __init__(self,nombre,reglas,puntos,nombreEq,jugadores):
        super().__init__(nombre,reglas,puntos)
        self.jugadores = jugadores # Recibe una lista con los jugadores que participan
        self.nombreEq = nombreEq

    def mostrar_jugadores(self):
        for i in range(len(self.jugadores)):
            print(f'Jugador {i+1}: {self.jugadores[i]}')