import sys
import unittest

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
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("C", "F")
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
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("F", "E")
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
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("D", "F")
        resultado_esperado = [["B", "C"]]

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
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D", "E", "F"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("A", "F")
        resultado_esperado = [["B", "C"], ["D", "E"]]

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
            [0, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("A", "B")
        resultado_esperado = [
            ["B", "A"],
            ["C", "A"],
            ["D", "A"],
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
        Verifica que exista más de un camino con dos estaciones intermedias (7 caminos)
        entre 2 estaciones.
        Comprueba también caminos que pasan por inicial y final.
        """
        conexiones = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
        estaciones = ["A", "B", "C", "D"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("A", "B")
        resultado_esperado = [
            ["C", "D"],
            ["B", "A"],
            ["B", "C"],
            ["B", "D"],
            ["A", "C"],
            ["A", "D"],
            ["D", "C"],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            7,
            f"""Se esperaban 7 listas; en cambio, 
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
        Verifica que exista más de un camino con dos estaciones intermedias (25 caminos)
        entre 2 estaciones.
        Caso de grafo completo con loops.
        """
        conexiones = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
        estaciones = ["A", "B", "C", "D", "E"]

        red = RedMetro(conexiones, estaciones)
        resultado_estudiante = red.estaciones_intermedias_avanzado("D", "D")
        resultado_esperado = [
            ["A", "A"],
            ["A", "B"],
            ["A", "C"],
            ["A", "D"],
            ["A", "E"],
            ["B", "A"],
            ["B", "B"],
            ["B", "C"],
            ["B", "D"],
            ["B", "E"],
            ["C", "A"],
            ["C", "B"],
            ["C", "C"],
            ["C", "D"],
            ["C", "E"],
            ["D", "A"],
            ["D", "B"],
            ["D", "C"],
            ["D", "D"],
            ["D", "E"],
            ["E", "A"],
            ["E", "B"],
            ["E", "C"],
            ["E", "D"],
            ["E", "E"],
        ]

        self.assertIsInstance(resultado_estudiante, list)
        self.assertEqual(
            len(resultado_estudiante),
            25,
            f"""Se esperaban 25 listas; en cambio, 
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
