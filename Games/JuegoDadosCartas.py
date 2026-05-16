from Entities.Dado import Dado
from Entities.Baraja import Baraja
from Entities.Jugador import Jugador
from typing import Optional, Tuple


class JuegoDadosCarta:
    # Juego rapido: Dados + Carta.
    # Cada jugador tira un dado y roba una carta, la suma de puntos determina el ganador.

    def __init__(self):
        self._dado = Dado(6)
        self._baraja = Baraja()
    @staticmethod
    def _mostrar_reglas() -> None:
        print("\n--- REGLAS: DADOS + CARTA ---")
        print("  Cada jugador tira un dado (1-6) y roba una carta de la baraja.")
        print("  Los puntos son la suma del dado y el valor de la carta:")
        print("    - Numeros (2-10): su valor")
        print("    - As (A): 10 puntos")
        print("    - J: 11 puntos | Q: 12 puntos | K: 13 puntos")
        print("  Gana quien sume mas puntos. Si empatan, es empate.")
        print("  Puntos: Victoria = 10 | Empate = 3 | Derrota = 5")
        print("-" * 40)

    def turno(self, jugador: Jugador) -> Tuple[int, str, int]:
        # Ejecuta el turno de un jugador: tirar dado + roba carta.
        # Devuelve: (valor_dado, carta, puntos_totales)
        valor_dado = self._dado.lanzar()
        carta = self._baraja.robar_carta()
        puntos = valor_dado + self._valor_carta(carta)
        return valor_dado, carta, puntos

    @staticmethod
    def _valor_carta( carta: str) -> int:
        # Convierte carta a valor numerico
        carta = carta.strip()

        if len(carta) == 1 and carta.isdigit():
            return int(carta)
        if len(carta) == 2 and carta[0].isdigit() and carta[1].isdigit():
            return int(carta)

        valores = {'J': 11, 'Q': 12, 'K': 13}
        if carta[0] in valores:
            return valores[carta[0]]

        return 10

    def obtener_ganador(self, j1: Jugador, j2: Jugador) -> Tuple[Optional[Jugador], int, int]:
        # Compara resultados de dos jugadores.
        # Devuelve: (ganador, puntos_j1, puntos_j2)
        # Si hay empate, devuelve (None, puntos, puntos)
        self._mostrar_reglas()
        _, _, p1 = self.turno(j1)
        self._baraja.reiniciar()
        self._baraja.barajar()
        _, _, p2 = self.turno(j2)

        if p1 > p2:
            return j1, p1, p2
        elif p2 > p1:
            return j2, p1, p2
        else:
            return None, p1, p2