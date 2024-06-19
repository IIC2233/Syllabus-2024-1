import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_segun_edad, cargar_datos
from test_solution import ANIMALES_SEGUN_EDAD_S, ANIMALES_SEGUN_EDAD_M, ANIMALES_SEGUN_EDAD_L

from timeout_function import timeout
N_SECOND = 20 

class TestAnimalesSegunEdadCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_1(self):
        """
         Verifica que el test funcione para pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        resultado = animales_segun_edad(g_a, "<", 10)
        expected_output = ANIMALES_SEGUN_EDAD_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_2(self):
        """
         Verifica que el test funcione para medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        resultado = animales_segun_edad(g_a, "<", 10)
        expected_output = ANIMALES_SEGUN_EDAD_M
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_3(self):
        """
         Verifica que el test funcione para grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        resultado = animales_segun_edad(g_a, "<", 10)
        expected_output = ANIMALES_SEGUN_EDAD_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
