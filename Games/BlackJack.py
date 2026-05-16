from Entities.Baraja import Baraja
from Entities.Jugador import Jugador


class BlackJack:
    # Juego de Blackjack simplificado: el jugador pide cartas intentando llegar a 21 sin pasarse.
    # El jugador compite contra la banca (automatica).

    def __init__(self):
        self._baraja = Baraja()
        self._baraja.barajar()
    @staticmethod
    def _mostrar_reglas() -> None:
        print("\n--- REGLAS: BLACKJACK ---")
        print("  Objetivo: llegar a 21 puntos sin pasarse.")
        print("  Valores de las cartas:")
        print("    - Numeros (2-10): su valor")
        print("    - J, Q, K: valen 10 puntos")
        print("    - As (A): vale 11, o 1 si te pasas de 21")
        print("  En tu turno puedes pedir carta o plantarte.")
        print("  La banca pide cartas automaticamente hasta llegar a 17.")
        print("  Si te pasas de 21, pierdes aunque la banca tambien se pase.")
        print("  Puntos: Victoria = 10 | Empate = 3 | Derrota = 5")
        print("-" * 40)
    @staticmethod
    def _valor_carta( carta: str) -> int:
        # Extrae el valor numerico de una carta
        parte = carta.split(" de ")[0].strip()
        if parte in ("J", "Q", "K"):
            return 10
        if parte == "A":
            return 11
        return int(parte)

    def _valor_mano(self, mano: list) -> int:
        # Calcula el valor total de una mano, ajustando ases si se pasa de 21
        total = sum(self._valor_carta(c) for c in mano)
        ases = sum(1 for c in mano if c.startswith("A"))
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        return total

    def _mostrar_mano(self, nombre: str, mano: list, ocultar_segunda: bool = False) -> None:
        if ocultar_segunda:
            print(f"  {nombre}: {mano[0]} | [oculta]")
        else:
            print(f"  {nombre}: {', '.join(mano)} => {self._valor_mano(mano)} pts")

    def jugar(self, jugador: Jugador) -> None:
        self._mostrar_reglas()
        self._baraja.reiniciar()
        self._baraja.barajar()

        mano_jugador = [self._baraja.robar_carta(), self._baraja.robar_carta()]
        mano_banca = [self._baraja.robar_carta(), self._baraja.robar_carta()]

        print(f"\n--- BLACKJACK ---")
        self._mostrar_mano("Banca", mano_banca, ocultar_segunda=True)
        self._mostrar_mano(jugador.nombre, mano_jugador)

        while self._valor_mano(mano_jugador) < 21:
            print("\n  [1] Pedir carta")
            print("  [2] Plantarse")
            opcion = input("  Elige: ").strip()
            if opcion == "1":
                carta = self._baraja.robar_carta()
                mano_jugador.append(carta)
                print(f"\n  Carta robada: {carta}")
                self._mostrar_mano(jugador.nombre, mano_jugador)
                if self._valor_mano(mano_jugador) > 21:
                    print(f"\n  Te has pasado de 21.")
                    break
            elif opcion == "2":
                break

        print(f"\n  Banca revela su mano:")
        self._mostrar_mano("Banca", mano_banca)
        while self._valor_mano(mano_banca) < 17:
            carta = self._baraja.robar_carta()
            mano_banca.append(carta)
            print(f"  Banca pide: {carta}")
            self._mostrar_mano("Banca", mano_banca)

        pts_jugador = self._valor_mano(mano_jugador)
        pts_banca = self._valor_mano(mano_banca)

        print(f"\n  Resultado final:")
        print(f"  {jugador.nombre}: {pts_jugador} pts")
        print(f"  Banca: {pts_banca} pts")

        if pts_jugador > 21:
            print(f"\n  DERROTA: te pasaste de 21.")
            jugador.actualizar_estadisticas(5, False)
        elif pts_banca > 21 or pts_jugador > pts_banca:
            print(f"\n  VICTORIA: {jugador.nombre} gana a la banca.")
            jugador.actualizar_estadisticas(10, True)
        elif pts_jugador == pts_banca:
            print(f"\n  EMPATE.")
            jugador.actualizar_estadisticas(3, False)
        else:
            print(f"\n  DERROTA: la banca gana.")
            jugador.actualizar_estadisticas(5, False)