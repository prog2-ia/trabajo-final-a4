import json
from pathlib import Path
from Entities.Arbitro import Arbitro

class ArbitroRepoJson:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def guardar(self, entidades: list) -> None:
        """Persiste la lista de objetos en el soporte elegido."""
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in entidades], f, ensure_ascii=False, indent=2)

    def cargar(self) -> list:
        """Carga y devuelve la lista de objetos. Devuelve [] si no existe el fichero."""
        try:
            with open(self.__path, encoding="utf-8") as f:
                return [Arbitro.from_dict(d) for d in json.load(f)]
        except FileNotFoundError:
            return []