class menu:
    def __init__(self):
        pass

    def ejecutar(self):
        # bucle principal
        while True:
            print('*'*100)
            print('Bienvenido a la liga de juegos de mesa!')
            print('*' * 100)
            print('Introduce tus datos y a lo juego a los que quieras participar')
            print('Para salir pulsa 0')

            opcion = int(input('Selecciona tu opción'))
            if opcion == 1:
                print('Hasta luego!')
                return
            else:
                print('Opción no válida')
