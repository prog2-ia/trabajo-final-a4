class Juego:
    def __init__(self, nombre, reglas, puntos):
        self.nombre = nombre
        self.reglas = reglas
        self.puntos = puntos
        self.registro_jugadores = {}

    def mostrar_info(self):
        print('Nombre del juego: ', self.nombre)
        print('Reglas del juego: ', self.reglas)
        print(f'Este juego da {self.puntos} puntos\n !Suerte¡')

    def registrar_participacion(self, persona):
        nombre = persona.nombre

        if nombre not in self.registro_jugadores:
            self.registro_jugadores[nombre] = 1
        else:
            self.registro_jugadores[nombre] += 1

    def resetear_registro(self):
        self.registro_jugadores = {}

    def puntos_totales_jugador(self):
        top_jugador = None
        max_veces = 0
        for jugador, veces in self.registro_jugadores.items():
            if veces > max_veces:
                max_veces = veces
                top_jugador = jugador
        return f'El jugador con más puntos de este juego es {top_jugador}'
