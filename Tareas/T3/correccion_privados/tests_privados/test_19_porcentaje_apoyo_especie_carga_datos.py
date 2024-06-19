import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import porcentaje_apoyo_especie, cargar_datos
from utilidades import Animales, Candidatos, Votos
from test_solution import PORCENTAJE_APOYO_ESPECIE_S, PORCENTAJE_APOYO_ESPECIE_M, PORCENTAJE_APOYO_ESPECIE_L 

from timeout_function import timeout
N_SECOND = 20 

class TestPorcentajeApoyoEspecieCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = porcentaje_apoyo_especie(g_a, g_c, g_v)
        expected_output = PORCENTAJE_APOYO_ESPECIE_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = porcentaje_apoyo_especie(g_a, g_c, g_v)
        expected_output = PORCENTAJE_APOYO_ESPECIE_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = porcentaje_apoyo_especie(g_a, g_c, g_v)
        expected_output = PORCENTAJE_APOYO_ESPECIE_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
