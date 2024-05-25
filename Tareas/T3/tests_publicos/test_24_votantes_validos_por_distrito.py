import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votantes_validos_por_distritos, cargar_datos
from test_solution import (
    VOTANTES_VALIDOS_POR_DISTRITOS_S,
    VOTANTES_VALIDOS_POR_DISTRITOS_M,
    VOTANTES_VALIDOS_POR_DISTRITOS_L,
    VOTANTES_VALIDOS_POR_DISTRITOS_S_A,
    VOTANTES_VALIDOS_POR_DISTRITOS_M_A,
    VOTANTES_VALIDOS_POR_DISTRITOS_L_A,
    
)

class TestVotantesValidosPorDistrito(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=2, id_votantes=[4]),
            Locales(id_local=4, nombre_local="Local 4", id_comuna=3, id_votantes=[5]),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada4 = [
            Voto(1, 1, 0, 5),
            Voto(2, 2, 1, 3),
            Voto(3, 3, 2, 1),
            Voto(4, 4, 3, 1),
            Voto(5, 5, 4, 1),
        ]

        generador_entregado4 = (element for element in lista_entregada4)

        Ponderador = namedtuple("Ponderador", ["especie", "ponderador"])

        lista_entregada5 = [Ponderador("Perro", 5.5), Ponderador("Gato", 4)]

        generador_entregado5 = (element for element in lista_entregada5)

        resultado_estudiante = votantes_validos_por_distritos(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            generador_entregado4,
            generador_entregado5,
        )

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
        ]
        resultado_considerando_la_edad = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)


    def test_1(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Perro", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=2, id_votantes=[4]),
            Locales(id_local=4, nombre_local="Local 4", id_comuna=3, id_votantes=[5]),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada4 = [
            Voto(1, 1, 0, 5),
            Voto(2, 2, 1, 3),
            Voto(3, 3, 2, 1),
            Voto(4, 4, 3, 1),
            Voto(5, 5, 4, 1),
        ]

        generador_entregado4 = (element for element in lista_entregada4)

        Ponderador = namedtuple("Ponderador", ["especie", "ponderador"])

        lista_entregada5 = [Ponderador("Perro", 0.1), Ponderador("Gato", 4)]

        generador_entregado5 = (element for element in lista_entregada5)

        resultado_estudiante = votantes_validos_por_distritos(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            generador_entregado4,
            generador_entregado5,
        )

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]
        resultado_considerando_la_edad = [
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_2(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=2, id_votantes=[4]),
            Locales(id_local=4, nombre_local="Local 4", id_comuna=3, id_votantes=[5]),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada4 = [
            Voto(1, 1, 0, 5),
            Voto(2, 2, 1, 3),
            Voto(3, 3, 2, 1),
            Voto(4, 4, 3, 1),
            Voto(5, 5, 4, 1),
        ]

        generador_entregado4 = (element for element in lista_entregada4)

        Ponderador = namedtuple("Ponderador", ["especie", "ponderador"])

        lista_entregada5 = [Ponderador("Perro", 5.5), Ponderador("Gato", 0.01)]

        generador_entregado5 = (element for element in lista_entregada5)

        resultado_estudiante = votantes_validos_por_distritos(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            generador_entregado4,
            generador_entregado5,
        )

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
        ]
        resultado_considerando_la_edad = [
            Animal(1, "Gay", "Perro", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_3(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(1, "Gay", "Gallina", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gallina", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=3, id_votantes=[4]),
            Locales(id_local=4, nombre_local="Local 4", id_comuna=3, id_votantes=[5]),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada4 = [
            Voto(1, 1, 0, 5),
            Voto(2, 2, 1, 3),
            Voto(3, 3, 2, 1),
            Voto(4, 4, 3, 1),
            Voto(5, 5, 4, 1),
        ]

        generador_entregado4 = (element for element in lista_entregada4)

        Ponderador = namedtuple("Ponderador", ["especie", "ponderador"])

        lista_entregada5 = [
            Ponderador("Perro", 5.5),
            Ponderador("Gato", 1),
            Ponderador("Gallina", 0.01),
        ]

        generador_entregado5 = (element for element in lista_entregada5)

        resultado_estudiante = votantes_validos_por_distritos(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            generador_entregado4,
            generador_entregado5,
        )

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]
        resultado_considerando_la_edad = [
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_4(self):
        """
        Verifica que el test funcione para para tests pequeños. Caso empate.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(1, "Gay", "Gallina", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 248, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 116, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=3, id_votantes=[4]),
            Locales(id_local=4, nombre_local="Local 4", id_comuna=3, id_votantes=[5]),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada4 = [
            Voto(1, 1, 0, 5),
            Voto(2, 2, 1, 3),
            Voto(3, 3, 2, 1),
            Voto(4, 4, 3, 1),
            Voto(5, 5, 4, 1),
        ]

        generador_entregado4 = (element for element in lista_entregada4)

        Ponderador = namedtuple("Ponderador", ["especie", "ponderador"])

        lista_entregada5 = [
            Ponderador("Perro", 5.5),
            Ponderador("Gato", 1),
            Ponderador("Gallina", 0.01),
        ]

        generador_entregado5 = (element for element in lista_entregada5)

        resultado_estudiante = votantes_validos_por_distritos(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            generador_entregado4,
            generador_entregado5,
        )

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(1, "Gay", "Gallina", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 248, 0.525, 67, "1957/12"),
        ]
        resultado_considerando_la_edad = [
            Animal(1, "Gay", "Gallina", 190, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 61, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 248, 0.525, 67, "1957/12"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_5(self):
        """
        Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_l = cargar_datos("locales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = votantes_validos_por_distritos(g_a, g_d, g_l, g_v, g_p)

        resultado_considerando_la_edad = VOTANTES_VALIDOS_POR_DISTRITOS_S
        resultado_considerando_el_ano = VOTANTES_VALIDOS_POR_DISTRITOS_S_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_considerando_el_ano)

    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_l = cargar_datos("locales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = votantes_validos_por_distritos(g_a, g_d, g_l, g_v, g_p)

        resultado_considerando_la_edad = VOTANTES_VALIDOS_POR_DISTRITOS_M
        resultado_considerando_el_ano = VOTANTES_VALIDOS_POR_DISTRITOS_M_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_considerando_el_ano)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_l = cargar_datos("locales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v = cargar_datos("votos", carpeta)
        resultado = votantes_validos_por_distritos(g_a, g_d, g_l, g_v, g_p)

        resultado_considerando_la_edad = VOTANTES_VALIDOS_POR_DISTRITOS_L
        resultado_considerando_el_ano = VOTANTES_VALIDOS_POR_DISTRITOS_L_A
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        list_resultado = list(resultado)

        try:
            self.assertCountEqual(list_resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_considerando_el_ano)


if __name__ == "__main__":
    unittest.main(verbosity=2)
