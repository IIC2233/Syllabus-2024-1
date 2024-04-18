import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestAsegurarRutaFacil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que existe solo una solución para la ruta.
        """
        conexiones = [[0, 0, 0], [1, 0, 1], [1, 0, 0]]
        estaciones = ["QR", "wF", "("]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("wF", "QR", 1)
        resultados_esperados = [
            [[0, 0, 0], [0, 0, 1], [1, 0, 0]],
        ]
        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [[0, 0, 0], [1, 0, 1], [1, 0, 0]]
        self.assertListEqual(
            red.red,
            conexiones_originales,
            "Se ha modificado la red original; no se debe modificar la red original",
        )
        self.assertIn(
            resultado_estudiante,
            resultados_esperados,
            "La solución no está en los resultados esperados	",
        )

    def test_1(self):
        """
        Verifica que existen múltiples soluciones para la rutas (4).
        Existe un loop.
        Inicio y fin en la misma estación.
        """
        conexiones = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 1],
        ]
        estaciones = ["A", "U", "C"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("U", "U", 0)
        resultados_esperados = [
            [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[0, 0, 0], [0, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        ]
        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 1],
        ]
        self.assertListEqual(
            red.red,
            conexiones_originales,
            "Se ha modificado la red original; no se debe modificar la red original",
        )
        self.assertIn(
            resultado_estudiante,
            resultados_esperados,
            "La solución no está en los resultados esperados	",
        )

    def test_2(self):
        """
        Verifica que existen múltiples soluciones para la ruta (4).
        Existe un loop.
        """
        conexiones = [
            [1, 1],
            [1, 0],
        ]
        estaciones = ["42", "Mac"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("Mac", "42", 0)
        resultados_esperados = [
            [[1, 1], [1, 0]],
            [[0, 1], [1, 0]],
            [[1, 0], [1, 0]],
            [[0, 0], [1, 0]],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [1, 1],
            [1, 0],
        ]
        self.assertListEqual(
            red.red,
            conexiones_originales,
            "Se ha modificado la red original; no se debe modificar la red original",
        )
        self.assertIn(
            resultado_estudiante,
            resultados_esperados,
            "La solución no está en los resultados esperados	",
        )

    def test_3(self):
        """
        Verifica que existe una solución para la ruta (3 estaciones intermedias).
        Inicio y fin en la misma estación.
        """
        conexiones = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
        estaciones = ["C", "B", "ACE", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("ACE", "ACE", 3)
        resultados_esperados = [
            [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
        self.assertListEqual(
            red.red,
            conexiones_originales,
            "Se ha modificado la red original; no se debe modificar la red original",
        )
        self.assertIn(
            resultado_estudiante,
            resultados_esperados,
            "La solución no está en los resultados esperados	",
        )


with patch("sys.stdout", new=StringIO()):
    unittest.main(verbosity=2)
