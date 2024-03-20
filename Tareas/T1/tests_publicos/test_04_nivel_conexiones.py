import sys
import unittest
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro
from dcciudad import alcanzable


class TestNivelConexiones(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que exista túnel directo entre 2 estaciones.
        """
        conexiones = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.nivel_conexiones("A", "B")
        resultado_esperado = "túnel directo"

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_1(self):
        """
        Verifica que exista una estación intermedia entre 2 estaciones.
        """
        conexiones = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.nivel_conexiones("A", "C")
        resultado_esperado = "estación intermedia"

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_2(self):
        """
        Verifica que exista camino, aunque hay más de 1 estación intermedia.
        """
        conexiones = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.nivel_conexiones("A", "D")
        resultado_esperado = "muy lejos"

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_3(self):
        """
        Verifica que no exista camino.
        """
        conexiones = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.nivel_conexiones("D", "B")
        resultado_esperado = "no hay ruta"

        self.assertEqual(resultado_estudiante, resultado_esperado)

    def test_4(self):
        """
        Verifica que se utilice la función alcanzable de "dcciudad.py".
        """
        conexiones = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        
        # Primero verificar si hace "import dcciudad y dcciudad.alcanzable"
        with patch("dcciudad.alcanzable", side_effect=alcanzable) as mock_2:
            red.nivel_conexiones("A", "B")
            red.nivel_conexiones("A", "C")
            red.nivel_conexiones("A", "D")
            red.nivel_conexiones("D", "B")

            try:
                mock_2.assert_called()
            except AssertionError:
                # Si no funciona
                # Probar si hace "from dcciudad import alcanzable"
                with patch("red.alcanzable", side_effect=alcanzable) as mock:
                    red.nivel_conexiones("A", "B")
                    red.nivel_conexiones("A", "C")
                    red.nivel_conexiones("A", "D")
                    red.nivel_conexiones("D", "B")
                    mock.assert_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
