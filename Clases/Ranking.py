class Ranking:
    def __init__(self, persona, puesto):
        self.persona = persona
        self.puesto = puesto

    def mostrar_posicion(self):
        print(f"El jugador {self.persona.nombre} está en el puesto {self.puesto}")