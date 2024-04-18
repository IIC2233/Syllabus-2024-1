import sys
import unittest
from io import StringIO
from unittest.mock import patch

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from red import RedMetro


class TestEstacionesIntermediasAvanzado(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que no exista un camino con dos estaciones intermedias entre 2 estaciones,
        pero sí existe un túnel directo entre estas.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0],
        ]
        estaciones = ["A", "B", "=1", "D", "E", "$."]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("$.", "=1")
        resultado_esperado = []

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            0,
            f"""Se esperaban 0 listas; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_1(self):
        """
        Verifica que no exista un camino con dos estaciones intermedias entre 2 estaciones,
        pero no existe un túnel directo entre estas.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ]
        estaciones = ["6Y", "CE", "C", "P", "33W", "55E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("33W", "55E")
        resultado_esperado = []

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            0,
            f"""Se esperaban 0 listas; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_2(self):
        """
        Verifica que exista un camino con dos estaciones intermedias entre 2 estaciones.
        """
        conexiones = [
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 1, 0],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "Be", "Ce", "D", "El", "Fa"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("Be", "Fa")
        resultado_esperado = [["Ce", "El"]]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            1,
            f"""Se esperaban 1 listas; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        for lista in resultado_estudiante:
            self.assertIsInstance(lista, list)
            self.assertEqual(len(lista), 2)
            for elemento in lista:
                self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_3(self):
        """
        Verifica que exista más de un camino con dos estaciones intermedias (2 caminos)
        entre 2 estaciones.
        """
        conexiones = [
            [0, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("C", "A")
        resultado_esperado = [["A", "C"], ["F", "A"]]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            2,
            f"""Se esperaban 2 listas; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        for lista in resultado_estudiante:
            self.assertIsInstance(lista, list)
            self.assertEqual(len(lista), 2)
            for elemento in lista:
                self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_4(self):
        """
        Verifica que exista más de un camino con dos estaciones intermedias (3 caminos)
        entre 2 estaciones.
        """
        conexiones = [
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [1, 1, 1, 0],
        ]
        estaciones = ["RW", "3q", "H", "La ciudad"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("La ciudad", "3q")
        resultado_esperado = [
            ["La ciudad", "RW"],
            ["La ciudad", "3q"],
            ["La ciudad", "H"],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            3,
            f"""Se esperaban 3 listas; en cambio,
                            se obtuvieron {len(resultado_estudiante)}""",
        )

        for lista in resultado_estudiante:
            self.assertIsInstance(lista, list)
            self.assertEqual(len(lista), 2)
            for elemento in lista:
                self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_5(self):
        """
        Verifica que exista más de un camino con dos estaciones intermedias (6 caminos)
        entre 2 estaciones.
        Comprueba también caminos que pasan por inicial y final.
        """
        conexiones = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
        estaciones = ["A", "B", "C", "&27"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("&27", "C")
        resultado_esperado = [
            ["C", "&27"],
            ["B", "C"],
            ["B", "&27"],
            ["A", "C"],
            ["A", "&27"],
            ["A", "B"],
        ]

        print()
        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            6,
            f"""Se esperaban 6 listas; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        for lista in resultado_estudiante:
            self.assertIsInstance(lista, list)
            self.assertEqual(len(lista), 2)
            for elemento in lista:
                self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)

    def test_6(self):
        """
        Verifica que exista más de un camino con dos estaciones intermedias (36 caminos)
        entre 2 estaciones.
        Caso de grafo completo con loops.
        """
        conexiones = [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ]
        estaciones = ["0", "1", "2", "3", "4", "5"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("2", "2")
        resultado_esperado = [
            ["0", "0"],
            ["0", "1"],
            ["0", "2"],
            ["0", "3"],
            ["0", "4"],
            ["0", "5"],
            ["1", "0"],
            ["1", "1"],
            ["1", "2"],
            ["1", "3"],
            ["1", "4"],
            ["1", "5"],
            ["2", "0"],
            ["2", "1"],
            ["2", "2"],
            ["2", "3"],
            ["2", "4"],
            ["2", "5"],
            ["3", "0"],
            ["3", "1"],
            ["3", "2"],
            ["3", "3"],
            ["3", "4"],
            ["3", "5"],
            ["4", "0"],
            ["4", "1"],
            ["4", "2"],
            ["4", "3"],
            ["4", "4"],
            ["4", "5"],
            ["5", "0"],
            ["5", "1"],
            ["5", "2"],
            ["5", "3"],
            ["5", "4"],
            ["5", "5"],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            36,
            f"""Se esperaban 36 listas; en cambio, 
                         se obtuvieron {len(resultado_estudiante)}""",
        )

        for lista in resultado_estudiante:
            self.assertIsInstance(lista, list)
            self.assertEqual(len(lista), 2)
            for elemento in lista:
                self.assertIsInstance(elemento, str)

        resultado_estudiante_set = {tuple(sorted(x)) for x in resultado_estudiante}
        resultado_esperado_set = {tuple(sorted(x)) for x in resultado_esperado}

        self.assertCountEqual(resultado_estudiante_set, resultado_esperado_set)


with patch("sys.stdout", new=StringIO()):
    unittest.main(verbosity=2)
