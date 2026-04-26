from persona import Persona

class Jugador(Persona):
    def __init__(self, id, nombre, apellido, edad, alias):
        super().__init__(id, nombre, apellido, edad)
        self._alias = alias
        self._puntos = 0
        self._partidas_jugadas = 0
        self._partidas_ganadas = 0
        self._partidas_perdidas = 0
        self._es_maquina = False

    # Getters
    def get_alias(self):
        return self._alias

    def get_puntos(self):
        return self._puntos

    def get_partidas_jugadas(self):
        return self._partidas_jugadas

    def get_partidas_ganadas(self):
        return self._partidas_ganadas

    def get_partidas_perdidas(self):
        return self._partidas_perdidas

    def es_maquina(self):
        return self._es_maquina

    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    # Actualización de estadísticas
    def sumar_victoria(self, puntos: int = 3):
        self._partidas_ganadas += 1
        self._partidas_jugadas += 1
        self._puntos += puntos

    def sumar_derrota(self):
        self._partidas_perdidas += 1
        self._partidas_jugadas += 1

    def sumar_empate(self, puntos: int = 1):
        self._partidas_jugadas += 1
        self._puntos += puntos

    def __str__(self):
        return (
            f"{self._alias} | {self.get_nombre_completo()} | "
            f"Puntos: {self._puntos} | "
            f"Partidas Jugadas: {self._partidas_jugadas} Partidas Ganadas: {self._partidas_ganadas} Partidas Perdidas: {self._partidas_perdidas}"
        )
    # Permite sumar los puntos de dos jugadores: jugador1 + jugador2
    def __add__(self, otro):
        if isinstance(otro, Jugador):
            return self._puntos + otro._puntos
        return self._puntos + otro

    # Permite comparar jugadores por puntos: jugador1 > jugador2
    def __gt__(self, otro):
        if isinstance(otro, Jugador):
            return self._puntos > otro._puntos
        return self._puntos > otro

    # Permite comparar jugadores por puntos: jugador1 < jugador2
    def __lt__(self, otro):
        if isinstance(otro, Jugador):
            return self._puntos < otro._puntos
        return self._puntos < otro

    # Permite comparar jugadores por puntos: jugador1 == jugador2
    def __eq__(self, otro):
        if isinstance(otro, Jugador):
            return self._puntos == otro._puntos
        return self._puntos == otro

class JugadorMaquina(Jugador):
    def __init__(self):
        super().__init__(0, "Máquina", "IA", 0, "CPU")
        self._es_maquina = True

    def mostrar_info(self):
        print("[CPU] Jugador controlado por la máquina")

    def __str__(self):
        return f"[CPU] {self._alias}"

