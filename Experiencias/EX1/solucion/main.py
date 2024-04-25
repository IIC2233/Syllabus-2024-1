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
            if self.historial: 
                self.cola.append(self.historial[-1])
        elif len(args) == 1:
            self.cola.append(args[0])

    def escuchar_siguiente_cancion(self) -> None:
        if len(self.cola) > 0: 
            siguiente = self.cola.popleft() 
            self.historial.append(siguiente)
            print(f'Escuchando "{siguiente.nombre}" de "{siguiente.artista}"')
        else:
            print(f'Para continuar escuchando, debes agregar canciones a la cola')
    
    def crear_playlist(self, nombre: str, canciones: List[Cancion]=None) -> None:
        self.playlists[nombre] = set()
        playlist = self.playlists[nombre]
        if canciones is not None:
            for cancion in canciones:
                playlist.add(cancion)
        print(f'Playlist "{nombre}" creada correctamente con {len(playlist)} cancion(es).')

    def escuchar_playlist(self, nombre: str) -> None:
        if nombre not in self.playlists.keys():
            print(f'Lo sentimos, la playlist "{nombre}" no existe.')
        else:
            playlist = self.playlists[nombre]
            for cancion in playlist:
                self.agregar_a_la_cola(cancion)
            print(f'Playlist "{nombre}" agregada a la cola.\n  Se agregó {len(playlist)} cancion(es).')


    def agregar_a_playlist(self, nombre_playlist: str, cancion: Cancion) -> None:
        if nombre_playlist not in self.playlists.keys():
            print(f'Lo sentimos, la playlist "{nombre_playlist}" no existe.')
        else:
            self.playlists[nombre_playlist].add(cancion)


if __name__ == '__main__':
    cancionero = DCCancionero()
    cancionero.cargar_canciones()
    print(cancionero.canciones)

    cancionero.agregar_a_la_cola()
    cancionero.agregar_a_la_cola(Cancion('Fellas in London', 'Ye'))
    cancionero.escuchar_siguiente_cancion()
    cancionero.crear_playlist('Bangers')
    cancionero.crear_playlist('Top Tier', [Cancion('Might give you up', 'Rick Roller')])
    cancionero.escuchar_playlist('Top Tier')
    cancionero.escuchar_siguiente_cancion()
    cancionero.agregar_a_playlist('Bangers', Cancion('All moon', 'Wash Mouth'))