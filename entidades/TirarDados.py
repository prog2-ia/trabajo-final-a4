import random
from juego import Juego


class TirarDados(Juego):
    """
    Juego de tirar dados: cada jugador lanza N dados y gana quien saque mayor suma.
    puede humano vs humano y humano vs máquina.
    """

    def __init__(self, num_dados: int = 2, caras: int = 6):
        super().__init__("Tirar Dados", 2, 2)
        self._num_dados = num_dados
        self._caras = caras

    #  Implementación de métodos abstractos
    def obtener_decisiones_posibles(self) -> list:
        # En este juego no hay decisiones del usuario; el "movimiento" es tirar el dado
        return ["tirar"]

    def es_valida_decision(self, decision) -> bool:
        return decision == "tirar"

    def jugar(self, jugador1, jugador2, decision_j1: str = "tirar", decision_j2: str = "tirar"):
        """
        Ambos jugadores tiran los dados.
        Si alguno es máquina, sus dados los lanza el sistema igualmente.
        Devuelve el ganador (Jugador) o None si empate.
        """
        resultado_j1 = self._lanzar()
        resultado_j2 = self._lanzar()

        print(f"\n  {jugador1.get_alias()} sacó: {resultado_j1} (suma: {sum(resultado_j1)})")
        print(f"  {jugador2.get_alias()} sacó: {resultado_j2} (suma: {sum(resultado_j2)})")

        suma1 = sum(resultado_j1)
        suma2 = sum(resultado_j2)

        if suma1 == suma2:
            print("  >> ¡EMPATE!")
            jugador1.sumar_empate()
            jugador2.sumar_empate()
            return None

        ganador = jugador1 if suma1 > suma2 else jugador2
        perdedor = jugador2 if ganador is jugador1 else jugador1
        print(f"  >> ¡{ganador.get_alias()} GANA con {max(suma1, suma2)} puntos!")
        ganador.sumar_victoria()
        perdedor.sumar_derrota()
        self.registrar_resultado(ganador, perdedor)
        return ganador

    #  Lógica interna
    def _lanzar(self) -> list:
        """Lanza los dados y devuelve una lista con cada resultado."""
        return [random.randint(1, self._caras) for _ in range(self._num_dados)]

    def get_num_dados(self):
        return self._num_dados

    def get_caras(self):
        return self._caras

    def __str__(self):
        return f"[{self._nombre}] {self._num_dados} dado(s) de {self._caras} caras"