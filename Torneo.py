
class Torneo:
    def __init__(self, tipo,organizador,juegos,pais):
        self.tipo = tipo
        self.organizador = organizador
        self.juegos = juegos
        self.pais = pais

    def __str__(self):
        print(f'Torneo del tipo: {self.tipo} cuyo organizador es {self.organizador} y toma lugar en {self.pais} con los juegos {self.juegos}')