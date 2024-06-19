import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animal_mas_viejo_edad_humana


class TestAnimalMasViejoEdadHumanaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Registro(id=93, nombre="Gay", especie="Tortuga", id_comuna=190, peso_kg=288.0, edad=1, fecha_nacimiento="2023/7"),
            Registro(id=94, nombre="Lexi", especie="Perro", id_comuna=61, peso_kg=0.071, edad=1, fecha_nacimiento="2023/8"),
            Registro(id=95, nombre="Ernst", especie="Gato", id_comuna=116, peso_kg=81.0, edad=1, fecha_nacimiento="2023/9"),
            Registro(id=96, nombre="Shreya", especie="Conejo", id_comuna=292, peso_kg=7.8, edad=1, fecha_nacimiento="2023/12"),
            Registro(id=97, nombre="Johanna", especie="Canario", id_comuna=248, peso_kg=0.525, edad=1, fecha_nacimiento="2023/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada2 = [
            Ponderador('Perro', 5.5),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 1),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10000),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 0.16),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 0.016)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = animal_mas_viejo_edad_humana(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [nombre for nombre in resultado_estudiante]

        resultado_considerando_el_ano = [
            "Gay"
        ]
        resultado_considerando_la_edad = [
            "Gay"
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

 
    def test_1(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Registro(id=93, nombre="Gay", especie="Tortuga", id_comuna=190, peso_kg=288.0, edad=10, fecha_nacimiento="2014/7"),
            Registro(id=94, nombre="Lexi", especie="Perro", id_comuna=61, peso_kg=0.071, edad=17, fecha_nacimiento="2007/8"),
            Registro(id=95, nombre="Ernst", especie="Gato", id_comuna=116, peso_kg=81.0, edad=5, fecha_nacimiento="2019/9"),
            Registro(id=96, nombre="Shreya", especie="Conejo", id_comuna=292, peso_kg=7.8, edad=12, fecha_nacimiento="2012/2"),
            Registro(id=97, nombre="Johanna", especie="Rata", id_comuna=248, peso_kg=0.525, edad=40, fecha_nacimiento="1984/12"),
            Registro(id=98, nombre="Arnold", especie="Pez dorado", id_comuna=248, peso_kg=0.525, edad=40, fecha_nacimiento="1984/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada2 = [
            Ponderador('Perro', 5.5),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 0.16),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 0.016)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = animal_mas_viejo_edad_humana(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [nombre for nombre in resultado_estudiante]

        resultado_considerando_el_ano = [
            "Arnold"
        ]
        resultado_considerando_la_edad = [
            "Arnold"
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_2(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Registro(id=93, nombre="Gay", especie="Tortuga", id_comuna=190, peso_kg=288.0, edad=10, fecha_nacimiento="2014/7"),
            Registro(id=94, nombre="Lexi", especie="Perro", id_comuna=61, peso_kg=0.071, edad=17, fecha_nacimiento="2007/8"),
            Registro(id=95, nombre="Ernst", especie="Gato", id_comuna=116, peso_kg=81.0, edad=5, fecha_nacimiento="2019/9"),
            Registro(id=96, nombre="Shreya", especie="Conejo", id_comuna=292, peso_kg=7.8, edad=12, fecha_nacimiento="2012/2"),
            Registro(id=97, nombre="Johanna", especie="Rata", id_comuna=248, peso_kg=0.525, edad=0, fecha_nacimiento="2024/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada2 = [
            Ponderador('Perro', 5.5),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 30.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 0.16),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 0.016)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = animal_mas_viejo_edad_humana(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [nombre for nombre in resultado_estudiante]

        resultado_considerando_el_ano = [
            "Shreya"
        ]
        resultado_considerando_la_edad = [
            "Shreya"
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_3(self):
        """
         Verifica que el test funcione para para tests pequeños. Caso empate.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Registro(id=93, nombre="Gay", especie="Tortuga", id_comuna=190, peso_kg=288.0, edad=10, fecha_nacimiento="2014/7"),
            Registro(id=94, nombre="Lexi", especie="Gato", id_comuna=61, peso_kg=0.071, edad=25, fecha_nacimiento="1999/8"),
            Registro(id=95, nombre="Ernst", especie="Rata", id_comuna=116, peso_kg=81.0, edad=5, fecha_nacimiento="2019/9"),
            Registro(id=96, nombre="Shreya", especie="Conejo", id_comuna=292, peso_kg=7.8, edad=12, fecha_nacimiento="2012/2"),
            Registro(id=97, nombre="Johanna", especie="Rata", id_comuna=248, peso_kg=0.525, edad=0, fecha_nacimiento="2024/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada2 = [
            Ponderador('Perro', 5.5),
            Ponderador('Gato', 2),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 20),
            Ponderador('Caballo', 0.16),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 0.016)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = animal_mas_viejo_edad_humana(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [nombre for nombre in resultado_estudiante]

        resultado_considerando_el_ano = [
            "Gay",
            "Ernst"
        ]
        resultado_considerando_la_edad = [
            "Gay",
            "Ernst"
        ]

        try:
            self.assertCountEqual(resultado_lista, resultado_considerando_el_ano)
        except AssertionError:
            self.assertCountEqual(resultado_lista, resultado_considerando_la_edad)

    def test_4(self):
        """
         Verifica que el test funcione para para tests pequeños. Caso empate múltiple
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Registro(id=93, nombre="Gay", especie="Tortuga", id_comuna=190, peso_kg=288.0, edad=10, fecha_nacimiento="2014/7"),
            Registro(id=94, nombre="Lexi", especie="Gato", id_comuna=61, peso_kg=0.071, edad=25, fecha_nacimiento="1999/8"),
            Registro(id=95, nombre="Ernst", especie="Perro", id_comuna=116, peso_kg=81.0, edad=5, fecha_nacimiento="2019/9"),
            Registro(id=96, nombre="Shreya", especie="Conejo", id_comuna=292, peso_kg=7.8, edad=12, fecha_nacimiento="2012/2"),
            Registro(id=97, nombre="Johanna", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=10, fecha_nacimiento="2014/12"),
            Registro(id=98, nombre="Pepe", especie="Tortuga", id_comuna=248, peso_kg=0.525, edad=10, fecha_nacimiento="2014/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada2 = [
            Ponderador('Perro', 5.5),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 0.16),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 0.016)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = animal_mas_viejo_edad_humana(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        resultado_lista = [nombre for nombre in resultado_estudiante]

        resultado_considerando_el_ano = [
            "Gay",
            "Lexi",
            "Johanna",
            "Pepe"
        ]
        resultado_considerando_la_edad = [
            "Gay",
            "Lexi",
            "Johanna",
            "Pepe"
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
