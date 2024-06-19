import sys
import unittest
import os
import csv
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import hallar_region, cargar_datos
from test_solution import HALLAR_REGION_S, HALLAR_REGION_M, HALLAR_REGION_L

from timeout_function import timeout
N_SECOND = 20 

class TestHallarRegionCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_d = cargar_datos("distritos", carpeta)
        g_l =  cargar_datos("locales", carpeta)
        resultado = hallar_region(g_d , g_l, 12)
        expected_output = HALLAR_REGION_S
        
        self.assertCountEqual(resultado, expected_output)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_d = cargar_datos("distritos", carpeta)
        g_l =  cargar_datos("locales", carpeta)
        resultado = hallar_region(g_d , g_l, 12)
        expected_output = HALLAR_REGION_M

        self.assertCountEqual(resultado, expected_output)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_d = cargar_datos("distritos", carpeta)
        g_l =  cargar_datos("locales", carpeta)
        resultado = hallar_region(g_d , g_l, 12)
        expected_output = HALLAR_REGION_L
        
        self.assertCountEqual(resultado, expected_output)  


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
