import dcciudad

class RedMetro:
    def __init__(self, red: list, estaciones: list) -> None:
        self.red = red
        self.estaciones = estaciones


    def informacion_red(self) -> list:
        pass

    def agregar_tunel(self, inicio: str, destino: str) -> int:
        pass

    def tapar_tunel(self, inicio: str, destino: str) -> int:
        pass

    def invertir_tunel(self, estacion_1: str, estacion_2: str) -> bool:
        pass

    def nivel_conexiones(self, inicio: str, destino: str) -> str:
        pass

    def rutas_posibles(self, inicio: str, destino: str, p_intermedias: int) -> int:
        pass

    def ciclo_mas_corto(self, estacion: str) -> int:
        pass

    def estaciones_intermedias(self, inicio: str, destino: str) -> list:
        pass

    def estaciones_intermedias_avanzado(self, inicio: str, destino: str) -> list:
        pass

    def cambiar_planos(self, nombre_archivo: str) -> bool:
        pass

    def asegurar_ruta(self, inicio: str, destino: str, p_intermedias: int) -> list:
        pass