import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import mismo_mes_candidato , cargar_datos
from test_solution import MISMO_MES_CANDIDATO_S, MISMO_MES_CANDIDATO_M, MISMO_MES_CANDIDATO_L, MISMO_MES_CANDIDATO_S_2, MISMO_MES_CANDIDATO_M_2, MISMO_MES_CANDIDATO_L_2

from timeout_function import timeout
N_SECOND = 20 

class TestMismoMesCandidatoCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_0(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 1)
        expected_output = MISMO_MES_CANDIDATO_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 11825)
        expected_output = MISMO_MES_CANDIDATO_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 995616)
        expected_output = MISMO_MES_CANDIDATO_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_3(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 5088)
        expected_output = MISMO_MES_CANDIDATO_S_2
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)




if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
