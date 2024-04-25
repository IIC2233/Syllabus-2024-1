import unittest
from collections import deque
from io import StringIO
from unittest.mock import patch

from main import DCCancionero, Cancion


class VerificarDCCancionero(unittest.TestCase):
    def setUp(self) -> None:
        self.cancionero = DCCancionero()

    def test_cargar_edita_canciones(self) -> None:
        """
        Verifica que cargar_canciones agregue elementos a la lista de canciones
        """
        self.cancionero.cargar_canciones()
        self.assertGreater(len(self.cancionero.canciones), 0)

    def test_cargar_guarda_canciones(self) -> None:
        """
        Verifica que cargar_canciones agregue objetos de tipo cancion
        """
        self.cancionero.cargar_canciones()
        cancion = None if not self.cancionero.canciones else self.cancionero.canciones[-1]
        self.assertIsInstance(cancion, Cancion)

    def test_agregar_edita_cola_sin_historial(self) -> None:
        """
        Verifica que agregar_a_la_cola no agregue nada si no hay historial
        """
        self.cancionero.agregar_a_la_cola()
        self.assertEqual(len(self.cancionero.cola), 0)

    def test_agregar_edita_cola_con_historial(self) -> None:
        """
        Verifica que agregar_a_la_cola agregue el elemento más nuevo historial
        """
        cancion = Cancion('We are number one', 'Stefan Karl Stefansson')
        self.cancionero.historial = [cancion]
        self.cancionero.agregar_a_la_cola()
        self.assertEqual(len(self.cancionero.cola), 1)
        self.assertEqual(self.cancionero.cola[-1], cancion)

    def test_agregar_guarda_canciones(self) -> None:
        """
        Verifica que cargar_canciones guarde la canción que se le entrega
        """
        cancion = Cancion('We are number one', 'Stefan Karl Stefansson')
        self.cancionero.agregar_a_la_cola(cancion)
        self.assertEqual(self.cancionero.cola[-1], cancion)
    
    def test_escuchar_siguiente_cola_vacia(self) -> None:
        """
        Verifica que escuchar_siguiente_cancion no levante una excepción si la cola está vacía
        """
        self.cancionero.escuchar_siguiente_cancion()

    def test_escuchar_siguiente_cola_no_vacia(self) -> None:
        """
        Verifica que escuchar_siguiente_cancion quite el últemo elemento de la cola
        """
        self.cancionero.cola = deque([Cancion('We are number one', 'Stefan Karl Stefansson'),
                                      Cancion('Africa', 'Toto')])
        self.cancionero.escuchar_siguiente_cancion()
        self.assertEqual(self.cancionero.cola, deque([Cancion('Africa', 'Toto')]))

    def test_crear_playlist_vacia(self) -> None:
        """
        Verifica que crear_playlist no levante una excepción para una playlist vacía
        """
        self.cancionero.crear_playlist('vacia')
    
    def test_crear_playlist_llena(self) -> None:
        """
        Verifica que crear_playlist cree la playlist correctamente
        """
        canciones = [Cancion('We are number one', 'Stefan Karl Stefansson'),
                     Cancion('Africa', 'Toto')]
        nombre = 'Epic'
        self.cancionero.crear_playlist(nombre, canciones)
        self.assertEqual(self.cancionero.playlists[nombre], set(canciones))

    def test_escuchar_playlist_inexistente(self) -> None:
        """
        Verifica que escuchar_playlist no levante una excepción para un nombre que no existe
        """
        self.cancionero.playlists = {}
        self.cancionero.escuchar_playlist('Epic')

    def test_escuchar_playlist_real(self) -> None:
        """
        Verifica que escuchar_playlist agruegue las canciones correspondientes a la cola
        """
        nombre = 'Epic'
        canciones = {Cancion('We are number one', 'Stefan Karl Stefansson'),
                     Cancion('Africa', 'Toto')}
        self.cancionero.cola = deque()
        self.cancionero.playlists = {nombre: canciones}

        self.cancionero.escuchar_playlist('Epic')
        self.assertEqual(self.cancionero.cola, deque(canciones))

    def test_agregar_a_playlist_inexistente(self) -> None:
        """
        Verifica que agregar_a_playlist no levante una excepción para un nombre que no existe
        """
        cancion = Cancion('We are number one', 'Stefan Karl Stefansson')
        self.cancionero.playlists = {}
        self.cancionero.agregar_a_playlist('Epic', cancion)

    def test_escuchar_playlist_real(self) -> None:
        """
        Verifica que agregar_a_playlist agruegue la canción correspondiente
        """
        nombre = 'Epic'
        cancion = Cancion('We are number one', 'Stefan Karl Stefansson')
        self.cancionero.playlists = {nombre: {Cancion('Africa', 'Toto')}}

        self.cancionero.agregar_a_playlist(nombre, cancion)
        self.assertTrue(cancion in self.cancionero.playlists[nombre])


if __name__ == "__main__":
    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)