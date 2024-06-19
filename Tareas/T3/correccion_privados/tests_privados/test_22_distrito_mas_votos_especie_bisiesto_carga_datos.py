import sys
import unittest


# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import distrito_mas_votos_especie_bisiesto, cargar_datos
from test_solution import (
    DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_S,
    DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_M,
    DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_L,
    DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_S_A,
    DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_M_A,
    DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_L_A,
)

from timeout_function import timeout

N_SECOND = 20


class TestDistritoMasVotosEspecieBisiestoCargaDatos(unittest.TestCase):

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
        g_v = cargar_datos("votos", carpeta)
        resultado = distrito_mas_votos_especie_bisiesto(g_a, g_v, g_d, "Gato")
        expected_output = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_S
        expected_output_alternative = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_S_A

        self.assertIn(resultado, [expected_output, expected_output_alternative])

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = distrito_mas_votos_especie_bisiesto(g_a, g_v, g_d, "Gato")
        expected_output = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_M
        expected_output_alternative = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_M_A

        self.assertIn(resultado, [expected_output, expected_output_alternative])

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = distrito_mas_votos_especie_bisiesto(g_a, g_v, g_d, "Gato")
        expected_output = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_L
        expected_output_alternative = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_L_A

        self.assertIn(resultado, [expected_output, expected_output_alternative])


if __name__ == "__main__":
    from io import StringIO

    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
