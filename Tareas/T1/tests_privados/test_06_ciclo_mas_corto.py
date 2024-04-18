import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro
from dcciudad import elevar_matriz


class TestCicloMasCorto(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que el ciclo más corto tenga 7 estaciones intermedias.
        """
        conexiones = [
            [0, 1, 0, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["A", "EFF", "C", "D", "J", "F", "G", "V"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.ciclo_mas_corto("V")
        resultado_esperado = 7

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_1(self):
        """
        Verifica que el ciclo más corto tenga 0 estaciones intermedias.
        Caso de loop.
        """
        conexiones = [[0, 1, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 1, 1]]
        estaciones = ["A", "B", "C", "H"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.ciclo_mas_corto("H")
        resultado_esperado = 0

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_2(self):
        """
        Verifica que el ciclo más corto tenga más de una estación intermedia.
        (2 estaciones intermedias)
        """
        conexiones = [
            [0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["K", "B", "*", "D", "E", "F", "G"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.ciclo_mas_corto("*")
        resultado_esperado = 2

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_3(self):
        """
        Verifica que se utilice la función elevar_matriz de dcciudad.py
        """
        conexiones = [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 1, 0],
        ]
        estaciones = ["L", "O", "P", "B", "N", "M", "WE"]

        red = RedMetro(conexiones, estaciones)

        # Primero verificar si hace "import dcciudad y dcciudad.elevar_matriz"
        with patch("dcciudad.elevar_matriz", side_effect=elevar_matriz) as mock_2:
            red.ciclo_mas_corto("L")
            red.ciclo_mas_corto("O")
            red.ciclo_mas_corto("P")
            red.ciclo_mas_corto("B")
            red.ciclo_mas_corto("M")
            red.ciclo_mas_corto("N")
            red.ciclo_mas_corto("WE")

            try:
                mock_2.assert_called()
            except AssertionError:
                # Si no funciona
                # Probar si hace "from dcciudad import elevar_matriz"
                with patch("red.elevar_matriz", side_effect=elevar_matriz) as mock:
                    red.ciclo_mas_corto("L")
                    red.ciclo_mas_corto("O")
                    red.ciclo_mas_corto("P")
                    red.ciclo_mas_corto("B")
                    red.ciclo_mas_corto("M")
                    red.ciclo_mas_corto("N")
                    red.ciclo_mas_corto("WE")
                    mock.assert_called()

    def test_4(self):
        """
        Verifica que el ciclo más corto tenga una estación intermedia.
        """
        conexiones = [
            [0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["V", "B", "C", "D", "J", "F", "G"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.ciclo_mas_corto("J")
        resultado_esperado = 1

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_5(self):
        """
        Verifica que no exista ciclo para la estación.
        """
        conexiones = [
            [0, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F", "H"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.ciclo_mas_corto("H")
        resultado_esperado = -1

        self.assertEqual(resultado_estudiante, resultado_esperado)


with patch("sys.stdout", new=StringIO()):
    unittest.main(verbosity=2)
