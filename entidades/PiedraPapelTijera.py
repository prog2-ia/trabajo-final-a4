import random
from Juego import Juego


class PiedraPapelTijera(Juego):
    """
    Implementación del juego Piedra, Papel o Tijera.
    Partidas humano vs humano y humano vs máquina.
    """

    PIEDRA = "piedra"
    PAPEL = "papel"
    TIJERA = "tijera"
    DECISIONES = [PIEDRA, PAPEL, TIJERA]

    # Diccionario con lógica del juego: clave gana a valor
    _GANA_A = {
        PIEDRA: TIJERA,
        PAPEL: PIEDRA,
        TIJERA: PAPEL,
    }

    def __init__(self):
        super().__init__("Piedra Papel Tijera", 2, 2)

    # Implementación de métodos abstractos
    def obtener_decisiones_posibles(self) -> list:
        return list(self.DECISIONES)

    def es_valida_decision(self, decision) -> bool:
        return isinstance(decision, str) and decision.lower() in self.DECISIONES

    def jugar(self, jugador1, jugador2, decision_j1: str = None, decision_j2: str = None):
        """
        Ejecuta una ronda.
        - Si jugador2 es máquina, decision_j2 se genera automáticamente.
        - Devuelve el ganador (Jugador) o None si hay empate.
        """
        d1 = decision_j1.lower()
        d2 = (
            self.decision_maquina()
            if jugador2.es_maquina()
            else decision_j2.lower()
        )

        print(f"\n  {jugador1.get_alias()} eligió: {d1.upper()}")
        print(f"  {jugador2.get_alias()} eligió: {d2.upper()}")

        ganador = self._resolver(jugador1, jugador2, d1, d2)

        if ganador is None:
            print("¡EMPATE!")
            jugador1.sumar_empate()
            jugador2.sumar_empate()
        else:
            perdedor = jugador2 if ganador is jugador1 else jugador1
            print(f" ¡{ganador.get_alias()} GANA la ronda!")
            ganador.sumar_victoria()
            perdedor.sumar_derrota()
            self.registrar_resultado(ganador, perdedor)

        return ganador

    # Lógica interna
    def _resolver(self, jugador1, jugador2, d1: str, d2: str):
        # Determina quién gana según las decisiones. Devuelve None en empate.
        if d1 == d2:
            return None
        if self._GANA_A[d1] == d2:
            return jugador1
        return jugador2

    def decision_maquina(self) -> str:
        # Genera una decisión aleatoria para la máquina.
        return random.choice(self.DECISIONES)

    def __str__(self):
        return f"[{self._nombre}] Decisiones: {', '.join(self.DECISIONES)}"
        # El .join(self.DECIOSIONES) devuelve el string 'Decisiones: piedra, papel, tijera' lo pasa a string