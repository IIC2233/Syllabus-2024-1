import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import especies_postulantes, cargar_datos
from test_solution import ESPECIES_POSTULANTES_S, ESPECIES_POSTULANTES_M, ESPECIES_POSTULANTES_L


class TestEspeciesPostulantes(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que el test funcione cuando se requiere solo 1 postulante.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatí de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Gamba')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 1)

        self.assertIsInstance(resultado_estudiante, Generator)

        lista_esperada = [ 'Medusa', 'Tortuga', 'Pingüino emperador',
                          'Delfín nariz de botella', 'Mantarraya', 'Manatí de tierra',
                          'Caracol de jardín', 'Gamba'
        ]

        resultado_lista = [especie for especie in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_1(self):
        """
         Verifica que el test funcione con generadores pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada = [
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

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 2)

        self.assertIsInstance(resultado_estudiante, Generator)

        lista_esperada = [ 'Medusa', 'Pingüino emperador',
                          'Caracol de jardín'
        ]

        resultado_lista = [especie for especie in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione con generadores pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada = [
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
            Candidato(4018, 'Judi', 7, 'Medusa')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 3)

        self.assertIsInstance(resultado_estudiante, Generator)

        lista_esperada = [ 'Medusa']

        resultado_lista = [especie for especie in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione con generadores pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Medusa'),
            Candidato(6400, 'Kellen', 2, 'Pingüino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Medusa'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Medusa'),
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Pingüino emperador'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pingüino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Pingüino emperador')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 4)

        self.assertIsInstance(resultado_estudiante, Generator)

        lista_esperada = [ 'Medusa', 'Pingüino emperador',
        ]

        resultado_lista = [especie for especie in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)  

    def test_4(self):
        """
         Verifica que el test funcione con generadores pequeños.
        """

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Medusa'),
            Candidato(6400, 'Kellen', 2, 'Medusa'),
            Candidato(6182, 'Valentin', 2, 'Delfín nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Medusa'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardín'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Búho'),
            Candidato(2042, 'Jerrie', 5, 'Medusa'),
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Medusa'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Medusa'),
            Candidato(2818, 'Elby', 7, 'Medusa'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardín'),
            Candidato(4018, 'Judi', 7, 'Medusa')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 10)

        self.assertIsInstance(resultado_estudiante, Generator)

        lista_esperada = ['Medusa']

        resultado_lista = [especie for especie in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_c = cargar_datos("candidatos", carpeta)
        resultado = especies_postulantes(g_c, 3)
        expected_output = ESPECIES_POSTULANTES_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_c = cargar_datos("candidatos", carpeta)
        resultado = especies_postulantes(g_c, 3)
        expected_output = ESPECIES_POSTULANTES_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_c = cargar_datos("candidatos", carpeta)
        resultado = especies_postulantes(g_c, 3)
        expected_output = ESPECIES_POSTULANTES_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
