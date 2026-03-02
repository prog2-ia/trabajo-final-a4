from Juego import Juego
class JuegoAzar(Juego):
    def __init__(self,nombre,reglas,puntos,azar):
        super().__init__(nombre,reglas,puntos)
        self.azar = azar