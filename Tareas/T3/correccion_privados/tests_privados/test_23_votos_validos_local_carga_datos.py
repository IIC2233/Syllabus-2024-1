import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_validos_local, cargar_datos
from utilidades import Animales, Votos, Ponderador
from test_solution import VOTOS_VALIDOS_LOCAL_S, VOTOS_VALIDOS_LOCAL_M, VOTOS_VALIDOS_LOCAL_L, VOTOS_VALIDOS_LOCAL_S_A, VOTOS_VALIDOS_LOCAL_M_A, VOTOS_VALIDOS_LOCAL_L_A

from timeout_function import timeout
N_SECOND = 20 

class TestVotosValidosLocalCargaDatos(unittest.TestCase):

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
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos_local(g_a, g_v, g_p, 6)
        
        resultado_esperado_considerando_el_ano_de_nacimiento = VOTOS_VALIDOS_LOCAL_S
        resultado_esperado_considerando_la_edad = VOTOS_VALIDOS_LOCAL_S_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)
    
    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos_local(g_a, g_v, g_p, 6)
        
        resultado_esperado_considerando_el_ano_de_nacimiento = VOTOS_VALIDOS_LOCAL_M
        resultado_esperado_considerando_la_edad = VOTOS_VALIDOS_LOCAL_M_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos_local(g_a, g_v, g_p, 6)
        
        resultado_esperado_considerando_el_ano_de_nacimiento = VOTOS_VALIDOS_LOCAL_L
        resultado_esperado_considerando_la_edad = VOTOS_VALIDOS_LOCAL_L_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
