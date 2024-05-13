import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import pares_candidatos, cargar_datos
from utilidades import Candidatos
from test_solution import PARES_CANDIDATOS_S, PARES_CANDIDATOS_M, PARES_CANDIDATOS_L

class TestParesCandidatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne los nombres en pares para 0 o 1 candidatos.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe', id_distrito_postulacion=0, especie='Medusa')
        ]
        
        expected_output = []

        generador = (p for p in lista_candidatos)
        resultado = pares_candidatos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        resultado_esperado_ordenado = [sorted(x) for x in expected_output]
        resultado_ordenado = [sorted(x) for x in list(resultado)]


        self.assertCountEqual(resultado_esperado_ordenado, resultado_ordenado)

    def test_1(self):
        """
         Verifica que retorne los nombres en pares para 2 candidatos.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=0,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=9,   especie='Mendosino'),
        ]
        
        expected_output = [("Don Pepe", 'Sr. Cortizona')]
        
        generador = (p for p in lista_candidatos)
        resultado = pares_candidatos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        resultado_esperado_ordenado = [sorted(x) for x in expected_output]
        resultado_ordenado = [sorted(x) for x in list(resultado)]

        self.assertCountEqual(resultado_esperado_ordenado, resultado_ordenado)

    def test_2(self):
        """
         Verifica que retorne los nombres en pares para 3 candidatos.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=0,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=9,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=8,   especie='Perro'),
        ]
        
        expected_output = [('Don Pepe', 'Sr. Cortizona'),('Don Pepe', 'Calvo Calvin'),('Sr. Cortizona', 'Calvo Calvin')]
        
        generador = (p for p in lista_candidatos)
        resultado = pares_candidatos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        resultado_esperado_ordenado = [sorted(x) for x in expected_output]
        resultado_ordenado = [sorted(x) for x in list(resultado)]

        self.assertCountEqual(resultado_esperado_ordenado, resultado_ordenado)
  
    def test_3(self):
        """
         Verifica que retorne los nombres en pares para 4 candidatos.
        """
        lista_candidatos = [
            Candidatos(id_candidato=1, nombre='Don Pepe',                   id_distrito_postulacion=0,   especie='Medusa'),
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=9,   especie='Mendosino'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=8,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=7,   especie='Gato'),
        ]
        
        expected_output = [('Don Pepe', 'Sr. Cortizona'),('Don Pepe', 'Calvo Calvin'),('Don Pepe', 'Alan Brito Delgado'),
                           ('Sr. Cortizona', 'Calvo Calvin'),('Sr. Cortizona', 'Alan Brito Delgado'), 
                           ('Calvo Calvin','Alan Brito Delgado')]
        
        generador = (p for p in lista_candidatos)
        resultado = pares_candidatos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        resultado_esperado_ordenado = [sorted(x) for x in expected_output]
        resultado_ordenado = [sorted(x) for x in list(resultado)]

        self.assertCountEqual(resultado_esperado_ordenado, resultado_ordenado)

    def test_4(self):
        """
         Verifica que retorne los nombres en pares para n candidatos.
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
        
        expected_output = [('Don Pepe', 'Sr. Cortizona'), ('Don Pepe', 'Calvo Calvin'), ('Don Pepe', 'Alan Brito Delgado'), ('Don Pepe', 'Auto Motor'), ('Don Pepe', 'Lalo'), ('Don Pepe', 'Maria'), ('Don Pepe', 'Dona Dulce'), ('Don Pepe', 'Alberto'), ('Don Pepe', 'Peaje Autopista'),
                            ('Sr. Cortizona', 'Calvo Calvin'),('Sr. Cortizona', 'Alan Brito Delgado'), ('Sr. Cortizona', 'Auto Motor'), ('Sr. Cortizona', 'Lalo'), ('Sr. Cortizona', 'Maria'), ('Sr. Cortizona', 'Dona Dulce'), ('Sr. Cortizona', 'Alberto'), ('Sr. Cortizona', 'Peaje Autopista'),
                            ('Calvo Calvin','Alan Brito Delgado'), ('Calvo Calvin', 'Auto Motor'), ('Calvo Calvin', 'Lalo'), ('Calvo Calvin', 'Maria'), ('Calvo Calvin', 'Dona Dulce'), ('Calvo Calvin', 'Alberto'), ('Calvo Calvin', 'Peaje Autopista'),
                            ('Alan Brito Delgado', 'Auto Motor'),('Alan Brito Delgado', 'Lalo'),('Alan Brito Delgado', 'Maria'),('Alan Brito Delgado', 'Dona Dulce'),('Alan Brito Delgado', 'Alberto'),('Alan Brito Delgado', 'Peaje Autopista'),
                            ('Auto Motor', 'Lalo'), ('Auto Motor', 'Maria'), ('Auto Motor', 'Dona Dulce'), ('Auto Motor', 'Alberto'), ('Auto Motor', 'Peaje Autopista'),
                            ('Lalo', 'Maria'), ('Lalo', 'Dona Dulce'), ('Lalo', 'Alberto'), ('Lalo', 'Peaje Autopista'), 
                            ('Maria', 'Dona Dulce'), ('Maria', 'Alberto'), ('Maria', 'Peaje Autopista'),
                            ('Dona Dulce', 'Alberto'), ('Dona Dulce', 'Peaje Autopista'),
                            ('Alberto', 'Peaje Autopista')
                            ]
        
        generador = (p for p in lista_candidatos)
        resultado = pares_candidatos(generador)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))

        resultado_esperado_ordenado = [sorted(x) for x in expected_output]
        resultado_ordenado = [sorted(x) for x in list(resultado)]

        self.assertCountEqual(resultado_esperado_ordenado, resultado_ordenado)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_c = cargar_datos("candidatos", carpeta)
        resultado = pares_candidatos(g_c)
        expected_output = PARES_CANDIDATOS_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_c = cargar_datos("candidatos", carpeta)
        resultado = pares_candidatos(g_c)
        expected_output = PARES_CANDIDATOS_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_c = cargar_datos("candidatos", carpeta)
        resultado = pares_candidatos(g_c)
        expected_output = PARES_CANDIDATOS_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)       

        
if __name__ == "__main__":
    unittest.main(verbosity=2)
