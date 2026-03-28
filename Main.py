"""""
Aplicación	 para	 organizar	 una	 liga	 con	 modalidades	 heredadas	 que	 definen	 reglas	 y
puntuaciones	 específicas;	 la	 sobrecarga	 de	 operadores	 facilita	 combinar	 clasificaciones,
aplicar	desempates	o	comparar	rendimientos	de	jugadores	de	forma	directa;	se	controlarán
excepciones	por	partidas	inválidas,	resultados	contradictorios	o	inscripciones	duplicadas,	y
se	mantendrán	actas	y	tablas	en	texto	junto	a	una	persistencia	binaria	completa	con	pickle
para	conservar	la	competición.
"""

if __name__ == '__main__':
    from Clases.Jugador import Jugador
    from Clases.Coach import Coach
    from Clases.Juego import Juego
    persona1 = Jugador('Z207345G','Antonio','García',20,'Squad')
    persona2 = Jugador('J2093423L','Martín','Echegaray',19,'Equipo',10)
    coach1 = Coach('Z23895732F','Alberto','Fernandez',40,'Squad')
    juego1 = Juego('Catan','Domina y expande tu terrotorio!',20)
    juego2 = Juego('Uno','Quedate sin cartas para ganar!',5)
    persona1.mostrar_info()
    persona1.anadir_puntos(20) # Ganó el catan
    persona1.mostrar_info()
    persona2.mostrar_info()
    persona2.anadir_puntos(10) # Ganó dos partidas del uno
    persona2.mostrar_info()
    juego1.registrar_participacion(persona1)
    juego2.registrar_participacion(persona2)
    persona1.registrar_juego('Catan')
    persona2.registrar_juego('Uno')
    persona2.registrar_juego('Uno')
    print(persona2.juegos)
    print(persona1.juegos)
    print(Juego.registro_jugadores)