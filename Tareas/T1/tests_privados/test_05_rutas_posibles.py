import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestRutasPosibles(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verificar cantidad de rutas con cantidad específica de estaciones intermedias.
        """
        conexiones = [
            [0, 1, 0, 1, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0],
            [1, 1, 1, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.rutas_posibles("C", "D", 2)
        resultado_esperado = 3

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_1(self):
        """
        Verificar cantidad de rutas con cantidad específica de estaciones intermedias
        y diagonales cíclicas.
        """
        conexiones = [
            [1, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.rutas_posibles("B", "A", 1)
        resultado_esperado = 4

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_2(self):
        """
        Verifica para caso sin rutas con esa cantidad específica de estaciones intermedias.
        """
        conexiones = [[1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.rutas_posibles("D", "C", 1)
        resultado_esperado = 0

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_3(self):
        """
        Verifica para caso sin rutas entre estaciones y diagonales.
        """
        conexiones = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.rutas_posibles("C", "A", 2)
        resultado_esperado = 0

        self.assertEqual(resultado_estudiante, resultado_esperado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
