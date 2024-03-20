import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestAsegurarRuta(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_00(self):
        """
        Verifica que no existe una solución para la ruta (0 estaciones intermedias).
        """
        conexiones = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "D", 0)
        resultados_esperados = [[]]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0]]
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

    def test_01(self):
        """
        Verifica que no existe una solución para la ruta (3 estaciones intermedias).
        """
        conexiones = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "F", 3)
        resultados_esperados = [[]]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales= [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
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

    def test_02(self):
        """
        Verifica que existe una solución para la ruta (4 estaciones intermedias).
        La solución es idéntica a la red original.
        """
        conexiones = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "F", 4)
        resultados_esperados = [
            [
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
            ],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
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

    def test_03(self):
        """
        Verifica que existe solo una solución para la ruta (caso enunciado).
        """
        conexiones = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
        estaciones = ["A", "B", "C"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "C", 1)
        resultados_esperados = [
            [[0, 1, 0], [0, 0, 1], [0, 0, 0]],
        ]
        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
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

    def test_04(self):
        """
        Verifica que existen múltiples soluciones para la rutas (4).
        Existe un loop.
        Inicio y fin en la misma estación.
        """
        conexiones = [
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, 0],
        ]
        estaciones = ["A", "B", "C"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "A", 0)
        resultados_esperados = [
            [[1, 1, 0], [0, 0, 1], [0, 0, 0]],
            [[1, 1, 0], [0, 0, 0], [0, 0, 0]],
            [[1, 0, 0], [0, 0, 1], [0, 0, 0]],
            [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, 0],
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

    def test_05(self):
        """
        Verifica que existe una solución para la ruta (3 estaciones intermedias).
        Eliminación de 3 túneles.
        """
        conexiones = [
            [0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "E", 3)
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
            [0, 1, 1, 1, 1],
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

    def test_06(self):
        """
        Verifica que existen múltiples soluciones para la ruta (4).
        Existe un loop.
        """
        conexiones = [
            [0, 1],
            [1, 1],
        ]
        estaciones = ["A", "B"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "B", 0)
        resultados_esperados = [
            [[0, 1], [1, 1]],
            [[0, 1], [0, 1]],
            [[0, 1], [1, 0]],
            [[0, 1], [0, 0]],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 1],
            [1, 1],
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

    def test_07(self):
        """
        Verifica que no existen soluciones para la ruta en un caso simple,
        dado que existe un camino directo entre las estaciones y no hay forma de eliminar
        túneles de manera conveniente.
        Existencia de un loop.
        """
        conexiones = [
            [0, 1],
            [0, 1],
        ]
        estaciones = ["A", "B"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "B", 10)
        resultados_esperados = [
            [],
        ]
        conexiones_originales = [
            [0, 1],
            [0, 1],
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

    def test_08(self):
        """
        Verifica que no existen soluciones para la ruta en un caso simple,
        dado que existe un camino directo entre las estaciones y no hay forma de eliminar
        túneles de manera conveniente.
        Sin loop.
        """
        conexiones = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ]
        estaciones = ["A", "B", "C"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "B", 3)
        resultados_esperados = [
            [],
        ]
        conexiones_originales = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
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

    def test_09(self):
        """
        Verifica la existencia de múltiples soluciones para la ruta.
        Se deben eliminar túneles de más de una estación.
        """
        conexiones = [
            [0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "F", 4)
        resultados_esperados = [
            [
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
            ],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [
            [0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
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

    def test_10(self):
        """
        Verifica que existe una solución para la ruta (2 estaciones intermedias).
        Inicio y fin en la misma estación.
        """
        conexiones = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        estaciones = ["A", "B", "C"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.asegurar_ruta("A", "A", 2)
        resultados_esperados = [[[0, 1, 0], [0, 0, 1], [1, 0, 0]]]

        self.assertIsInstance(resultado_estudiante, list)
        conexiones_originales = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
