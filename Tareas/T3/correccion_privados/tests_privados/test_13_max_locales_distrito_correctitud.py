import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import max_locales_distrito, cargar_datos
from utilidades import Distritos, Locales

class TestMaxLocalesDistritoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne el nombre del distrito con más locales, solo 2 distritos.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=0,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=9,   provincia='Macul',                   region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=8,   provincia='Puente Alto',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=7,   provincia='Perro',                   region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=6,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=5,   provincia='Gato Chico',              region= 'AN'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=4,   provincia='Perro Danes',             region= 'AN'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=3,   provincia='KDA',                     region= 'LOL'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=2,   provincia='Maraton',                 region= 'GR'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=1,   provincia='Nuble',                   region= 'L6'),
        ]

        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 0, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 9, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 8, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 7, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 6, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 5, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 4, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 3, id_votantes= [217, 374, 982]),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= [153, 57]),
        ]
        
        expected_output = ['Distrito Automatizador Privado']

        generador_distrito = (p for p in lista_distritos)
        generador_local = (p for p in lista_locales)
        resultado = max_locales_distrito(generador_distrito ,generador_local)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne el nombre del distrito con más locales, con 3 distritos.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=0,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=9,   provincia='Macul',                   region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=8,   provincia='Puente Alto',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=7,   provincia='Perro',                   region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador',       id_comuna=6,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador',       id_comuna=5,   provincia='Gato Chico',              region= 'AN'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador',       id_comuna=4,   provincia='Perro Danes',             region= 'AN'),
            Distritos(id_distrito=3, nombre='Distrito Playa',               id_comuna=3,   provincia='KDA',                     region= 'GR'),
            Distritos(id_distrito=3, nombre='Distrito Playa',               id_comuna=2,   provincia='Maraton',                 region= 'GR'),
            Distritos(id_distrito=3, nombre='Distrito Playa',               id_comuna=1,   provincia='Nuble',                   region= 'GR'),
        ]

        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 0, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 9, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 8, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 7, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 6, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 5, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 4, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 3, id_votantes= [217, 374, 982]),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= [153, 57]),
        ]
        
        expected_output = ['Distrito Sacacorcho']

        generador_distrito = (p for p in lista_distritos)
        generador_local = (p for p in lista_locales)
        resultado = max_locales_distrito(generador_distrito ,generador_local)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne el nombre del distrito con más locales, con 3 distritos y un empate.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=0,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=9,   provincia='Macul',                   region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=8,   provincia='Puente Alto',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacacorcho',          id_comuna=7,   provincia='Perro',                   region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=6,   provincia='Gato',                    region= 'LOL'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=5,   provincia='Gato Chico',              region= 'LOL'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=4,   provincia='Perro Danes',             region= 'LOL'),
            Distritos(id_distrito=2, nombre='Distrito Automatizador Privado',       id_comuna=3,   provincia='KDA',                     region= 'LOL'),
            Distritos(id_distrito=3, nombre='Distrito Playa',               id_comuna=2,   provincia='Maraton',                 region= 'GR'),
            Distritos(id_distrito=3, nombre='Distrito Playa',               id_comuna=1,   provincia='Nuble',                   region= 'GR'),
        ]

        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 0, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 9, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 8, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 7, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 6, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 5, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 4, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 3, id_votantes= [217, 374, 982]),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= [153, 57]),
        ]
        
        expected_output = ['Distrito Sacacorcho', 'Distrito Automatizador Privado']

        generador_distrito = (p for p in lista_distritos)
        generador_local = (p for p in lista_locales)
        resultado = max_locales_distrito(generador_distrito ,generador_local)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
        
    def test_3(self):
        """
         Verifica que retorne el nombre del distrito con más locales, con 5 distritos y dos empates.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=0,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=10,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito 1',                   id_comuna=9,   provincia='Macul',                   region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito 1',                   id_comuna=8,   provincia='Puente Alto',             region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito 1',                   id_comuna=7,   provincia='Perro',                   region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Automatizador Privado',       id_comuna=6,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=3, nombre='Distrito Automatizador Privado',       id_comuna=11,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=3, nombre='Distrito Automatizador Privado',       id_comuna=5,   provincia='Gato Chico',              region= 'AN'),
            Distritos(id_distrito=4, nombre='Distrito Plano',               id_comuna=4,   provincia='Perro Danes',             region= 'AN'),
            Distritos(id_distrito=4, nombre='Distrito Plano',               id_comuna=3,   provincia='KDA',                     region= 'AN'),
            Distritos(id_distrito=5, nombre='Distrito Playa',               id_comuna=2,   provincia='Maraton',                 region= 'L6'),
            Distritos(id_distrito=5, nombre='Distrito Playa',               id_comuna=1,   provincia='Nuble',                   region= 'L6'),
        ]

        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 0, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 9, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 8, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 7, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 6, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 5, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 4, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 3, id_votantes= [217, 374, 982]),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= [153, 57]),
            Locales(id_local= 10, nombre_local="Local 10" , id_comuna= 10, id_votantes= [153, 57]),
            Locales(id_local= 11, nombre_local="Local 11" , id_comuna= 11, id_votantes= [153, 57]),
        ]
        
        expected_output = ['Distrito 1', 'Distrito Automatizador Privado']

        generador_distrito = (p for p in lista_distritos)
        generador_local = (p for p in lista_locales)
        resultado = max_locales_distrito(generador_distrito ,generador_local)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
      
    def test_4(self):
        """
         Verifica que retorne el nombre del distrito con más locales, Caso mixto, con mas de un local en algunas comunas y un ganador.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=0,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',          id_comuna=10,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito 2',                   id_comuna=9,   provincia='Macul',                   region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito 2',                   id_comuna=8,   provincia='Puente Alto',             region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito 2',                   id_comuna=7,   provincia='Perro',                   region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Automatizador',       id_comuna=6,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=3, nombre='Distrito Automatizador',       id_comuna=11,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=3, nombre='Distrito Automatizador',       id_comuna=5,   provincia='Gato Chico',              region= 'AN'),
            Distritos(id_distrito=4, nombre='Distrito Plano',               id_comuna=4,   provincia='Perro Danes',             region= 'AN'),
            Distritos(id_distrito=4, nombre='Distrito Plano',               id_comuna=3,   provincia='KDA',                     region= 'AN'),
            Distritos(id_distrito=5, nombre='Distrito Chill',               id_comuna=2,   provincia='Maraton',                 region= 'GR'),
        ]

        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 0, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 9, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 8, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 7, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 6, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 5, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 4, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 3, id_votantes= [217, 374, 982]),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 13, nombre_local="Local 13" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 14, nombre_local="Local 14" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 15, nombre_local="Local 15" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 16, nombre_local="Local 16" , id_comuna= 2, id_votantes= [377, 210]),
            Locales(id_local= 10, nombre_local="Local 10" , id_comuna= 10, id_votantes= [153, 57]),
            Locales(id_local= 11, nombre_local="Local 11" , id_comuna= 11, id_votantes= [153, 57]),
        ]
        
        expected_output = ['Distrito Chill']

        generador_distrito = (p for p in lista_distritos)
        generador_local = (p for p in lista_locales)
        resultado = max_locales_distrito(generador_distrito ,generador_local)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
