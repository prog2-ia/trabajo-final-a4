"""
Menú principal del sistema de Liga de Juegos de Mesa.
Gestión de jugadores, árbitros y juegos.
"""

from Entities.Jugador import Jugador
from Entities.Arbitro import Arbitro
from Entities.Ranking import Liga
from Entities.Dado import Dado
from Games.JuegoDadosCartas import JuegoDadosCarta
from Games.JuegoPiedraPapelTijera import JuegoPiedraPapelTijera
from typing import Optional


class Menu:
    def __init__(self, nombre_liga: str = "Liga de Juegos de Mesa", temporada: int = 1):
        self._liga = Liga(nombre_liga, temporada)
        self._dado = Dado(6)

    def ejecutar(self) -> None:
        while True:
            self._mostrar_encabezado()
            self._mostrar_menu_principal()
            opcion = self._pedir_entero("Selecciona tu opción: ", 0, 6)

            if opcion == 0:
                print("\n¡Hasta luego! Gracias por jugar.\n")
                return
            elif opcion == 1:
                self._submenu_jugadores()
            elif opcion == 2:
                self._submenu_arbitros()
            elif opcion == 3:
                self._ver_clasificacion()
            elif opcion == 4:
                self._jugar_dados_carta()
            elif opcion == 5:
                self._jugar_piedra_papel_tijera()
            elif opcion == 6:
                self._ver_resumen_liga()

    def _mostrar_encabezado(self) -> None:
        print("\n" + "=" * 60)
        print(f" {self._liga.nombre} | Temporada {self._liga.temporada}")
        print("=" * 60)

    def _mostrar_menu_principal(self) -> None:
        print("[1] Gestionar Jugadores")
        print("[2] Gestionar Árbitros")
        print("[3] Ver Clasificación")
        print("[4] Jugar: Dados + Carta")
        print("[5] Jugar: Piedra, Papel, Tijera")
        print("[6] Ver Resumen de Liga")
        print("[0] Salir")

    # ==================== JUGADORES ====================
    def _submenu_jugadores(self) -> None:
        while True:
            print("\n--- GESTIÓN DE JUGADORES ---")
            print(f"[1] Inscribir ({len(self._liga.jugadores)})")
            print("[2] Ver todos")
            print("[3] Modificar")
            print("[4] Eliminar")
            print("[0] Volver")
            opcion = self._pedir_entero("Selecciona: ", 0, 4)
            if opcion == 0:
                return
            elif opcion == 1:
                self._registrar_jugador()
            elif opcion == 2:
                self._ver_jugadores()
            elif opcion == 3:
                self._modificar_jugador()
            elif opcion == 4:
                self._eliminar_jugador()

    def _registrar_jugador(self) -> None:
        print("\n--- NUEVO JUGADOR ---")
        nombre = input("  Nombre: ").strip()
        if not nombre:
            print(" El nombre no puede estar vacío.")
            return
        edad = self._pedir_entero("  Edad (1-120): ", 1, 120)
        try:
            jugador = Jugador(nombre, edad)
            self._liga.inscribir_jugador(jugador)
            print(f"\n '{jugador.nombre}' inscrito (ID: {jugador.id})")
        except ValueError as e:
            print(f" Error: {e}")

    def _ver_jugadores(self) -> None:
        if not self._liga.jugadores:
            print("\n No hay jugadores.")
            return
        print("\n--- JUGADORES ---")
        for i, j in enumerate(self._liga.jugadores, 1):
            print(f"  [{i}] {j.nombre} | E:{j.edad} | P:{j.partidas_jugadas} | V:{j.victorias}")

    def _modificar_jugador(self) -> None:
        if not self._liga.jugadores:
            print(" No hay jugadores.")
            return
        jugador = self._seleccionar_jugador("modificar")
        if not jugador:
            return
        print(f"\n--- MODIFICAR: {jugador.nombre} ---")
        print("[1] Nombre")
        print("[2] Edad")
        opcion = self._pedir_entero("Selecciona: ", 0, 2)
        if opcion == 1:
            nuevo = input("  Nuevo nombre: ").strip()
            if nuevo:
                jugador.nombre = nuevo
                print(" Actualizado.")
        elif opcion == 2:
            jugador.edad = self._pedir_entero("  Nueva edad: ", 1, 120)
            print(" Actualizado.")

    def _eliminar_jugador(self) -> None:
        if not self._liga.jugadores:
            print(" No hay jugadores.")
            return
        jugador = self._seleccionar_jugador("eliminar")
        if not jugador:
            return
        self._liga.jugadores.remove(jugador)
        print(f" '{jugador.nombre}' eliminado.")

    # ==================== ÁRBITROS ====================
    def _submenu_arbitros(self) -> None:
        while True:
            print("\n--- GESTIÓN DE ÁRBITROS ---")
            print(f"[1] Registrar ({len(self._liga.arbitros)})")
            print("[2] Ver todos")
            print("[3] Eliminar")
            print("[0] Volver")
            opcion = self._pedir_entero("Selecciona: ", 0, 3)
            if opcion == 0:
                return
            elif opcion == 1:
                self._registrar_arbitro()
            elif opcion == 2:
                self._ver_arbitros()
            elif opcion == 3:
                self._eliminar_arbitro()

    def _registrar_arbitro(self) -> None:
        print("\n--- NUEVO ÁRBITRO ---")
        nombre = input(" Nombre: ").strip()
        if not nombre:
            print(" El nombre no puede estar vacío.")
            return
        edad = self._pedir_entero("  Edad (1-120): ", 1, 120)
        cert = input("  Certificación: ").strip() or "FIDE"
        try:
            arbitro = Arbitro(nombre, edad, cert)
            self._liga.registrar_arbitro(arbitro)
            print(f"\n '{arbitro.nombre}' registrado")
        except ValueError as e:
            print(f" Error: {e}")

    def _ver_arbitros(self) -> None:
        if not self._liga.arbitros:
            print("\n No hay árbitros.")
            return
        print("\n--- ÁRBITROS ---")
        for i, a in enumerate(self._liga.arbitros, 1):
            print(f"  [{i}] {a.nombre} | E:{a.edad} | Cert:{a.certificacion}")

    def _eliminar_arbitro(self) -> None:
        if not self._liga.arbitros:
            print(" No hay árbitros.")
            return
        arbitro = self._seleccionar_arbitro()
        if not arbitro:
            return
        self._liga.arbitros.remove(arbitro)
        print(f" '{arbitro.nombre}' eliminado.")

    # ==================== CLASIFICACIÓN ====================
    def _ver_clasificacion(self) -> None:
        if not self._liga.jugadores:
            print("\n No hay jugadores.")
            return
        ranking = self._liga.obtener_clasificacion()
        print("\n--- CLASIFICACIÓN ---")
        for pos, (pts, j) in enumerate(ranking, 1):
            print(f"  [{pos}] {j.nombre} | {pts:.1f} pts | {j.porcentaje_victorias:.1f}% wins")
        print(f"\n Líder: {self._liga.clasificacion.obtener_lider().nombre}")

    # ==================== JUEGOS ====================
    def _jugar_dados_carta(self) -> None:
        if len(self._liga.jugadores) < 2:
            print(" Se necesitan 2 jugadores.")
            return
        print("\n--- DADOS + CARTA ---")
        j1 = self._seleccionar_jugador("jugador 1")
        if not j1:
            return
        disponibles = [j for j in self._liga.jugadores if j != j1]
        if not disponibles:
            print(" No hay segundo jugador.")
            return
        print("  Selecciona jugador 2:")
        for i, j in enumerate(disponibles, 1):
            print(f"    [{i}] {j.nombre}")
        idx = self._pedir_entero("  Número: ", 1, len(disponibles))
        j2 = disponibles[idx - 1]

        juego = JuegoDadosCarta()
        _, _, p1 = juego.turno(j1)
        _, _, p2 = juego.turno(j2)

        print(f"\n  {j1.nombre}: {p1} vs {j2.nombre}: {p2}")
        if p1 > p2:
            print(f"\n GANADOR: {j1.nombre}")
            j1.actualizar_estadisticas(10, True)
            j2.actualizar_estadisticas(5, False)
        elif p2 > p1:
            print(f"\n GANADOR: {j2.nombre}")
            j2.actualizar_estadisticas(10, True)
            j1.actualizar_estadisticas(5, False)
        else:
            print("\n EMPATE")
            j1.actualizar_estadisticas(3, False)
            j2.actualizar_estadisticas(3, False)

    def _jugar_piedra_papel_tijera(self) -> None:
        if len(self._liga.jugadores) < 2:
            print(" Se necesitan 2 jugadores.")
            return
        print("\n--- PIEDRA, PAPEL, TIJERA ---")
        j1 = self._seleccionar_jugador("jugador 1")
        if not j1:
            return
        disponibles = [j for j in self._liga.jugadores if j != j1]
        if not disponibles:
            print(" No hay segundo jugador.")
            return
        print("  Selecciona jugador 2:")
        for i, j in enumerate(disponibles, 1):
            print(f"    [{i}] {j.nombre}")
        idx = self._pedir_entero("  Número: ", 1, len(disponibles))
        j2 = disponibles[idx - 1]

        juego = JuegoPiedraPapelTijera()
        op1 = juego.pedir_opcion(j1.nombre)
        op2 = juego.pedir_opcion(j2.nombre)

        print(f"\n  {j1.nombre}: {op1} vs {j2.nombre}: {op2}")
        resultado = juego.calcular_ganador(op1, op2)

        if resultado == 1:
            print(f"\n GANADOR: {j1.nombre}")
            j1.actualizar_estadisticas(10, True)
            j2.actualizar_estadisticas(5, False)
        elif resultado == 2:
            print(f"\n GANADOR: {j2.nombre}")
            j2.actualizar_estadisticas(10, True)
            j1.actualizar_estadisticas(5, False)
        else:
            print("\n EMPATE")
            j1.actualizar_estadisticas(3, False)
            j2.actualizar_estadisticas(3, False)

    def _ver_resumen_liga(self) -> None:
        print("\n" + self._liga.resumen())

    # ==================== UTILIDADES ====================
    def _seleccionar_jugador(self, etiqueta: str) -> Optional[Jugador]:
        disponibles = self._liga.jugadores
        if not disponibles:
            return None
        print(f"\n  {etiqueta}:")
        for i, j in enumerate(disponibles, 1):
            print(f"    [{i}] {j.nombre}")
        idx = self._pedir_entero("  Número: ", 1, len(disponibles))
        return disponibles[idx - 1]

    def _seleccionar_arbitro(self):
        disponibles = self._liga.arbitros
        if not disponibles:
            return None
        print(f"\n  Selecciona:")
        for i, a in enumerate(disponibles, 1):
            print(f"    [{i}] {a.nombre}")
        idx = self._pedir_entero("  Número: ", 1, len(disponibles))
        return disponibles[idx - 1]

    def _pedir_entero(self, mensaje: str, minimo: int, maximo: int) -> int:
        while True:
            try:
                valor = int(input(mensaje))
                if minimo <= valor <= maximo:
                    return valor
                print(f"  Entre {minimo} y {maximo}.")
            except ValueError:
                print(" Inválido.")


if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()

