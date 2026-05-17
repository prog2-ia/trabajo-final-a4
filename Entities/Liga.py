from Entities.Jugador import Jugador
from Entities.Arbitro import Arbitro
from Entities.Partida import Partida
from Entities.Clasificacion import Clasificacion
from Entities.JugadorArbitro import JugadorArbitro


class Liga:
    """
    Clase principal que gestiona toda la competición:
    jugadores, árbitros, partidas y clasificación.
    """

    def __init__(self, nombre: str, temporada: int) -> None:
        self.nombre: str = nombre

        if temporada < 1:
            raise ValueError("El número de temporada debe ser mayor que 0.")
        self.temporada: int = temporada

        self.jugadores: list[Jugador] = []
        self.arbitros: list[Arbitro] = []
        self.jugadores_arbitros: list[JugadorArbitro] = []
        self.partidas: list[Partida] = []
        self.clasificacion: Clasificacion = Clasificacion()

    def inscribir_jugador(self, jugador: Jugador) -> None:
        """
        Inscribe un jugador en la liga y lo añade a la clasificación.

        :raises ValueError: Si el jugador ya estaba inscrito
        """
        if jugador in self.jugadores:
            raise ValueError(f"{jugador.nombre} ya está inscrito en la liga.")
        self.jugadores.append(jugador)
        self.clasificacion.registrar_jugador(jugador)

    def registrar_arbitro(self, arbitro: Arbitro) -> None:
        """
        Registra un árbitro en la liga.

        :raises ValueError: Si el árbitro ya estaba registrado
        """
        if arbitro in self.arbitros:
            raise ValueError(f"{arbitro.nombre} ya está registrado como árbitro.")
        self.arbitros.append(arbitro)

    def registrar_jugador_arbitro(self, jugador_arbitro: JugadorArbitro) -> None:
        """
        Registra un jugador/árbitro en la liga.

        :raises ValueError: Si ya estaba registrado
        """
        if jugador_arbitro in self.jugadores_arbitros:
            raise ValueError(f"{jugador_arbitro.nombre} ya está registrado como jugador/árbitro.")
        self.jugadores_arbitros.append(jugador_arbitro)
        # También lo inscribimos como jugador y registramos como árbitro
        self.jugadores.append(jugador_arbitro)
        self.arbitros.append(jugador_arbitro)
        self.clasificacion.registrar_jugador(jugador_arbitro)

    def programar_partida(self, juego: str, arbitro: Arbitro) -> Partida:
        """
        Crea y registra una nueva partida pendiente.

        :param juego: Nombre del juego a disputar
        :param arbitro: Árbitro asignado a la partida
        :return: La partida recién creada
        :raises ValueError: Si el árbitro no está registrado en la liga
        """
        if arbitro not in self.arbitros:
            raise ValueError("El árbitro debe estar registrado en la liga antes de arbitrar.")
        partida = Partida(juego, arbitro)
        self.partidas.append(partida)
        return partida

    def obtener_clasificacion(self) -> list[tuple[int, Jugador]]:
        """Devuelve el ranking actualizado de la liga."""
        return self.clasificacion.obtener_ranking()

    def resumen(self) -> str:
        """Genera un resumen del estado actual de la liga."""
        lider = self.clasificacion.obtener_lider()
        return (f"=== {self.nombre} | Temporada {self.temporada} ===\n"
                f"  Jugadores inscritos : {len(self.jugadores)}\n"
                f"  Árbitros registrados: {len(self.arbitros)}\n"
                f"  Partidas totales    : {len(self.partidas)}\n"
                f"  Líder actual        : {lider.nombre if lider else 'sin datos'}")

    def __str__(self) -> str:
        return self.resumen()