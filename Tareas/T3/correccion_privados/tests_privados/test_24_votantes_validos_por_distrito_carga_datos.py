import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votantes_validos_por_distritos, cargar_datos
from test_solution import (
    VOTANTES_VALIDOS_POR_DISTRITOS_S,
    VOTANTES_VALIDOS_POR_DISTRITOS_M,
    VOTANTES_VALIDOS_POR_DISTRITOS_L,
    VOTANTES_VALIDOS_POR_DISTRITOS_S_A,
    VOTANTES_VALIDOS_POR_DISTRITOS_M_A,
    VOTANTES_VALIDOS_POR_DISTRITOS_L_A,
)

from timeout_function import timeout
N_SECOND = 20 

class TestVotantesValidosPorDistritoCargaDatos(unittest.TestCase):

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
        g_d = cargar_datos("distritos", carpeta)
        g_l = cargar_datos("locales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = votantes_validos_por_distritos(g_a, g_d, g_l, g_v, g_p)

        resultado_considerando_la_edad = VOTANTES_VALIDOS_POR_DISTRITOS_S
        resultado_considerando_el_ano = VOTANTES_VALIDOS_POR_DISTRITOS_S_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_considerando_el_ano)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_l = cargar_datos("locales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = votantes_validos_por_distritos(g_a, g_d, g_l, g_v, g_p)

        resultado_considerando_la_edad = VOTANTES_VALIDOS_POR_DISTRITOS_M
        resultado_considerando_el_ano = VOTANTES_VALIDOS_POR_DISTRITOS_M_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_considerando_el_ano)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_l = cargar_datos("locales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = votantes_validos_por_distritos(g_a, g_d, g_l, g_v, g_p)

        resultado_considerando_la_edad = VOTANTES_VALIDOS_POR_DISTRITOS_L
        resultado_considerando_el_ano = VOTANTES_VALIDOS_POR_DISTRITOS_L_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_considerando_el_ano)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
