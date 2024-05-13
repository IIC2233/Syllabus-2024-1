import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_segun_edad, cargar_datos
from test_solution import ANIMALES_SEGUN_EDAD_S, ANIMALES_SEGUN_EDAD_M, ANIMALES_SEGUN_EDAD_L

class TestAnimalesSegunEdad(unittest.TestCase):

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
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=60, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)

        resultado_estudiante = animales_segun_edad(generador_entregado, "=", 60)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            "Ernst",
            "Johanna"
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
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)

        resultado_estudiante = animales_segun_edad(generador_entregado, ">", 1)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            "Gay",
            "Lexi",
            "Ernst",
            "Shreya",
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
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)
        
        resultado_estudiante = animales_segun_edad(generador_entregado, "<", 40)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            "Lexi",
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
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)
        
        resultado_estudiante = animales_segun_edad(generador_entregado, ">", 31)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            "Gay",
            "Lexi",
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
            Registro(id=96, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/2"),
            Registro(id=97, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado = (animal for animal in lista_entregada)

        resultado_estudiante = animales_segun_edad(generador_entregado, "=", 1)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))
        
        
        lista_esperada = [
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_5(self):
        """
         Verifica que el test funcione para pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        resultado = animales_segun_edad(g_a, "<", 10)
        expected_output = ANIMALES_SEGUN_EDAD_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_6(self):
        """
         Verifica que el test funcione para medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        resultado = animales_segun_edad(g_a, "<", 10)
        expected_output = ANIMALES_SEGUN_EDAD_M
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
         Verifica que el test funcione para grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        resultado = animales_segun_edad(g_a, "<", 10)
        expected_output = ANIMALES_SEGUN_EDAD_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
