from pathlib import Path
from Persistence.ArbitroRepoJson import ArbitroRepoJson
from Persistence.JugadorRepoJson import JugadorRepoJson
from ui.menu import Menu

if __name__ == "__main__":
    BASE = Path(__file__).parent
    menu1 = Menu()
    repo1 = ArbitroRepoJson(BASE / "arbitros.json")
    arbitros = repo1.cargar()

    repo2 = JugadorRepoJson(BASE / "jugadores.json")
    jugadores = repo2.cargar()

    for jugador in jugadores:
        menu1._liga.inscribir_jugador(jugador)

    for arbitro in arbitros:
        menu1._liga.registrar_arbitro(arbitro)

    print(f"{len(jugadores)} jugadores cargados")
    print(f"{len(arbitros)} árbitros cargados")

    menu1.ejecutar()
