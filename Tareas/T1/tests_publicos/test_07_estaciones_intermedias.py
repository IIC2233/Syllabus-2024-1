import sys
import unittest

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
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("D", "E")
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
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("E", "A")
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
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("A", "A")
        resultado_esperado = ["C"]

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
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("D", "E")
        resultado_esperado = ["A", "B"]

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
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias("C", "E")
        resultado_esperado = ["A", "B", "D"]

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
