import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import cantidad_votos_especie_entre_edades, cargar_datos
from test_solution import (
    CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_S,
    CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_M,
    CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_L,
)

from timeout_function import timeout

N_SECOND = 20


class TestCantidadVotosEspecieEntreEdadesCargaDatos(unittest.TestCase):

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
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_especie_entre_edades(g_a, g_v, g_p, "Perro", 14, 16)
        expected_output = CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_S

        self.assertCountEqual(resultado, expected_output)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_especie_entre_edades(g_a, g_v, g_p, "Perro", 14, 16)
        expected_output = CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_M

        self.assertEqual(resultado, expected_output)

    @timeout(60)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_especie_entre_edades(g_a, g_v, g_p, "Perro", 14, 16)
        expected_output = CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_L

        self.assertEqual(resultado, expected_output)


if __name__ == "__main__":
    from io import StringIO

    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
