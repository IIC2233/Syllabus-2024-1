
import sys
import unittest
from collections import namedtuple

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import cantidad_votos_candidato, cargar_datos
from test_solution import CANTIDAD_VOTOS_CANDIDATO_S, CANTIDAD_VOTOS_CANDIDATO_M, CANTIDAD_VOTOS_CANDIDATO_L

from timeout_function import timeout
N_SECOND = 20 

class TestCantidadVotosCandidatoCargaDatos(unittest.TestCase):

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
        resultado = cantidad_votos_candidato(g_v, 4611)
        expected_output = CANTIDAD_VOTOS_CANDIDATO_S
        
        self.assertEqual(resultado, expected_output)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_candidato(g_v, 11825)
        expected_output = CANTIDAD_VOTOS_CANDIDATO_M
        
        self.assertEqual(resultado, expected_output)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_candidato(g_v, 995616)
        expected_output = CANTIDAD_VOTOS_CANDIDATO_L
        
        self.assertEqual(resultado, expected_output)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
