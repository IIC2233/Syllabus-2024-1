import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_candidato_mas_votado, cargar_datos
from test_solution import VOTOS_CANDIDATO_MAS_VOTADO_S, VOTOS_CANDIDATO_MAS_VOTADO_M, VOTOS_CANDIDATO_MAS_VOTADO_L

from timeout_function import timeout
N_SECOND = 20 

class TestVotosCandidatoMasVotadoCargaDatos(unittest.TestCase):

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
        resultado = votos_candidato_mas_votado(g_v)
        expected_output = VOTOS_CANDIDATO_MAS_VOTADO_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_candidato_mas_votado(g_v)
        expected_output = VOTOS_CANDIDATO_MAS_VOTADO_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(40)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_candidato_mas_votado(g_v)
        expected_output = VOTOS_CANDIDATO_MAS_VOTADO_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)  


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
