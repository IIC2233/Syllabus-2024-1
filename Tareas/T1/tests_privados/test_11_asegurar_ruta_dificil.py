import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestAsegurarRutaDificil(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que existe una solución para la ruta (3 estaciones intermedias).
        Eliminación de 2 túneles.
        """
        conexiones = [
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["K", "Q", "3", "y", "=="]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("K", "==", 3)
        resultados_esperados = [
            [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0],
            ]
        ]
        conexiones_originales = [
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
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

    def test_1(self):
        """
        Verifica que existe una solución para la ruta (4 estaciones intermedias).
        La solución es idéntica a la red original.
        """
        conexiones = [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["Hou", "Ak", "Lou", "VVV", "Min", "Omega"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("Omega", "Hou", 4)
        resultados_esperados = [
            [
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
            ]
        ]
        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
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
        Verifica la existencia de múltiples soluciones para la ruta.
        Se deben eliminar túneles de más de una estación.
        """
        conexiones = [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 0],
        ]
        estaciones = ["Pez", "B", "Cui", "D", "E", "Gato"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("Gato", "Pez", 2)
        resultados_esperados = [
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
            ],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 0],
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
        Verifica la existencia de una solución para la ruta.
        Se deben eliminar túneles de más de una estación.
        """
        conexiones = [
            [0, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]
        estaciones = ["Mil", "Dos", "Umi", "Neko", "Oswald", "Destino"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("Umi", "Neko", 4)
        resultados_esperados = [
            [
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
            ],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 0, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
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


with patch("sys.stdout", new=StringIO()):
    unittest.main(verbosity=2)
