import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestAsegurarRutaSinSolucion(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que no existe una solución para la ruta (0 estaciones intermedias).
        """
        conexiones = [[1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1], [1, 0, 1, 0]]
        estaciones = ["A", "B", "C", "D-"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("D-", "B", 0)
        resultados_esperados = [[]]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [[1, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1], [1, 0, 1, 0]]
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
        Verifica que no existe una solución para la ruta (3 estaciones intermedias).
        """
        conexiones = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["9000", "B", "C", "D", "E", "FHd"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("FHd", "9000", 3)
        resultados_esperados = [[]]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
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
        Verifica que no existen soluciones para la ruta en un caso simple,
        dado que existe un camino directo entre las estaciones y no hay forma de eliminar
        túneles de manera conveniente.
        Existencia de un loop.
        """
        conexiones = [
            [0, 1],
            [1, 1],
        ]
        estaciones = ["OU", "98f"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("98f", "OU", 13)
        resultados_esperados = [
            [],
        ]
        conexiones_originales = [
            [0, 1],
            [1, 1],
        ]
        self.assertIsInstance(resultado_estudiante, list)
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
        Verifica que no existen soluciones para la ruta en un caso simple,
        dado que existe un camino directo entre las estaciones y no hay forma de eliminar
        túneles de manera conveniente.
        Sin loop.
        """
        conexiones = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
        ]
        estaciones = ["L", "X", "Y", "Z"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("X", "Y", 4)
        resultados_esperados = [
            [],
        ]
        conexiones_originales = [
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
        ]
        self.assertIsInstance(resultado_estudiante, list)
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
