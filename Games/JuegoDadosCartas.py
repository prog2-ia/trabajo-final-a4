from Entities.Dado import Dado
from Entities.Baraja import Baraja
from Entities.Jugador import Jugador

class JuegoDadosCarta:
    """
    Juego rápido: Dados + Carta.
    Cada jugador tira un dado y roba una carta, la suma de puntos determina el ganador.
    """

    def __init__(self):
        self._dado = Dado(6)
        self._baraja = Baraja()

    def turno(self, jugador: Jugador) -> tuple[int, str, int]:
        """
        Ejecuta el turno de un jugador: tirar dado + roba carta.
        Devuelve: (valor_dado, carta, puntos_totales)
        """
        valor_dado = self._dado.lanzar()
        carta = self._baraja.robar_carta()
        puntos = valor_dado + self._valor_carta(carta)
        return valor_dado, carta, puntos

    def _valor_carta(self, carta: str) -> int:
        """
        Convierte carta a valor numérico.
        1-10 = su valor, J=11, Q=12, K=13
        """
        carta = carta.strip()

        if len(carta) == 1 and carta.isdigit():
            return int(carta)
        if len(carta) == 2 and carta[0].isdigit() and carta[1].isdigit():
            return int(carta)

        valores = {'J': 11, 'Q': 12, 'K': 13}
        if carta[0] in valores:
            return valores[carta[0]]

        return 10

    def obtener_ganador(self, j1: Jugador, j2: Jugador) -> tuple[Jugador | None, int, int]:
        """
        Compara resultados de dos jugadores.
        Devuelve: (ganador, puntos_j1, puntos_j2)
        Si hay empate, devuelve (None, puntos, puntos)
        """
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