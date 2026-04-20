
class JuegoOnline:
    def __init__(self, servidor: str, latencia_max: int):
        self.__servidor = servidor  # Encapsulamiento
        self.__latencia_max = latencia_max

    def verificar_conexion(self):
        print(f"Conectando al servidor {self.__servidor}...")
        print(f"Latencia estable por debajo de {self.__latency_max}ms. ¡Listo!")

    @property
    def servidor(self):
        return self.__servidor
