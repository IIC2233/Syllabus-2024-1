import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votaron_por_si_mismos, cargar_datos
from test_solution import VOTARON_POR_SI_MISMOS_S, VOTARON_POR_SI_MISMOS_M, VOTARON_POR_SI_MISMOS_L

class TestVotaronPorSiMismos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada1 = [
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
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = votaron_por_si_mismos(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            'Phil'
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_1(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada1 = [
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
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 2055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = votaron_por_si_mismos(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            'Phil',
            'Toccara'
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada1 = [
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
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 2055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 6493, 3, 6493),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]


        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = votaron_por_si_mismos(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            'Marylyn'
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para para tests pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada1 = [
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
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 5385, 1, 5385),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 2055),
            Voto(10, 81, 3, 81),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 4018, 6, 4018)
        ]


        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = votaron_por_si_mismos(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            'Joetta',
            'Mose',
            'Judi'
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione para para tests pequeños. Caso generador vacío.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada1 = [
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
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 2055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2056),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]


        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = votaron_por_si_mismos(generador_entregado1, generador_entregado2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
        ]

        resultado_lista = [nombre for nombre in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votaron_por_si_mismos(g_c, g_v)
        expected_output = VOTARON_POR_SI_MISMOS_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votaron_por_si_mismos(g_c, g_v)
        expected_output = VOTARON_POR_SI_MISMOS_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = votaron_por_si_mismos(g_c, g_v)
        expected_output = VOTARON_POR_SI_MISMOS_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

if __name__ == "__main__":
    unittest.main(verbosity=2)
