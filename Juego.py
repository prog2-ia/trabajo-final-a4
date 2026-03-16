class Juego:
    registro_jugadores = {}
    def __init__(self, nombre, reglas, puntos):
        self.nombre = nombre
        self.reglas = reglas
        self.puntos = puntos


    def mostrar_info(self):
        print('Nombre del juego: ', self.nombre)
        print('Reglas del juego: ', self.reglas)
        print(f'Este juego da {self.puntos} puntos\n !Suerte¡')

    def registrar_participacion(self,persona):
        nombre = persona.nombre
        if nombre not in Juego.registro_jugadores:
            Juego.registro_jugadores[nombre] = 1
        else:
            Juego.registro_jugadores[nombre] += 1

    def resetear_registro(self):
        Juego.registro_jugadores = {}

    def puntos_totales_jugador(self):
        top_jugador = ''
        puntos_max = 0
        for jugador, veces in Juego.registro_jugadores.items():
            if veces > puntos_max:
                puntos_max = veces
                top_jugador = jugador
        return f'El jugador con más puntos de este juego es {top_jugador}'
