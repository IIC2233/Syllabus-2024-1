import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestCambiarPlanos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verificar lectura y modificación del nuevo plano.
        """
        conexiones = [[0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)

        self.assertEqual(red.cambiar_planos("test_1_private.txt"), True)
        conexiones_esperadas = [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [1, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0],
        ]
        estaciones_esperadas = [
            "Moneda",
            "Camino Agricola",
            "Cerrillos",
            "Miradores",
            "Quinta Normal",
            "San Joaquin",
        ]

        self.assertListEqual(red.red, conexiones_esperadas)
        self.assertListEqual(red.estaciones, estaciones_esperadas)

    def test_1(self):
        """
        Verifica que no actualice cuando no existe archivo.
        """
        conexiones = [[0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        self.assertEqual(red.cambiar_planos("text_-11.txt"), False)

        self.assertListEqual(red.red, conexiones)
        self.assertListEqual(red.estaciones, estaciones)

    def test_2(self):
        """
        Verificar lectura y modificación del nuevo plano.
        """
        conexiones = [[0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)

        self.assertEqual(red.cambiar_planos("test_2_private.txt"), True)
        conexiones_esperadas = [[1, 1, 0], [0, 1, 0], [1, 0, 1]]
        estaciones_esperadas = ["Camino Agricola", "Los Contadores", "Baquedano"]

        self.assertListEqual(red.red, conexiones_esperadas)
        self.assertListEqual(red.estaciones, estaciones_esperadas)

    def test_3(self):
        """
        Verifica que no actualice cuando no existe archivo.
        """
        conexiones = [[0, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        self.assertEqual(red.cambiar_planos("solucion.ppt"), False)

        self.assertListEqual(red.red, conexiones)
        self.assertListEqual(red.estaciones, estaciones)


if __name__ == "__main__":
    unittest.main(verbosity=2)
