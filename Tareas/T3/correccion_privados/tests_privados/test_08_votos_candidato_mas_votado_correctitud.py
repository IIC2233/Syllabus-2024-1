import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_candidato_mas_votado

class TestVotosCandidatoMasVotadoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
         Verifica que el test funcione para generadores pequeños.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada = [
            Voto(1, 385, 1, 1055),
            Voto(2, 626, 1, 1055),
            Voto(3, 1272, 2, 1055),
            Voto(4, 1763, 2, 1055),
            Voto(5, 1846, 2, 1055),
            Voto(6, 1885, 2, 1055),
            Voto(7, 2055, 2, 1055),
            Voto(8, 2390, 2, 1055),
            Voto(9, 3055, 2, 1055),
            Voto(10, 3203, 3, 1055),
            Voto(11, 3227, 3, 1055),
            Voto(12, 3532, 3, 1055),
            Voto(13, 3559, 3, 1055),
            Voto(14, 3618, 3, 1055),
            Voto(15, 3667, 4, 1055),
            Voto(16, 3983, 5, 1055)
        ]

        generador_entregado = (element for element in lista_entregada)

        
        resultado_estudiante = votos_candidato_mas_votado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
        ]

        resultado_estudiante_lista = [voto_id for voto_id in resultado_estudiante]

        self.assertCountEqual(resultado_estudiante_lista, lista_esperada)

    def test_1(self):
        """
         Verifica que el test funcione para generadores pequeños.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2057),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 2055),
            Voto(12, 3532, 3, 2055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2060),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055),
            Voto(18, 3619, 3, 2055),
            Voto(19, 3669, 4, 2055),
            Voto(20, 3989, 5, 2055),
            Voto(21, 3979, 6, 2055)
        ]

        
        generador_entregado = (element for element in lista_entregada)

        
        resultado_estudiante = votos_candidato_mas_votado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            2,5,10,11,12,13,16,17,18,19,20,21
        ]

        resultado_estudiante_lista = [voto_id for voto_id in resultado_estudiante]

        self.assertCountEqual(resultado_estudiante_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione para generadores pequeños.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada = [
            Voto(1, 385, 1, 2055),
            Voto(2, 626, 1, 3055),
            Voto(3, 1272, 2, 2055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 2055),
            Voto(8, 2390, 2, 3055),
            Voto(9, 3055, 2, 2055),
            Voto(10, 3203, 3, 3055),
            Voto(11, 3227, 3, 2055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 3055),
            Voto(17, 3984, 6, 2055),
            Voto(18, 3988, 6, 2055),
            Voto(19, 3980, 6, 2055)
        ]
        
        generador_entregado = (element for element in lista_entregada)
        
        resultado_estudiante = votos_candidato_mas_votado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            1,3,5,7,9,11,13,15,17,18,19
        ]

        resultado_estudiante_lista = [voto_id for voto_id in resultado_estudiante]

        self.assertCountEqual(resultado_estudiante_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para generadores pequeños. Caso empate doble.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada = [
            Voto(1, 385, 1, 4055),
            Voto(2, 626, 1, 3055),
            Voto(3, 1272, 2, 4055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 4055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 4055),
            Voto(9, 3055, 2, 4055),
            Voto(10, 3203, 3, 3055),
            Voto(11, 3227, 3, 4055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 4055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 3055),
            Voto(16, 3983, 5, 4055),
        ]

        generador_entregado = (element for element in lista_entregada)
        
        resultado_estudiante = votos_candidato_mas_votado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            1,3,5,8,9,11,13,16
        ]

        resultado_estudiante_lista = [voto_id for voto_id in resultado_estudiante]

        self.assertCountEqual(resultado_estudiante_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione para generadores pequeños. Caso empate multiple.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada = [
            Voto(1, 385, 1, 1000),
            Voto(2, 626, 1, 2000),
            Voto(3, 1272, 2, 3000),
            Voto(4, 1763, 2, 4000),
            Voto(5, 1846, 2, 5000),
            Voto(6, 1885, 2, 1000),
            Voto(7, 2055, 2, 2000),
            Voto(8, 2390, 2, 3000),
            Voto(9, 3055, 2, 4000),
            Voto(10, 3203, 3, 5000),
            Voto(11, 3227, 3, 5557),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 6709),
            Voto(14, 3618, 3, 3055),
            Voto(14, 3550, 3, 6000),
            Voto(15, 3619, 3, 6000),
        ]

        generador_entregado = (element for element in lista_entregada)
        
        resultado_estudiante = votos_candidato_mas_votado(generador_entregado)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            14,15
        ]

        resultado_estudiante_lista = [voto_id for voto_id in resultado_estudiante]

        self.assertCountEqual(resultado_estudiante_lista, lista_esperada)
 


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
