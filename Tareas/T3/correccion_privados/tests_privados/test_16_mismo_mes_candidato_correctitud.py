import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import mismo_mes_candidato

class TestMismoMesCandidatoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que el test funcione para para tests pequeños. Mismo mes.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=385, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/12"),
            Animal(id=386, nombre="Sofie", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/12"),
            Animal(id=1763, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Animal(id=3, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3056, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/12"),
            Animal(id=3057, nombre="Thomas", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=81, nombre="Joetta", especie="Buho", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=3, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=59, fecha_nacimiento="1965/6"),
            Animal(id=3055, nombre="Phil", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 386, 1, 531),
            Voto(4, 1763, 2, 531),
            Voto(7, 2055, 2, 3055),
            Voto(9, 3056, 2, 531),
            Voto(10, 3, 3, 2055),
            Voto(14, 385, 3, 3055),
            Voto(15, 3057, 4, 2055),
            Voto(16, 531, 5, 2055),
            Voto(17, 2055, 6, 2055),
            Voto(18, 81, 6, 2055)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 531)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            386,
            3056
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_1(self):
        """
         Verifica que el test funcione para para tests pequeños. Mismo año.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=385, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/11"),
            Animal(id=1768, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=67, fecha_nacimiento="1957/8"),
            Animal(id=3, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=2056, nombre="Kellen", especie="Pinguino emperador", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/11"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=3055, nombre="Phil", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=81, nombre="Joetta", especie="Buho", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
            Animal(id=626, nombre="Thomas", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(2056, 'Kellen', 2, 'Pinguino emperador'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 385, 1, 531),
            Voto(2, 626, 1, 2055),
            Voto(4, 1768, 2, 531),
            Voto(5, 3, 2, 2055),
            Voto(6, 626, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 531)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            1768
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione para para tests pequeños. Mismo mes y/o año.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=626, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=627, nombre="Thomas", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=1846, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=32, fecha_nacimiento="1992/8"),
            Animal(id=2390, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3203, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=3055, nombre="Phil", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(2, 626, 1, 2055),
            Voto(5, 1846, 2, 2055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(10, 3203, 3, 2055),
            Voto(18, 627, 1, 2055)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 2055)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            626,
            1846,
            3203,
            627
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=626, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=1846, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=32, fecha_nacimiento="1992/8"),
            Animal(id=2390, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3203, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3204, nombre="Freya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=3055, nombre="Phil", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/1"),
            Animal(id=2045, nombre="Shreya", especie="Coati", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/7"),
            Animal(id=2056, nombre="Joan", especie="Medusa", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/7"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(2045, 'Shreya', 6, 'Coati'),
            Candidato(2056, 'Joan', 6, 'Medusa'),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(2, 626, 1, 2055),
            Voto(5, 3204, 2, 2045),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 2056, 2, 531),
            Voto(10, 3203, 3, 2055),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione para para tests pequeños. No hay votante que cumpla con la condicion.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=626, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=1846, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=32, fecha_nacimiento="1992/8"),
            Animal(id=2390, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3203, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/12"),
            Animal(id=3055, nombre="Phil", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/1"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 626, 1, 531),
            Voto(3, 1846, 2, 3055),
            Voto(4, 2390, 2, 531),
            Voto(6, 3203, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(17, 3055, 6, 2055)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 2055)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = []

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
