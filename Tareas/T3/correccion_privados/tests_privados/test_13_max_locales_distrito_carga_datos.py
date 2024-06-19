import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import max_locales_distrito, cargar_datos
from utilidades import Distritos, Locales
from test_solution import MAX_LOCALES_DISTRITO_S, MAX_LOCALES_DISTRITO_M, MAX_LOCALES_DISTRITO_L

from timeout_function import timeout
N_SECOND = 20 

class TestMaxLocalesDistritoCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_d = cargar_datos("distritos", carpeta)
        g_l =  cargar_datos("locales", carpeta)
        resultado = max_locales_distrito(g_d, g_l)
        expected_output = MAX_LOCALES_DISTRITO_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_d = cargar_datos("distritos", carpeta)
        g_l =  cargar_datos("locales", carpeta)
        resultado = max_locales_distrito(g_d, g_l)
        expected_output = MAX_LOCALES_DISTRITO_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_d = cargar_datos("distritos", carpeta)
        g_l =  cargar_datos("locales", carpeta)
        resultado = max_locales_distrito(g_d, g_l)
        expected_output = MAX_LOCALES_DISTRITO_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
