import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import mismo_mes_candidato, cargar_datos
from test_solution import MISMO_MES_CANDIDATO_S, MISMO_MES_CANDIDATO_M, MISMO_MES_CANDIDATO_L

class TestMismoMesCandidato(unittest.TestCase):

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
            Animal(id=1763, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1990/8"),
            Animal(id=3, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3056, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatí de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 385, 1, 531),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 531),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3056, 2, 531),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 531)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            385,
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
            Animal(id=1763, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1957/8"),
            Animal(id=3, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3056, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/11"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1957/12")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatí de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 385, 1, 531),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 531),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3056, 2, 531),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 531)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            1763
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione para para tests pequeños. Mismo mes y/o año.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=626, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1992/12"),
            Animal(id=1846, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1992/8"),
            Animal(id=2390, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3203, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1992/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/12"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatí de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 385, 1, 531),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 531),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3056, 2, 531),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2045),
            Voto(16, 3983, 5, 2045),
            Voto(17, 3984, 6, 2045)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 2055)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            626,
            1846,
            3203
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para para tests pequeños. No existe candidato.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=626, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1992/12"),
            Animal(id=1846, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1992/8"),
            Animal(id=2390, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3203, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1992/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/12"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatí de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 385, 1, 531),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 531),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3056, 2, 531),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2045),
            Voto(16, 3983, 5, 2045),
            Voto(17, 3984, 6, 2045)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione para para tests pequeños. No hay votos para el candidato.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
            Animal(id=626, nombre="Gay", especie="Tortuga marina", id_comuna=190, peso_kg=288.0, edad=45, fecha_nacimiento="1992/12"),
            Animal(id=1846, nombre="Lexi", especie="Gecko", id_comuna=61, peso_kg=0.071, edad=34, fecha_nacimiento="1992/8"),
            Animal(id=2390, nombre="Ernst", especie="Llama", id_comuna=116, peso_kg=81.0, edad=60, fecha_nacimiento="1964/9"),
            Animal(id=3203, nombre="Shreya", especie="Coati", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1993/12"),
            Animal(id=531, nombre="Johanna", especie="Langosta", id_comuna=248, peso_kg=0.525, edad=67, fecha_nacimiento="1992/12"),
            Animal(id=2055, nombre="Toccara", especie="Medusa", id_comuna=292, peso_kg=7.8, edad=31, fecha_nacimiento="1992/12"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada2 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatí de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada3 = [
            Voto(1, 385, 1, 531),
            Voto(2, 626, 1, 2050),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 531),
            Voto(5, 1846, 2, 2051),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2057),
            Voto(9, 3056, 2, 531),
            Voto(10, 3203, 3, 3055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2045),
            Voto(16, 3983, 5, 2045),
            Voto(17, 3984, 6, 2045)
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = mismo_mes_candidato(generador_entregado1, generador_entregado2, generador_entregado3, 2055)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = []

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 1)
        expected_output = MISMO_MES_CANDIDATO_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 1)
        expected_output = MISMO_MES_CANDIDATO_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = mismo_mes_candidato(g_a,  g_c, g_v, 1)
        expected_output = MISMO_MES_CANDIDATO_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
