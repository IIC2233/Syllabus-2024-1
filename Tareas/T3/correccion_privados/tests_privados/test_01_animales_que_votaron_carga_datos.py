import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_que_votaron_por, cargar_datos
from utilidades import Votos
from test_solution import ANIMALES_QUE_VOTARON_POR_S, ANIMALES_QUE_VOTARON_POR_M, ANIMALES_QUE_VOTARON_POR_L, ANIMALES_QUE_VOTARON_POR_S_2, ANIMALES_QUE_VOTARON_POR_M_2, ANIMALES_QUE_VOTARON_POR_L_2

from timeout_function import timeout
N_SECOND = 20 

class TestAnimalesQueVotaronPorCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos. (Retorna generador vacío)
        """
        carpeta = "s"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 4611)
        expected_output = ANIMALES_QUE_VOTARON_POR_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos. (Retorna generador vacío)
        """
        carpeta = "m"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 11825)
        expected_output = ANIMALES_QUE_VOTARON_POR_M
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos. (Retorna generador vacío)
        """
        carpeta = "l"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 995616)
        expected_output = ANIMALES_QUE_VOTARON_POR_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    @timeout(N_SECOND)
    def test_8(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos. (Retorna generador no vacío)
        """
        carpeta = "s"
        generador_voto = cargar_datos("votos", carpeta)
        resultado = animales_que_votaron_por(generador_voto, 7)
        expected_output = ANIMALES_QUE_VOTARON_POR_S_2
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)



if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
