
import sys
import unittest
from collections import namedtuple

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import cantidad_votos_candidato


class TestCantidadVotosCandidatoCorrectitud(unittest.TestCase):

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

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 100)
        
        self.assertEqual(resultado_estudiante, 0)


    def test_1(self):
        """
         Verifica que el test funcione cuando todos votan por el candidato.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
            Voto(1, 385, 1,2055),
            Voto(2, 626, 1, 2055),
            Voto(3, 1272, 2, 2055),
            Voto(4, 1763, 2, 2055),
            Voto(5, 1846, 2, 2055),
            Voto(6, 1885, 2, 2055),
            Voto(7, 2055, 2, 2055),

        ]

        generador_entregado = (voto for voto in lista_votos)

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 2055)
        
        self.assertEqual(resultado_estudiante, 7)

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

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 3055)
        
        self.assertEqual(resultado_estudiante, 9)

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
            Voto(5, 1846, 2, 2058),
            Voto(6, 1885, 2, 3055),
            Voto(7, 2055, 2, 3055),
            Voto(8, 2390, 2, 2058),
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

        resultado_estudiante = cantidad_votos_candidato(generador_entregado, 2058)
        
        self.assertEqual(resultado_estudiante, 2)


    def test_4(self):
        """
         Verifica que el test funcione para intancias pequeñas.
        """

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_votos = [
            Voto(1, 385, 1, 3055),
            Voto(2, 626, 1, 1111),
            Voto(3, 1272, 2, 3055),
            Voto(4, 1763, 2, 1111),
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
        
        self.assertEqual(resultado_estudiante, 5)

if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
