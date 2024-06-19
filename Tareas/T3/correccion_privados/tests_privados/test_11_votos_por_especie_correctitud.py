import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_por_especie
from utilidades import Candidatos, Votos

class TestVotosPorEspecieCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne todas las especies cuando todos tienen votos.
        """
        lista_candidatos = [
            Candidatos(id_candidato= 1, nombre="Foca" ,         id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 2, nombre="Tomy" ,         id_distrito_postulacion= 1,     especie= "Gato" ),
            Candidatos(id_candidato= 3, nombre="Mancha" ,       id_distrito_postulacion= 4,     especie= "Gato" ),
            Candidatos(id_candidato= 5, nombre="Luna de mar" ,  id_distrito_postulacion= 4,     especie= "Pato"),
            Candidatos(id_candidato= 6, nombre="Guaton" ,       id_distrito_postulacion= 2,     especie= "Pato"),
            Candidatos(id_candidato= 9, nombre="Misifus" ,      id_distrito_postulacion= 5,     especie= "Perro" ),
        ]

        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 9), #Perro
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 1), #Perro
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 2), #Gato
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 2), #Gato
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 3), #Gato
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 3), #Gato
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 6), #Pato
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 5), #Pato
        ]
        
        expected_output = [("Perro", 2 ), ("Gato", 4), ("Pato", 2)]

        generador_candidato = (p for p in lista_candidatos)
        generador_voto = (p for p in lista_votos)
        resultado = votos_por_especie(generador_candidato ,generador_voto)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne todas las especies y votos cuando algunos no tienen Voto.
        """
        lista_candidatos = [
            Candidatos(id_candidato= 0, nombre="Enrique" ,      id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 1, nombre="Foca" ,         id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 2, nombre="Tomy" ,         id_distrito_postulacion= 1,     especie= "Gato" ),
            Candidatos(id_candidato= 3, nombre="Mancha" ,       id_distrito_postulacion= 4,     especie= "Gato" ),
            Candidatos(id_candidato= 4, nombre="Luna" ,         id_distrito_postulacion= 4,     especie= "Gallina"),
            Candidatos(id_candidato= 5, nombre="Luna de mar" ,  id_distrito_postulacion= 4,     especie= "Pato"),
            Candidatos(id_candidato= 6, nombre="Guaton" ,       id_distrito_postulacion= 2,     especie= "Pato"),
            Candidatos(id_candidato= 7, nombre="Gordis" ,       id_distrito_postulacion= 1,     especie= "Vaca"),
            Candidatos(id_candidato= 8, nombre="Cuello" ,       id_distrito_postulacion= 2,     especie= "Gato" ),
            Candidatos(id_candidato= 9, nombre="Misifus" ,      id_distrito_postulacion= 5,     especie= "Perro" ),
        ]

        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 9), #Perro
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 1), #Perro
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 2), #Gato
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 2), #Gato
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 3), #Gato
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 3), #Gato
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 6), #Pato
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 4), #Gallina
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 5), #Pato
        ]
        
        expected_output = [("Perro", 2 ), ("Gato", 4), ("Gallina", 1), ("Pato", 2), ("Vaca", 0)]

        generador_candidato = (p for p in lista_candidatos)
        generador_voto = (p for p in lista_votos)
        resultado = votos_por_especie(generador_candidato ,generador_voto)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne todas las especies y votos cuando algunos no tienen votos, pero la especie si.
        """
        lista_candidatos = [
            Candidatos(id_candidato= 0, nombre="Enrique" ,      id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 1, nombre="Foca" ,         id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 2, nombre="Tomy" ,         id_distrito_postulacion= 1,     especie= "Gato" ),
            Candidatos(id_candidato= 3, nombre="Mancha" ,       id_distrito_postulacion= 4,     especie= "Gato" ),
            Candidatos(id_candidato= 4, nombre="Luna" ,         id_distrito_postulacion= 4,     especie= "Gallina"),
            Candidatos(id_candidato= 5, nombre="Luna de mar" ,  id_distrito_postulacion= 4,     especie= "Pato"),
            Candidatos(id_candidato= 6, nombre="Guaton" ,       id_distrito_postulacion= 2,     especie= "Pato"),
            Candidatos(id_candidato= 8, nombre="Cuello" ,       id_distrito_postulacion= 2,     especie= "Gato" ),
            Candidatos(id_candidato= 9, nombre="Misifus" ,      id_distrito_postulacion= 5,     especie= "Perro" ),
        ]

        lista_votos = [
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 1), #Perro
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 2), #Gato
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 2), #Gato
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 3), #Gato
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 3), #Gato
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 6), #Pato
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 5), #Pato
        ]
        
        expected_output = [("Perro", 1 ), ("Gato", 4), ("Gallina", 0), ("Pato", 2)]

        generador_candidato = (p for p in lista_candidatos)
        generador_voto = (p for p in lista_votos)
        resultado = votos_por_especie(generador_candidato ,generador_voto)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_3(self):
        """
         Verifica que retorne todas las especies y votos cuando solo una especie tiene Votos.
        """
        lista_candidatos = [
            Candidatos(id_candidato= 0, nombre="Enrique" ,      id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 1, nombre="Foca" ,         id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 2, nombre="Tomy" ,         id_distrito_postulacion= 1,     especie= "Gato" ),
            Candidatos(id_candidato= 3, nombre="Mancha" ,       id_distrito_postulacion= 4,     especie= "Gato" ),
            Candidatos(id_candidato= 4, nombre="Luna" ,         id_distrito_postulacion= 4,     especie= "Gallina"),
            Candidatos(id_candidato= 5, nombre="Luna de mar" ,  id_distrito_postulacion= 4,     especie= "Pato"),
            Candidatos(id_candidato= 6, nombre="Guaton" ,       id_distrito_postulacion= 2,     especie= "Pato"),
            Candidatos(id_candidato= 7, nombre="Gordis" ,       id_distrito_postulacion= 1,     especie= "Vaca"),
            Candidatos(id_candidato= 8, nombre="Cuello" ,       id_distrito_postulacion= 2,     especie= "Gato" ),
            Candidatos(id_candidato= 9, nombre="Misifus" ,      id_distrito_postulacion= 5,     especie= "Perro" ),
        ]

        lista_votos = [
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 0), #Perro
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 0), #Perro
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 0), #Perro
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 0), #Perro
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 0), #Perro
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 0), #Perro
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 0), #Perro
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 0), #Perro
            Votos(id_voto= 9, id_animal_votante= 20,  id_local = 1, id_candidato= 0), #Perro
        ]
        
        expected_output = [("Perro", 9 ), ("Gato", 0), ("Gallina", 0), ("Pato", 0), ("Vaca", 0)]

        generador_candidato = (p for p in lista_candidatos)
        generador_voto = (p for p in lista_votos)
        resultado = votos_por_especie(generador_candidato ,generador_voto)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que retorne todas las especies y votos cuando no hay votos.
        """
        lista_candidatos = [
            Candidatos(id_candidato= 0, nombre="Enrique" ,      id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 1, nombre="Foca" ,         id_distrito_postulacion= 2,     especie= "Perro"),
            Candidatos(id_candidato= 2, nombre="Tomy" ,         id_distrito_postulacion= 1,     especie= "Gato" ),
            Candidatos(id_candidato= 3, nombre="Mancha" ,       id_distrito_postulacion= 4,     especie= "Gato" ),
            Candidatos(id_candidato= 4, nombre="Luna" ,         id_distrito_postulacion= 4,     especie= "Gallina"),
            Candidatos(id_candidato= 5, nombre="Luna de mar" ,  id_distrito_postulacion= 4,     especie= "Pato"),
            Candidatos(id_candidato= 6, nombre="Guaton" ,       id_distrito_postulacion= 2,     especie= "Pato"),
            Candidatos(id_candidato= 8, nombre="Cuello" ,       id_distrito_postulacion= 2,     especie= "Gato" ),
            Candidatos(id_candidato= 9, nombre="Misifus" ,      id_distrito_postulacion= 5,     especie= "Perro" ),
        ]

        lista_votos = [
        ]
        
        expected_output = [("Perro", 0), ("Gato", 0), ("Gallina", 0), ("Pato", 0)]

        generador_candidato = (p for p in lista_candidatos)
        generador_voto = (p for p in lista_votos)
        resultado = votos_por_especie(generador_candidato ,generador_voto)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
