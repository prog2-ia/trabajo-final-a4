import json
from pathlib import Path
from Entities.Persona import Persona

class PersonaRepoJson:
    def __init__(self, path: Path) -> None:
        self.__path = path

    def guardar(self, entidades: list) -> None:
        """Persiste la lista de objetos en el soporte elegido."""
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in entidades], f, ensure_ascii=False, indent=2)

    def cargar(self) -> list:
        """Carga y devuelve la lista de personas. Devuelve [] si no existe el fichero."""
        try:
            with open(self.__path, encoding="utf-8") as f:
                # Al ser clase abstracta, las hijas implementan su propia carga.
                return json.load(f)
        except FileNotFoundError:
            return []