import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import ganadores_por_distrito, cargar_datos
from utilidades import Candidatos, Votos
from test_solution import GANADORES_POR_DISTRITO_S, GANADORES_POR_DISTRITO_M, GANADORES_POR_DISTRITO_L

class TestGanadoresPorDistrito(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne los candidatos ganadores por pares, cuando solo se postula un animal por distrito.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=0,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=9,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=8,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=7,   especie='Gato'),
            Candidatos(id_candidato=5, nombre='Auto Motor',                 id_distrito_postulacion=6,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=5,   especie='Gato Chico'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=4,   especie='Perro Danes'),
            Candidatos(id_candidato=8, nombre='Dona Dulce',                 id_distrito_postulacion=3,   especie='Elefante'),
            Candidatos(id_candidato=9, nombre='Alberto',                    id_distrito_postulacion=2,   especie='Delfin'),
            Candidatos(id_candidato=0, nombre='Peaje Autopista',            id_distrito_postulacion=1,   especie='Gallina'),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 9),
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 1),
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 2),
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 3),
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 6),
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 5),
        ]
        
        expected_output = []

        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)

        resultado = ganadores_por_distrito(generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne los candidatos ganadores por pares, cuando se postulan 2 por distrito y siempre hay un solo ganador.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=2,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=1,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=1,   especie='Gato'),
            Candidatos(id_candidato=5, nombre='Auto Motor',                 id_distrito_postulacion=5,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=5,   especie='Gato Chico'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Perro Danes'),
            Candidatos(id_candidato=8, nombre='Dona Dulce',                 id_distrito_postulacion=7,   especie='Elefante'),
            Candidatos(id_candidato=9, nombre='Alberto',                    id_distrito_postulacion=9,   especie='Delfin'),
            Candidatos(id_candidato=0, nombre='Peaje Autopista',            id_distrito_postulacion=9,   especie='Gallina'),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 2),
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 2),
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 4),
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 4), 
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 5), 
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 5),
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 7),
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 9),
            Votos(id_voto= 9, id_animal_votante= 20,  id_local = 9, id_candidato= 9),
        ]
        
        expected_output = ['Sr. Cortizona', 'Alan Brito Delgado', 'Auto Motor', 'Maria', 'Alberto']

        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = ganadores_por_distrito(generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne los candidatos ganadores por pares, cuando se postulan 2 por distrito y hay empates.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=2,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=1,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=1,   especie='Gato'),
            Candidatos(id_candidato=5, nombre='Auto Motor',                 id_distrito_postulacion=5,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=5,   especie='Gato Chico'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Perro Danes'),
            Candidatos(id_candidato=8, nombre='Dona Dulce',                 id_distrito_postulacion=7,   especie='Elefante'),
            Candidatos(id_candidato=9, nombre='Alberto',                    id_distrito_postulacion=9,   especie='Delfin'),
            Candidatos(id_candidato=0, nombre='Peaje Autopista',            id_distrito_postulacion=9,   especie='Gallina'),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 1),
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 2),
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 3),
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 4), 
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 5), 
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 5),
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 7),
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 9),
            Votos(id_voto= 9, id_animal_votante= 20,  id_local = 9, id_candidato= 9),
        ]
        
        expected_output = ['Don Pepe','Sr. Cortizona', 'Calvo Calvin', 'Alan Brito Delgado', 'Auto Motor', 'Maria', 'Alberto']

        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = ganadores_por_distrito(generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_3(self):
        """
         Verifica que retorne los candidatos ganadores por pares, cuando se postulan 3 por distrito sin empates.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=2,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=2,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=5, nombre='Auto Motor',                 id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=3,   especie='Gato Chico'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Perro Danes'),
            Candidatos(id_candidato=8, nombre='Dona Dulce',                 id_distrito_postulacion=7,   especie='Elefante'),
            Candidatos(id_candidato=9, nombre='Alberto',                    id_distrito_postulacion=7,   especie='Delfin'),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 1),
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 1),
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 2),
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 4), 
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 4), 
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 5),
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 7),
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 8),
        ]
        
        expected_output = ['Don Pepe', 'Don Pepe', 'Sr. Cortizona', 'Alan Brito Delgado', 'Alan Brito Delgado', 'Auto Motor', 'Maria', 'Maria', 'Dona Dulce']

        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = ganadores_por_distrito(generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que retorne los candidatos ganadores por pares, cuando se postulan 3 por distrito con empates.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=2,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=2,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=5, nombre='Auto Motor',                 id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=3,   especie='Gato Chico'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Perro Danes'),
            Candidatos(id_candidato=8, nombre='Dona Dulce',                 id_distrito_postulacion=7,   especie='Elefante'),
            Candidatos(id_candidato=9, nombre='Alberto',                    id_distrito_postulacion=7,   especie='Delfin'),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 11,  id_local = 1, id_candidato= 1),
            Votos(id_voto= 1, id_animal_votante= 12,  id_local = 2, id_candidato= 2),
            Votos(id_voto= 2, id_animal_votante= 13,  id_local = 3, id_candidato= 3),
            Votos(id_voto= 3, id_animal_votante= 14,  id_local = 4, id_candidato= 4), 
            Votos(id_voto= 4, id_animal_votante= 15,  id_local = 5, id_candidato= 4), 
            Votos(id_voto= 5, id_animal_votante= 16,  id_local = 6, id_candidato= 5),
            Votos(id_voto= 6, id_animal_votante= 17,  id_local = 7, id_candidato= 7),
            Votos(id_voto= 7, id_animal_votante= 18,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 19,  id_local = 9, id_candidato= 8),
        ]
        
        expected_output = ['Don Pepe','Sr. Cortizona', 'Don Pepe', 'Calvo Calvin', 'Sr. Cortizona', 'Calvo Calvin','Alan Brito Delgado', 'Alan Brito Delgado', 'Auto Motor', 'Maria', 'Maria', 'Dona Dulce']

        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = ganadores_por_distrito(generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = ganadores_por_distrito(g_c , g_v)
        expected_output = GANADORES_POR_DISTRITO_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = ganadores_por_distrito(g_c , g_v)
        expected_output = GANADORES_POR_DISTRITO_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_c = cargar_datos("candidatos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = ganadores_por_distrito(g_c , g_v)
        expected_output = GANADORES_POR_DISTRITO_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

if __name__ == "__main__":
    unittest.main(verbosity=2)
