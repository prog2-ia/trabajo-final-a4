from entidades.JuegoCOO import JuegoCooperativo
from entidades.JuegoOnline import JuegoOnline

class TorneoOnline(JuegoCooperativo, JuegoOnline):
    def __init__(self, nombre, reglas, puntos, equipos, servidor, latencia):
        # Inicializamos ambos padres
        JuegoCooperativo.__init__(self, nombre, reglas, puntos, equipos)
        JuegoOnline.__init__(self, servidor, latencia)

    def mostrar_info(self):
        # Esto usa el mostrar_info de JuegoCooperativo y añade lo de Online
        super().mostrar_info()
        print(f"Servidor: {self.servidor} (Online)")



