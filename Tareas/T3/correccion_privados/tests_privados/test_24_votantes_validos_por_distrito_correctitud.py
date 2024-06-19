import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votantes_validos_por_distritos


class TestVotantesValidosPorDistritoCorrectitud(unittest.TestCase):

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
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 2, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 2, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(6, "Arthur", "Gato", 2, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3,6]),
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
            Voto(6, 6, 2, 5),
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

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 2, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 2, 0.525, 67, "1957/12"),
            Animal(6, "Arthur", "Gato", 2, 81.0, 60, "1964/9"),
        ]
        resultado_considerando_la_edad = [
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 2, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 2, 0.525, 67, "1957/12"),
            Animal(6, "Arthur", "Gato", 2, 81.0, 60, "1964/9"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)


    def test_1(self):
        self.maxDiff = None
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
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 2, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 3, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 3, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Perro", 3, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(3, "Distrito 3", 3, "Iquique", "Tarapaca"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=2, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=3, id_votantes=[3]),
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

        lista_entregada5 = [Ponderador("Perro", 0.1), Ponderador("Gato", 4)]

        generador_entregado5 = (element for element in lista_entregada5)

        resultado_estudiante = votantes_validos_por_distritos(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            generador_entregado4,
            generador_entregado5,
        )

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(2, "Lexi", "Gato", 2, 0.071, 34, "1990/8"),
        ]
        resultado_considerando_la_edad = [
            Animal(2, "Lexi", "Gato", 2, 0.071, 34, "1990/8"),
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
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 2, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 3, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=2, id_votantes=[]),
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

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 2, 0.525, 67, "1957/12"),
        ]
        resultado_considerando_la_edad = [
            Animal(1, "Gay", "Perro", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gato", 2, 0.525, 67, "1957/12"),
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
            Animal(1, "Gay", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Gallina", 2, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 3, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(6, "Pedro", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(7, "Thomas", "Gato", 3, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[1]),
            Locales(id_local=1, nombre_local="Local 1", id_comuna=1, id_votantes=[2]),
            Locales(id_local=2, nombre_local="Local 2", id_comuna=2, id_votantes=[3]),
            Locales(id_local=3, nombre_local="Local 3", id_comuna=3, id_votantes=[4,6]),
            Locales(id_local=4, nombre_local="Local 4", id_comuna=3, id_votantes=[5,7]),
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
            Voto(6, 6, 3, 1),
            Voto(7, 7, 4, 1),
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

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(4, "Phil", "Perro", 3, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(6, "Pedro", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(7, "Thomas", "Gato", 3, 81.0, 60, "1964/9"),
        ]
        resultado_considerando_la_edad = [
            Animal(4, "Phil", "Perro", 3, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(6, "Pedro", "Gato", 3, 81.0, 60, "1964/9"),
            Animal(7, "Thomas", "Gato", 3, 81.0, 60, "1964/9"),
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
            Animal(0, "Gary", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(1, "Gay", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 2, 0.525, 67, "1957/12"),
            Animal(4, "Phil", "Perro", 3, 0.525, 67, "1957/12"),
            Animal(5, "Ernst", "Gato", 3, 81.0, 60, "1964/9"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada2 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Locales = namedtuple("Locales", "id_local, nombre_local, id_comuna, id_votantes")

        lista_entregada3 = [
            Locales(id_local=0, nombre_local="Local 0", id_comuna=1, id_votantes=[0,1]),
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
            Voto(0, 0, 0, 5),
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

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [animal for animal in resultado_estudiante]

        resultado_considerando_el_ano = [
            Animal(0, "Gary", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(1, "Gay", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 2, 0.525, 67, "1957/12"),
        ]
        resultado_considerando_la_edad = [
            Animal(0, "Gary", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(1, "Gay", "Gallina", 1, 288.0, 45, "1979/11"),
            Animal(2, "Lexi", "Gato", 1, 0.071, 34, "1990/8"),
            Animal(3, "Toccara", "Perro", 2, 0.525, 67, "1957/12"),
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    
if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
