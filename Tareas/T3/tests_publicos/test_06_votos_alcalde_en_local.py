import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_alcalde_en_local, cargar_datos
from test_solution import VOTOS_ALCALDE_EN_LOCAL_S, VOTOS_ALCALDE_EN_LOCAL_M, VOTOS_ALCALDE_EN_LOCAL_L

class TestVotosAlcaldeEnLocal(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
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
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado = (voto for voto in lista_entregada)
        
        resultado_estudiante = votos_alcalde_en_local(generador_entregado, 3055, 1)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            Voto(1, 385, 1, 3055),
        ]

        resultado_lista = [voto for voto in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

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
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado = (voto for voto in lista_entregada)
        
        resultado_estudiante = votos_alcalde_en_local(generador_entregado, 2055, 5)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            Voto(16, 3983, 5, 2055),
        ]

        resultado_lista = [voto for voto in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
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
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado = (voto for voto in lista_entregada)
        
        resultado_estudiante = votos_alcalde_en_local(generador_entregado, 3055, 2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(9, 3055, 2, 3055),
        ]

        resultado_lista = [voto for voto in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para generadores pequeños. Caso: no hay votos en el local.
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
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 3055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado = (voto for voto in lista_entregada)
        
        resultado_estudiante = votos_alcalde_en_local(generador_entregado, 3055, 8)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
        ]

        resultado_lista = [voto for voto in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione para generadores pequeños. Caso: no hay votos para ese candidato en el local.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 4055),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 4055),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 2055),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado = (voto for voto in lista_entregada)
        
        resultado_estudiante = votos_alcalde_en_local(generador_entregado, 4055, 1)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator))

        lista_esperada = [
        ]

        resultado_lista = [voto for voto in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 1, 2)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 1, 2)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_v = cargar_datos("votos", carpeta)
        resultado = votos_alcalde_en_local(g_v, 1, 2)
        expected_output = VOTOS_ALCALDE_EN_LOCAL_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)       


if __name__ == "__main__":
    unittest.main(verbosity=2)
