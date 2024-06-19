import sys
import unittest
from collections import namedtuple

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_validos, cargar_datos
from test_solution import VOTOS_VALIDOS_S, VOTOS_VALIDOS_M, VOTOS_VALIDOS_L, VOTOS_VALIDOS_S_A, VOTOS_VALIDOS_M_A, VOTOS_VALIDOS_L_A

from timeout_function import timeout
N_SECOND = 20 

class TestVotosValidosCargaDatos(unittest.TestCase):

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
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos(g_a, g_v, g_p)
        
        resultado_considerando_la_edad = VOTOS_VALIDOS_S
        resultado_considerando_el_ano = VOTOS_VALIDOS_S_A

        try:
            self.assertEqual(resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertEqual(resultado, resultado_considerando_el_ano)
    
    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos(g_a, g_v, g_p)

        resultado_considerando_la_edad = VOTOS_VALIDOS_M
        resultado_considerando_el_ano = VOTOS_VALIDOS_M_A

        try:
            self.assertEqual(resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertEqual(resultado, resultado_considerando_el_ano)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos(g_a, g_v, g_p)

        resultado_considerando_la_edad = VOTOS_VALIDOS_L
        resultado_considerando_el_ano = VOTOS_VALIDOS_L_A

        try:
            self.assertEqual(resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertEqual(resultado, resultado_considerando_el_ano)

if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
