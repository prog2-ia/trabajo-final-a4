from entidades.Jugador import Jugador, JugadorMaquina
from entidades.PiedraPapelTijera import PiedraPapelTijera
from entidades.TirarDados import TirarDados


class Menu:
    def __init__(self):
        self._jugadores = []
        self._ppt = PiedraPapelTijera()
        self._dados = TirarDados()

    def ejecutar(self):
        # bucle principal
        while True:
            print('*' * 60)
            print('   Bienvenido a la liga de juegos de mesa!')
            print('*' * 60)
            print('[1] Registrar jugador')
            print('[2] Jugar Piedra Papel Tijera')
            print('[3] Jugar Tirar Dados')
            print('[4] Ver jugadores y puntos')
            print('[0] Salir')
            print('*' * 60)

            opcion = self._pedir_entero('Selecciona tu opción: ', 0, 4)

            if opcion == 0:
                print('\n¡Hasta luego!\n')
                return
            elif opcion == 1:
                self._registrar_jugador()
            elif opcion == 2:
                self._menu_piedra_papel_tijera()
            elif opcion == 3:
                self._menu_tirar_dados()
            elif opcion == 4:
                self._ver_jugadores()

    def _registrar_jugador(self):
        print('\n' + '*' * 40)
        print('  Registrar nuevo jugador')
        print('*' * 40)
        id_jugador = len(self._jugadores) + 1
        nombre = input('  Nombre: ').strip()
        apellido = input('  Apellido: ').strip()
        edad = self._pedir_entero('  Edad: ', 1, 120)
        alias = input('  Alias: ').strip()
        jugador = Jugador(id_jugador, nombre, apellido, edad, alias)
        self._jugadores.append(jugador)
        print(f'\n  Jugador "{alias}" registrado correctamente.\n')

    def _pedir_entero(self, mensaje: str, minimo: int, maximo: int) -> int:
        # Pide un entero al usuario y lo valida. Nunca peta con un ValueError.
        while True:
            try:
                valor = int(input(mensaje))
                if minimo <= valor <= maximo:
                    return valor
                print(f' Introduce un número entre {minimo} y {maximo}.')
            except ValueError:
                print(' Eso no es un número válido.')

    def _seleccionar_jugador(self, etiqueta: str, excluir=None) -> Jugador:
        # Muestra la lista de jugadores y devuelve el elegido.
        disponibles = [j for j in self._jugadores if j is not excluir]
        if not disponibles:
            print('  ✗ No hay jugadores disponibles. Registra al menos uno.')
            return None
        print(f'\n  Selecciona {etiqueta}:')
        for i, j in enumerate(disponibles, start=1):
            print(f'    [{i}] {j.get_alias()} — {j.nombre} {j.apellido}')
        idx = self._pedir_entero('  Número: ', 1, len(disponibles))
        return disponibles[idx - 1]

    def _pedir_decision(self, jugador: Jugador, opciones: list) -> str:
        # Muestra las opciones del juego y devuelve la elegida.
        print(f'\n  {jugador.get_alias()}, elige tu jugada:')
        for i, op in enumerate(opciones, start=1):
            print(f'    [{i}] {op.capitalize()}')
        idx = self._pedir_entero('  Tu elección: ', 1, len(opciones))
        return opciones[idx - 1]

