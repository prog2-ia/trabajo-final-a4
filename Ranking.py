# --- archivo: Ranking.py ---
class Ranking:
    def __init__(self, persona, puesto):
        self.persona = persona  # Aquí guardamos al objeto Jugador/Coach
        self.puesto = puesto

    def mostrar_posicion(self):
        # Accedemos a los datos de la persona a través del objeto guardado
        print(f"El jugador {self.persona.nombre} está en el puesto {self.puesto}")