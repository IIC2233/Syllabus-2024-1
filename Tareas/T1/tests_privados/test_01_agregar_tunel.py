import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestAgregarTunel(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que se agregue un túnel donde no exista uno.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0],
        ]

        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.agregar_tunel("F", "B")
        resultado_esperado = 4

        conexiones_esperado = [
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)

    def test_1(self):
        """
        Verifica que no se agregue un túnel donde ya exista uno.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.agregar_tunel("F", "A")
        resultado_esperado = -1

        conexiones_esperado = [
            [0, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)

    def test_2(self):
        """
        Verifica que se agregue un túnel donde no exista uno para la misma estación.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0],
        ]

        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.agregar_tunel("A", "A")
        resultado_esperado = 4

        conexiones_esperado = [
            [1, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)

    def test_3(self):
        """
        Verifica que no se agregue un túnel donde ya exista uno para la misma estación.
        """
        conexiones = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.agregar_tunel("A", "A")
        resultado_esperado = -1

        conexiones_esperado = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
