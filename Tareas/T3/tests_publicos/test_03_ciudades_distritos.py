import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import ciudades_distritos, cargar_datos
from utilidades import Distritos
from test_solution import CIUDADES_DISTRITOS_S, CIUDADES_DISTRITOS_M, CIUDADES_DISTRITOS_L

class TestCiudadesDistritos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne los nombres de las provincias cuando todos tienen distinto nombre.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',      id_comuna=0,   provincia='Providencia',             region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Lapiz',           id_comuna=9,   provincia='Macul',                   region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Goma',            id_comuna=8,   provincia='Puente Alto',             region= 'RM'),
            Distritos(id_distrito=4, nombre='Distrito Corrector',       id_comuna=7,   provincia='Perro',                   region= 'RM'),
            Distritos(id_distrito=5, nombre='Distrito Automatizador',   id_comuna=6,   provincia='Gato',                    region= 'AN'),
            Distritos(id_distrito=6, nombre='Distrito Catedra',         id_comuna=5,   provincia='Gato Chico',              region= 'AN'),
            Distritos(id_distrito=7, nombre='Distrito Bienestar',       id_comuna=4,   provincia='Perro Danes',             region= 'AN'),
            Distritos(id_distrito=8, nombre='Distrito Estuche',         id_comuna=3,   provincia='KDA',                     region= 'LOL'),
            Distritos(id_distrito=9, nombre='Distrito Liquid Paper',    id_comuna=2,   provincia='Maraton',                 region= 'GR'),
            Distritos(id_distrito=0, nombre='Distrito Tijera',          id_comuna=1,   provincia='Nuble',                   region= 'L6'),
        ]
        
        expected_output = ['Providencia', 'Macul', 'Puente Alto', 'Perro', 'Gato',
                            'Gato Chico', 'Perro Danes', 'KDA', 'Maraton','Nuble']

        generador = (p for p in lista_distritos)
        resultado = ciudades_distritos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne los nombres de las provincias cuando todos tienen casos de nombres iguales.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',      id_comuna=0,   provincia='Providencia',         region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Lapiz',           id_comuna=9,   provincia='Providencia',         region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Goma',            id_comuna=8,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=4, nombre='Distrito Corrector',       id_comuna=7,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=5, nombre='Distrito Automatizador',   id_comuna=6,   provincia='Gato',                region= 'AN'),
            Distritos(id_distrito=6, nombre='Distrito Catedra',         id_comuna=5,   provincia='Gato',                region= 'AN'),
            Distritos(id_distrito=7, nombre='Distrito Bienestar',       id_comuna=4,   provincia='Perro Danes',         region= 'AN'),
            Distritos(id_distrito=8, nombre='Distrito Estuche',         id_comuna=3,   provincia='Perro Danes',         region= 'AN'),
            Distritos(id_distrito=9, nombre='Distrito Liquid Paper',    id_comuna=2,   provincia='Maraton',             region= 'GR'),
            Distritos(id_distrito=0, nombre='Distrito Tijera',          id_comuna=1,   provincia='Maraton',             region= 'GR'),
        ]
        
        expected_output = ['Providencia', 'Puente Alto', 'Gato', 'Perro Danes', 'Maraton']
        
        generador = (p for p in lista_distritos)
        resultado = ciudades_distritos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne los nombres de las provincias cuando algunos tienen casos de nombres iguales.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',      id_comuna=0,   provincia='Providencia',         region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Lapiz',           id_comuna=9,   provincia='Macul',               region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Goma',            id_comuna=8,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=4, nombre='Distrito Corrector',       id_comuna=7,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=5, nombre='Distrito Automatizador',   id_comuna=6,   provincia='Gato',                region= 'AN'),
            Distritos(id_distrito=6, nombre='Distrito Catedra',         id_comuna=5,   provincia='Gato',                region= 'AN'),
            Distritos(id_distrito=7, nombre='Distrito Bienestar',       id_comuna=4,   provincia='Perro Danes',         region= 'AN'),
            Distritos(id_distrito=8, nombre='Distrito Estuche',         id_comuna=3,   provincia='KDA',                 region= 'LOL'),
            Distritos(id_distrito=9, nombre='Distrito Liquid Paper',    id_comuna=2,   provincia='Maraton',             region= 'GR'),
            Distritos(id_distrito=0, nombre='Distrito Tijera',          id_comuna=1,   provincia='Maraton',             region= 'GR')
        ]
        
        expected_output = ['Providencia', 'Puente Alto', 'Gato', 'Perro Danes', 'Maraton', 'KDA', 'Macul']
        
        generador = (p for p in lista_distritos)
        resultado = ciudades_distritos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
      
    def test_3(self):
        """
         Verifica que retorne los nombres de las provincias cuando algunos estan en la misma comuna y algunos tienen nombres iguales
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',      id_comuna=0,   provincia='Providencia',         region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Lapiz',           id_comuna=9,   provincia='Macul',               region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Goma',            id_comuna=4,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=4, nombre='Distrito Corrector',       id_comuna=3,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=5, nombre='Distrito Automatizador',   id_comuna=4,   provincia='Gato',                region= 'AN'),
            Distritos(id_distrito=6, nombre='Distrito Catedra',         id_comuna=3,   provincia='Perro',               region= 'AN'),
            Distritos(id_distrito=7, nombre='Distrito Bienestar',       id_comuna=2,   provincia='Recorcholis',         region= 'AN'),
            Distritos(id_distrito=8, nombre='Distrito Estuche',         id_comuna=1,   provincia='KDA',                 region= 'LOL'),
            Distritos(id_distrito=9, nombre='Distrito Liquid Paper',    id_comuna=2,   provincia='Maraton',             region= 'GR'),
            Distritos(id_distrito=0, nombre='Distrito Tijera',          id_comuna=1,   provincia='Maraton',             region= 'GR')
        ]
        
        expected_output = ['Providencia', 'Puente Alto', 'Gato', 'Perro', 'Recorcholis', 'Maraton', 'KDA', 'Macul']
        
        generador = (p for p in lista_distritos)
        resultado = ciudades_distritos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que retorne los nombres de las provincias cuando existen dos distritos del mismo nombre en provincias distintas.
        """
        lista_distritos = [
            Distritos(id_distrito=1, nombre='Distrito Sacapuntas',      id_comuna=0,   provincia='Providencia',         region= 'RM'),
            Distritos(id_distrito=2, nombre='Distrito Lapiz',           id_comuna=9,   provincia='Macul',               region= 'RM'),
            Distritos(id_distrito=3, nombre='Distrito Goma',            id_comuna=4,   provincia='Puente Alto',         region= 'RM'),
            Distritos(id_distrito=4, nombre='Distrito Corrector',       id_comuna=3,   provincia='Arenas',              region= 'RM'),
            Distritos(id_distrito=5, nombre='Distrito Automatizador',   id_comuna=4,   provincia='Gato',                region= 'AN'),
            Distritos(id_distrito=6, nombre='Distrito Catedra',         id_comuna=3,   provincia='Perro',               region= 'AN'),
            Distritos(id_distrito=7, nombre='Distrito Bienestar',       id_comuna=2,   provincia='Recorcholis',         region= 'AN'),
            Distritos(id_distrito=8, nombre='Distrito Estuche',         id_comuna=1,   provincia='KDA',                 region= 'LOL'),
            Distritos(id_distrito=9, nombre='Distrito Sacapuntas',      id_comuna=2,   provincia='Maraton',             region= 'GR'),
            Distritos(id_distrito=0, nombre='Distrito Goma',            id_comuna=1,   provincia='Maraton',             region= 'GR')
        ]
        
        expected_output = ['Providencia', 'Puente Alto', 'Gato', 'Perro', 'Recorcholis', 'Maraton', 'KDA', 'Macul', 'Arenas']
        
        generador = (p for p in lista_distritos)
        resultado = ciudades_distritos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_d = cargar_datos("distritos", carpeta)
        resultado = ciudades_distritos(g_d)
        expected_output = CIUDADES_DISTRITOS_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_d = cargar_datos("distritos", carpeta)
        resultado = ciudades_distritos(g_d)
        expected_output = CIUDADES_DISTRITOS_M
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_d = cargar_datos("distritos", carpeta)
        resultado = ciudades_distritos(g_d)
        expected_output = CIUDADES_DISTRITOS_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

   
if __name__ == "__main__":
    unittest.main(verbosity=2)
