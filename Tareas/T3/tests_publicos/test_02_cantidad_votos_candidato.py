
import sys
import unittest
from collections import namedtuple

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import cantidad_votos_candidato, cargar_datos
from test_solution import CANTIDAD_VOTOS_CANDIDATO_S, CANTIDAD_VOTOS_CANDIDATO_M, CANTIDAD_VOTOS_CANDIDATO_L



class TestCantidadVotosCandidato(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que el test funcione cuando nadie vota por el candidato.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
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

        generador_entregado = (voto for voto in lista_votos)

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 1)
        
        self.assertEqual(resultado_estudiante, 0)


    def test_1(self):
        """
         Verifica que el test funcione cuando todos votan por el candidato.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 3055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 3055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 3055),
        ]

        generador_entregado = (voto for voto in lista_votos)

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 3055)
        
        self.assertEqual(resultado_estudiante, 8)

    def test_2(self):
        """
         Verifica que el test funcione para instancias pequeñas.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
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

        generador_entregado = (voto for voto in lista_votos)

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 2055)
        
        self.assertEqual(resultado_estudiante, 8)

    def test_3(self):
        """
         Verifica que el test funcione para instancias pequeñas.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
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

        generador_entregado = (voto for voto in lista_votos)

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 2056)
        
        self.assertEqual(resultado_estudiante, 1)


    def test_4(self):
        """
         Verifica que el test funcione para intancias pequeñas.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 3055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 1111),
            Voto(8, 2390, 2, 2055),
            Voto(9, 3055, 2, 3055),
            Voto(10, 3203, 3, 2055),
            Voto(11, 3227, 3, 1111),
            Voto(12, 3532, 3, 3055),
            Voto(13, 3559, 3, 2055),
            Voto(14, 3618, 3, 3055),
            Voto(15, 3667, 4, 1111),
            Voto(16, 3983, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]
        
        generador_entregado = (voto for voto in lista_votos)

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 1111)
        
        self.assertEqual(resultado_estudiante, 3)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_candidato(g_v, 4)
        expected_output = CANTIDAD_VOTOS_CANDIDATO_S
        
        self.assertEqual(resultado, expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_candidato(g_v, 4)
        expected_output = CANTIDAD_VOTOS_CANDIDATO_M
        
        self.assertEqual(resultado, expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_v = cargar_datos("votos", carpeta)
        resultado = cantidad_votos_candidato(g_v, 4)
        expected_output = CANTIDAD_VOTOS_CANDIDATO_L
        
        self.assertEqual(resultado, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
