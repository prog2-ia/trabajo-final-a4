from Entities.Dado import Dado
from Entities.Jugador import Jugador


class JuegoApuestaDados:
    # Juego de apuesta con dados: cada jugador apuesta a un numero entre 2 y 12.
    # Se lanzan dos dados. Los puntos dependen de lo cerca que estes del resultado.

    PUNTOS_ACIERTO = 15
    PUNTOS_CERCANO = 8
    PUNTOS_FALLO = 3

    def __init__(self):
        self._dado1 = Dado(6)
        self._dado2 = Dado(6)

    def _mostrar_reglas(self) -> None:
        print("\n--- REGLAS: APUESTA CON DADOS ---")
        print("  Cada jugador apuesta a la suma de dos dados (entre 2 y 12).")
        print("  Segun lo cerca que estes del resultado real, consigues puntos:")
        print(f"    - Acierto exacto (diferencia 0): {self.PUNTOS_ACIERTO} puntos")
        print(f"    - Cerca (diferencia de 1 o 2): {self.PUNTOS_CERCANO} puntos")
        print(f"    - Fallo (diferencia de 3 o mas): {self.PUNTOS_FALLO} puntos")
        print("  Gana quien consiga mas puntos. Si empatan en puntos, es empate.")
        print("-" * 40)
    @staticmethod
    def _pedir_apuesta( nombre: str) -> int:
        # Pide al jugador que apueste a un numero entre 2 y 12
        while True:
            try:
                valor = int(input(f"  {nombre}, apuesta un numero entre 2 y 12: "))
                if 2 <= valor <= 12:
                    return valor
                print("  Debe estar entre 2 y 12.")
            except ValueError:
                print("  Numero invalido.")

    def _calcular_puntos(self, apuesta: int, resultado: int) -> tuple:
        # Devuelve (puntos, mensaje) segun como de cerca estuvo la apuesta
        diferencia = abs(apuesta - resultado)
        if diferencia == 0:
            return self.PUNTOS_ACIERTO, "Acierto exacto"
        elif diferencia <= 2:
            return self.PUNTOS_CERCANO, "Cerca"
        else:
            return self.PUNTOS_FALLO, "Fallo"

    def jugar(self, j1: Jugador, j2: Jugador) -> None:
        self._mostrar_reglas()

        apuesta1 = self._pedir_apuesta(j1.nombre)
        apuesta2 = self._pedir_apuesta(j2.nombre)

        d1 = self._dado1.lanzar()
        d2 = self._dado2.lanzar()
        suma = d1 + d2

        print(f"\n  Dados: {d1} + {d2} = {suma}")

        pts1, msg1 = self._calcular_puntos(apuesta1, suma)
        pts2, msg2 = self._calcular_puntos(apuesta2, suma)

        print(f"\n  {j1.nombre} apostó {apuesta1} => {msg1} ({pts1} pts)")
        print(f"  {j2.nombre} apostó {apuesta2} => {msg2} ({pts2} pts)")

        if pts1 > pts2:
            print(f"\n  GANADOR: {j1.nombre}")
            j1.actualizar_estadisticas(pts1, True)
            j2.actualizar_estadisticas(pts2, False)
        elif pts2 > pts1:
            print(f"\n  GANADOR: {j2.nombre}")
            j2.actualizar_estadisticas(pts2, True)
            j1.actualizar_estadisticas(pts1, False)
        else:
            print(f"\n  EMPATE")
            j1.actualizar_estadisticas(pts1, False)
            j2.actualizar_estadisticas(pts2, False)