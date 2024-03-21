from collections import deque, namedtuple
from typing import List


Cancion = namedtuple('Cancion', ['nombre', 'artista'])


class DCCancionero:
    def __init__(self) -> None:
        self.canciones = list()
        self.cola = deque()
        self.playlists = {}
        self.historial = list()

    def cargar_canciones(self) -> None:
        with open('canciones.dat') as archivo:
            self.canciones = [Cancion(*linea.strip().split(',')) for linea in archivo]

    def agregar_a_la_cola(self, *args) -> None:
        if len(args) == 0:
            self.cola.append(historial[])
        elif len(args) == 1:
            self.cola.add(args[0])

    def escuchar_siguiente_cancion(self) -> None:
        siguiente = self.cola.popleft()
        print(f'Escuchando {siguiente.nombre} de {siguiente.arista}')
    
    def crear_playlist(self, nombre: str, canciones: List[Cancion]=None) -> None:
        self.playlists[nombre] = {}
        playlist = self.playlists[nombre]
        for cancion in canciones:
            playlist.add(cancion)
        print(f'Playlist "{nombre}" creada correctamente con {len(playlist)} cancion(es).')

    def escuchar_playlist(self, nombre: str) -> None:
        pass

    def agregar_a_playlist(self, nombre_playlist: str, cancion: Cancion) -> None:
        pass


if __name__ == '__main__':
    cancionero = DCCancionero()
    cancionero.cargar_canciones()
    print(cancionero.canciones)