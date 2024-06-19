import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_segun_edad

class TestAnimalesSegunEdadCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que el test funcione para el operador "=" y para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada = [
            Registro(id=93, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/7"),
            Registro(id=94, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Registro(id=95, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=57, fecha_nacimiento="1967/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)

        resultado_estudiante = animales_segun_edad(generador_entregado, "=", 45)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            "Gay"
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_1(self):
        """
         Verifica que el test funcione para el operador ">" y para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada = [
            Registro(id=93, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/7"),
            Registro(id=94, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Registro(id=95, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)

        resultado_estudiante = animales_segun_edad(generador_entregado, ">", 38)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            "Gay",
            "Ernst",
            "Johanna"
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione para el operador "<" y para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada = [
            Registro(id=93, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/7"),
            Registro(id=94, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Registro(id=95, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)
        
        resultado_estudiante = animales_segun_edad(generador_entregado, "<", 65)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            "Gay",
            "Lexi",
            "Ernst",
            "Shreya"
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para el operador ">" y para tests pequeños.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada = [
            Registro(id=93, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/7"),
            Registro(id=94, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Registro(id=95, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)
        
        resultado_estudiante = animales_segun_edad(generador_entregado, ">", 40)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            "Gay",
            "Ernst",
            "Johanna"
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione cuando se retornan generadores vacíos.
        """

        Registro = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada = [
            Registro(id=93, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1979/7"),
            Registro(id=94, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Registro(id=95, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=32, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)

        resultado_estudiante = animales_segun_edad(generador_entregado, "=", 100)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))
        
        
        lista_esperada = [
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
