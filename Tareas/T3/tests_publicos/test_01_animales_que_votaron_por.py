import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_que_votaron_por, cargar_datos
from utilidades import Votos
from test_solution import ANIMALES_QUE_VOTARON_POR_S, ANIMALES_QUE_VOTARON_POR_M, ANIMALES_QUE_VOTARON_POR_L


class TestAnimalesQueVotaronPor(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que se retorne los votantes cuando el candidato tiene 1 voto.
        """
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 2), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 1), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
        ]

        expected_output = [5]

        generador_voto = (p for p in lista_votos)
        resultado = animales_que_votaron_por(generador_voto, 1)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que se retorne los votantes cuando el candidato tiene varios voto.
        """
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 1), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 1), 
        ]

        expected_output = [1, 5, 8]

        generador_voto = (p for p in lista_votos)
        resultado = animales_que_votaron_por(generador_voto, 1)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que se retorne un generador vacío cuando el candidato no tiene votos.
        """
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 1), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 1), 
        ]

        expected_output = []

        generador_voto = (p for p in lista_votos)
        resultado = animales_que_votaron_por(generador_voto, 10)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_3(self):
        """
         Verifica que se retorne los votantes cuando el candidato tiene todos los votos.
        """
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 3), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 3), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 3), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 3), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 3), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 3), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 3), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 3), 
        ]

        expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        generador_voto = (p for p in lista_votos)
        resultado = animales_que_votaron_por(generador_voto, 3)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que se retorne los votantes cuando el candidato tiene casi todos los votos.
        """
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 3), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 3), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 3), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 3), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 3), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 3), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 3), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 3), 
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 9, id_candidato= 1), 
            Votos(id_voto= 10, id_animal_votante= 10,  id_local = 9, id_candidato= 3), 
        ]

        expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10]

        generador_voto = (p for p in lista_votos)
        resultado = animales_que_votaron_por(generador_voto, 3)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 3)
        expected_output = ANIMALES_QUE_VOTARON_POR_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 3)
        expected_output = ANIMALES_QUE_VOTARON_POR_M
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 3)
        expected_output = ANIMALES_QUE_VOTARON_POR_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
