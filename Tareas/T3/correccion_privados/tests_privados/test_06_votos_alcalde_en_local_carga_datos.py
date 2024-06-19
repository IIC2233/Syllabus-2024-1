import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_alcalde_en_local, cargar_datos
from test_solution import VOTOS_ALCALDE_EN_LOCAL_S, VOTOS_ALCALDE_EN_LOCAL_M, VOTOS_ALCALDE_EN_LOCAL_L, VOTOS_ALCALDE_EN_LOCAL_S_2, VOTOS_ALCALDE_EN_LOCAL_M_2, VOTOS_ALCALDE_EN_LOCAL_L_2

from timeout_function import timeout
N_SECOND = 20 

class TestVotosAlcaldeEnLocalCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 1, 2)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 11825, 3425)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 995616, 20)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_3(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 7025, 1398)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_S_2
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
     


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
