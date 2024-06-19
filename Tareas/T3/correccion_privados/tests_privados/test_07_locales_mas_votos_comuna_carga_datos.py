import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import locales_mas_votos_comuna, cargar_datos
from utilidades import Locales
from test_solution import LOCALES_MAS_VOTOS_COMUNA_S, LOCALES_MAS_VOTOS_COMUNA_M, LOCALES_MAS_VOTOS_COMUNA_L

from timeout_function import timeout
N_SECOND = 20 

class TestLocalesMasVotosComunaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_l = cargar_datos("locales", carpeta)
        resultado = locales_mas_votos_comuna (g_l, 2, 5)
        expected_output = LOCALES_MAS_VOTOS_COMUNA_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_l = cargar_datos("locales", carpeta)
        resultado = locales_mas_votos_comuna (g_l, 2, 5)
        expected_output = LOCALES_MAS_VOTOS_COMUNA_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_l = cargar_datos("locales", carpeta)
        resultado = locales_mas_votos_comuna (g_l, 2, 5)
        expected_output = LOCALES_MAS_VOTOS_COMUNA_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)   


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
