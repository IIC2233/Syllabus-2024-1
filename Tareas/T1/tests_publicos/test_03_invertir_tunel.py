import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestInvertirTunel(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que no se invierta cuando no hay túneles entre dos estaciones.
        """
        conexiones = [
            [0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.invertir_tunel("C", "D")
        resultado_esperado = False

        conexiones_esperado = [
            [0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)

    def test_1(self):
        """
        Verifica que se invierta un túnel donde existe uno de estacion_1 a estacion_2.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F", "G"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.invertir_tunel("C", "B")
        resultado_esperado = True

        conexiones_esperado = [
            [0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 0, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)

    def test_2(self):
        """
        Verifica que se invierta un túnel donde existe uno de estacion_2 a estacion_1.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F", "G"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.invertir_tunel("G", "F")
        resultado_esperado = True

        conexiones_esperado = [
            [0, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 1, 1, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)

    def test_3(self):
        """
        Verifica caso donde exista conexión en ambos sentidos.
        """
        conexiones = [
            [0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F", "G"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.invertir_tunel("A", "B")
        resultado_esperado = True

        conexiones_esperado = [
            [0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
        ]

        self.assertEqual(resultado_estudiante, resultado_esperado)
        self.assertListEqual(red.red, conexiones_esperado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
