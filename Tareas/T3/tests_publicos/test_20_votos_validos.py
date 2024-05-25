import sys
import unittest
from collections import namedtuple

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_validos, cargar_datos
from test_solution import VOTOS_VALIDOS_S, VOTOS_VALIDOS_M, VOTOS_VALIDOS_L, VOTOS_VALIDOS_S_A, VOTOS_VALIDOS_M_A, VOTOS_VALIDOS_L_A


class TestVotosValidos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
         Verifica que el test funcione para para tests pequeños. Todos validos
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Perro', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Perro', 61, 0.071, 67, '1957/8'),
                Animal(2055, 'Toccara', 'Gallina', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Caballo', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Rata', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Perro', 292, 7.8, 32, '1992/11'),
                Animal(531, 'Johanna', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Serpiente', 139, 0.0282, 84, '1939/2'),
                Animal(596, 'Ulysses', 'Elefante', 68, 0.0091, 78, '1945/1'),
                Animal(597, 'Alexandria', 'Gallina', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Gato', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Gato', 5, 1.38, 58, '1965/3'),
                Animal(600, 'Kobe', 'Tortuga', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Elefante', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Elefante', 212, 2.02, 63, '1960/3'),
                Animal(603, 'Lon', 'Gato', 201, 2.4, 82, '1941/2'),
                Animal(604, 'Darren', 'Gato', 41, 72.8, 60, '1963/1'),
                Animal(605, 'Tilden', 'Perro', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Serpiente', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Caballo', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 2055, 3, 2055),
            Voto(18, 3055, 3, 2055),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada3 = [
            Ponderador('Perro', 15.5),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 2.16),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 1.016)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_validos(generador_entregado1, generador_entregado2, generador_entregado3)

        resultado_considerando_el_ano = 9 
        resultado_considerando_la_edad = 9

        self.assertIn(resultado_estudiante, [resultado_considerando_el_ano, resultado_considerando_la_edad])


    def test_1(self):
        """
         Verifica que el test funcione para para tests pequeños. Ninguno válido.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Perro', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Perro', 61, 0.071, 67, '1957/8'),
                Animal(2055, 'Toccara', 'Gallina', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Caballo', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Rata', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Perro', 292, 7.8, 32, '1992/11'),
                Animal(531, 'Johanna', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Serpiente', 139, 0.0282, 84, '1939/2'),
                Animal(596, 'Ulysses', 'Elefante', 68, 0.0091, 78, '1945/1'),
                Animal(597, 'Alexandria', 'Gallina', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Gato', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Gato', 5, 1.38, 58, '1965/3'),
                Animal(600, 'Kobe', 'Tortuga', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Elefante', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Elefante', 212, 2.02, 63, '1960/3'),
                Animal(603, 'Lon', 'Gato', 201, 2.4, 82, '1941/2'),
                Animal(604, 'Darren', 'Gato', 41, 72.8, 60, '1963/1'),
                Animal(605, 'Tilden', 'Perro', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Serpiente', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Caballo', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 2055, 3, 2055),
            Voto(18, 3055, 3, 2055),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada3 = [
            Ponderador('Perro', 0.11),
            Ponderador('Gato', 0.10005),
            Ponderador('Conejo', 0.11),
            Ponderador('Canario', 0.1),
            Ponderador('Serpiente', 0),
            Ponderador('Tortuga', 0.0008),
            Ponderador('Pez dorado', 0.0007),
            Ponderador('Rata', 0.1),
            Ponderador('Caballo', 0.10005),
            Ponderador('Gallina', 0.1),
            Ponderador('Elefante', 0.001)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_validos(generador_entregado1, generador_entregado2, generador_entregado3)

        resultado_considerando_el_ano = 0 
        resultado_considerando_la_edad = 0

        self.assertIn(resultado_estudiante, [resultado_considerando_el_ano, resultado_considerando_la_edad])

    def test_2(self):
        """
         Verifica que el test funcione para para tests pequeños. Probando edades estrictamente iguales a 18.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Perro', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Perro', 61, 0.071, 67, '1957/8'),
                Animal(2055, 'Toccara', 'Gallina', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Caballo', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Rata', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Perro', 292, 7.8, 32, '1992/11'),
                Animal(531, 'Johanna', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Serpiente', 139, 0.0282, 84, '1939/2'),
                Animal(596, 'Ulysses', 'Elefante', 68, 0.0091, 78, '1945/1'),
                Animal(597, 'Alexandria', 'Gallina', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Gato', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Gato', 5, 1.38, 58, '1965/3'),
                Animal(600, 'Kobe', 'Tortuga', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Elefante', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Elefante', 212, 2.02, 63, '1960/3'),
                Animal(603, 'Lon', 'Gato', 201, 2.4, 82, '1941/2'),
                Animal(604, 'Darren', 'Gato', 41, 72.8, 60, '1963/1'),
                Animal(605, 'Tilden', 'Perro', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Serpiente', 293, 1.35, 18, '2006/10'),
                Animal(3984, 'Hollie', 'Caballo', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 2055, 3, 2055),
            Voto(18, 3055, 3, 2055),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada3 = [
            Ponderador('Perro', 0.11),
            Ponderador('Gato', 0.10005),
            Ponderador('Conejo', 0.11),
            Ponderador('Canario', 0.1),
            Ponderador('Serpiente', 1),
            Ponderador('Tortuga', 0.0008),
            Ponderador('Pez dorado', 0.0007),
            Ponderador('Rata', 0.1),
            Ponderador('Caballo', 0.10005),
            Ponderador('Gallina', 0.1),
            Ponderador('Elefante', 0.001)
        ]
        
        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_validos(generador_entregado1, generador_entregado2, generador_entregado3)

        resultado_considerando_el_ano = 1
        resultado_considerando_la_edad = 1

        self.assertIn(resultado_estudiante, [resultado_considerando_el_ano, resultado_considerando_la_edad])

    def test_3(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Perro', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Perro', 61, 0.071, 67, '1957/8'),
                Animal(2055, 'Toccara', 'Gallina', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Caballo', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Rata', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Perro', 292, 7.8, 32, '1992/11'),
                Animal(531, 'Johanna', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Serpiente', 139, 0.0282, 84, '1939/2'),
                Animal(596, 'Ulysses', 'Elefante', 68, 0.0091, 78, '1945/1'),
                Animal(597, 'Alexandria', 'Gallina', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Gato', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Gato', 5, 1.38, 58, '1965/3'),
                Animal(600, 'Kobe', 'Tortuga', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Elefante', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Elefante', 212, 2.02, 63, '1960/3'),
                Animal(603, 'Lon', 'Gato', 201, 2.4, 82, '1941/2'),
                Animal(604, 'Darren', 'Gato', 41, 72.8, 60, '1963/1'),
                Animal(605, 'Tilden', 'Perro', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Serpiente', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Caballo', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 2055, 3, 2055),
            Voto(18, 3055, 3, 2055),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada3 = [
            Ponderador('Perro', 15.5),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 10),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 0.001),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 1.016)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_validos(generador_entregado1, generador_entregado2, generador_entregado3)

        resultado_considerando_el_ano = 8 
        resultado_considerando_la_edad = 8

        self.assertIn(resultado_estudiante, [resultado_considerando_el_ano, resultado_considerando_la_edad])

    def test_4(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Perro', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Perro', 61, 0.071, 67, '1957/8'),
                Animal(2055, 'Toccara', 'Gallina', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Caballo', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Rata', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Perro', 292, 7.8, 32, '1992/11'),
                Animal(531, 'Johanna', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Serpiente', 139, 0.0282, 84, '1939/2'),
                Animal(596, 'Ulysses', 'Elefante', 68, 0.0091, 78, '1945/1'),
                Animal(597, 'Alexandria', 'Gallina', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Gato', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Gato', 5, 1.38, 58, '1965/3'),
                Animal(600, 'Kobe', 'Tortuga', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Elefante', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Elefante', 212, 2.02, 63, '1960/3'),
                Animal(603, 'Lon', 'Gato', 201, 2.4, 82, '1941/2'),
                Animal(604, 'Darren', 'Gato', 41, 72.8, 60, '1963/1'),
                Animal(605, 'Tilden', 'Perro', 23, 0.056, 18, '2006/10'),
                Animal(606, 'Maryanne', 'Serpiente', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Caballo', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 2055, 3, 2055),
            Voto(18, 3055, 3, 2055),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Ponderador = namedtuple('Ponderador', ['especie', 'ponderador'])

        lista_entregada3 = [
            Ponderador('Perro', 1.0),
            Ponderador('Gato', 4),
            Ponderador('Conejo', 7.5),
            Ponderador('Canario', 2666.67),
            Ponderador('Serpiente', 22.86),
            Ponderador('Tortuga', 0.00001),
            Ponderador('Pez dorado', 800),
            Ponderador('Rata', 160),
            Ponderador('Caballo', 0.001),
            Ponderador('Gallina', 32),
            Ponderador('Elefante', 1.016)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_validos(generador_entregado1, generador_entregado2, generador_entregado3)

        resultado_considerando_el_ano = 7 
        resultado_considerando_la_edad = 7

        self.assertIn(resultado_estudiante, [resultado_considerando_el_ano, resultado_considerando_la_edad])
    
    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos(g_a, g_v, g_p)
        
        resultado_considerando_la_edad = VOTOS_VALIDOS_S
        resultado_considerando_el_ano = VOTOS_VALIDOS_S_A

        try:
            self.assertEqual(resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertEqual(resultado, resultado_considerando_el_ano)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos(g_a, g_v, g_p)

        resultado_considerando_la_edad = VOTOS_VALIDOS_M
        resultado_considerando_el_ano = VOTOS_VALIDOS_M_A

        try:
            self.assertEqual(resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertEqual(resultado, resultado_considerando_el_ano)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votos_validos(g_a, g_v, g_p)

        resultado_considerando_la_edad = VOTOS_VALIDOS_L
        resultado_considerando_el_ano = VOTOS_VALIDOS_L_A

        try:
            self.assertEqual(resultado, resultado_considerando_la_edad)
        except AssertionError:
            self.assertEqual(resultado, resultado_considerando_el_ano)

if __name__ == "__main__":
    unittest.main(verbosity=2)
