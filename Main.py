"""""
Aplicación	 para	 organizar	 una	 liga	 con	 modalidades	 heredadas	 que	 definen	 reglas	 y
puntuaciones	 específicas;	 la	 sobrecarga	 de	 operadores	 facilita	 combinar	 clasificaciones,
aplicar	desempates	o	comparar	rendimientos	de	jugadores	de	forma	directa;	se	controlarán
excepciones	por	partidas	inválidas,	resultados	contradictorios	o	inscripciones	duplicadas,	y
se	mantendrán	actas	y	tablas	en	texto	junto	a	una	persistencia	binaria	completa	con	pickle
para	conservar	la	competición.
"""

if __name__ == '__main__':
    from Persona import Persona
    from Jugador import Jugador
    from Coach import Coach
    from Juego import Juego
    persona1 = Persona('Antonio','García',20,'Squad')
    persona1.mostrar_info()

