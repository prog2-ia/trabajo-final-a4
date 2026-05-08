from Entities.Dado import Dado
from Entities.Jugador import Jugador


class JuegoPiedraPapelTijera:
    """
    Juego clásico: Piedra, Papel, Tijera.
    Cada jugador elige una opción y se comparan.
    """

    OPCIONES = ['piedra', 'papel', 'tijera']
    NOMBRES = {1: 'piedra', 2: 'papel', 3: 'tijera'}

    def __init__(self):
        self._dado = Dado(3)

    def pedir_opcion(self, jugador: str) -> str:
        print(f"\n{jugador}, elige tu opción:")
        print("  [1] Piedra")
        print("  [2] Papel")
        print("  [3] Tijera")

        while True:
            try:
                opcion = int(input("  Opción (1-3): "))
                if opcion in [1, 2, 3]:
                    return self.NOMBRES[opcion]
                print("  Elige 1, 2 o 3")
            except ValueError:
                print("  Introduce un número")

    def calcular_ganador(self, op1: str, op2: str) -> int:
        if op1 == op2:
            return 0

        if (op1 == 'piedra' and op2 == 'tijera') or \
           (op1 == 'tijera' and op2 == 'papel') or \
           (op1 == 'papel' and op2 == 'piedra'):
            return 1
        return 2

    def jugar(self, j1: Jugador, j2: Jugador):
        op1 = self.pedir_opcion(j1.nombre)
        op2 = self.pedir_opcion(j2.nombre)
        resultado = self.calcular_ganador(op1, op2)
        # Retorna ganador y opciones
        return resultado, op1, op2