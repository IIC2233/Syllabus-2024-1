import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestEstacionesIntermedias(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que no existan estaciones intermedias entre 2 estaciones,
        pero sí existe un túnel directo entre estas.
        """
        conexiones = [
            [0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
        ]
        estaciones = ["Juan", "R", "C", "S", "U"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("U", "S")
        resultado_esperado = []

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            0,
            f"""Se esperaban 0 estaciones intermedias; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        resultado_estudiante_set = {x for x in resultado_estudiante}
        resultado_esperado_set = {x for x in resultado_esperado}

        self.assertSetEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_1(self):
        """
        Verifica que no existan estaciones intermedias entre 2 estaciones,
        pero no existe un túnel directo entre estas.
        """
        conexiones = [
            [0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
        ]
        estaciones = ["I", "B", "C", "D", "O"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("O", "I")
        resultado_esperado = []

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            0,
            f"""Se esperaban 0 estaciones intermedias; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        resultado_estudiante_set = {x for x in resultado_estudiante}
        resultado_esperado_set = {x for x in resultado_esperado}

        self.assertSetEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_2(self):
        """
        Verifica que exista una estación intermedia entre 2 estaciones.
        """
        conexiones = [
            [0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0],
        ]
        estaciones = ["A", "GR", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("GR", "GR")
        resultado_esperado = ["D"]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            1,
            f"""Se esperaba 1 estación intermedia; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        for elemento in resultado_estudiante:
            self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {x for x in resultado_estudiante}
        resultado_esperado_set = {x for x in resultado_esperado}

        self.assertSetEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_3(self):
        """
        Verifica que existan más de una estación intermedia entre 2 estaciones (2 estaciones).
        """
        conexiones = [
            [0, 1, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["AR", "Los", "XOR", "H", "J"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("H", "J")
        resultado_esperado = ["Los", "XOR"]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            2,
            f"""Se esperaban 2 estaciones intermedias; en cambio, 
                            se obtuvieron {len(resultado_estudiante)}""",
        )

        for elemento in resultado_estudiante:
            self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {x for x in resultado_estudiante}
        resultado_esperado_set = {x for x in resultado_esperado}

        self.assertSetEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_4(self):
        """
        Verifica que existan más de una estación intermedia entre 2 estaciones (3 estaciones).
        """
        conexiones = [
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
        ]
        estaciones = ["1", "2", "3", "4", "5"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("1", "2")
        resultado_esperado = ["3", "4", "5"]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            3,
            f"""Se esperaban 3 estaciones intermedias; en cambio, 
                            se obtuvieron {len(resultado_estudiante)}""",
        )

        for elemento in resultado_estudiante:
            self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {x for x in resultado_estudiante}
        resultado_esperado_set = {x for x in resultado_esperado}

        self.assertSetEqual(resultado_estudiante_set, resultado_esperado_set)


with patch("sys.stdout", new=StringIO()):
    unittest.main(verbosity=2)
