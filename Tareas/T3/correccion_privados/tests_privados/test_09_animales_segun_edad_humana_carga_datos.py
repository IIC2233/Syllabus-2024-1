import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_segun_edad_humana, cargar_datos
from utilidades import Animales, Ponderador
from test_solution import ANIMALES_SEGUN_EDAD_HUMANA_S, ANIMALES_SEGUN_EDAD_HUMANA_M, ANIMALES_SEGUN_EDAD_HUMANA_L

from timeout_function import timeout
N_SECOND = 20 

class TestAnimalesSegunEdadHumanaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_6(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_p =  cargar_datos("ponderadores", carpeta)
        resultado = animales_segun_edad_humana(g_a, g_p, ">", 11)
        expected_output = ANIMALES_SEGUN_EDAD_HUMANA_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p =  cargar_datos("ponderadores", carpeta)
        resultado = animales_segun_edad_humana(g_a, g_p, ">", 11)
        expected_output = ANIMALES_SEGUN_EDAD_HUMANA_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p =  cargar_datos("ponderadores", carpeta)
        resultado = animales_segun_edad_humana(g_a, g_p, ">", 11)
        expected_output = ANIMALES_SEGUN_EDAD_HUMANA_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)  


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
