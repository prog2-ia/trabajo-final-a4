from pathlib import Path
import sys
from Persistence.ArbitroRepoJson import ArbitroRepoJson
from Persistence.JugadorRepoJson import JugadorRepoJson
from ui.menu import Menu
# Para que encuentre los módulos del proyecto
sys.path.insert(0, str(Path(__file__).parent.parent))
if __name__ == "__main__":
    BASE = Path(__file__).parent.parent / "Persistence"

    repo1 = ArbitroRepoJson(BASE / "arbitros.json")
    arbitros = repo1.cargar()

    repo2 = JugadorRepoJson(BASE / "jugadores.json")
    jugadores = repo2.cargar()

    print(f"{len(jugadores)} jugadores cargados")
    print(f"{len(arbitros)} árbitros cargados")

    menu = Menu()

    for jugador in jugadores:
        menu._liga.inscribir_jugador(jugador)

    for arbitro in arbitros:
        menu._liga.registrar_arbitro(arbitro)

    menu.ejecutar()