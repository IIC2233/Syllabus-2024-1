import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import especies_postulantes


class TestEspeciesPostulantesCorrectitud(unittest.TestCase):

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
            Candidato(6400, 'Kellen', 2, 'Perro'),
            Candidato(6182, 'Valentin', 2, 'Delfin nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manati de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardin'),
            Candidato(8094, 'Evander', 6, 'Leon'),
            Candidato(2818, 'Elby', 7, 'Perro'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardin'),
            Candidato(4018, 'Judi', 7, 'Gamba')

            
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 1)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [ 'Medusa', 'Tortuga', 'Perro',
                          'Delfin nariz de botella', 'Mantarraya', 'Manati de tierra',
                          'Caracol de jardin', 'Leon', 'Gamba'
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
            Candidato(6400, 'Kellen', 2, 'Pinguino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfin nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manati de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardin'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pinguino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardin'),
            Candidato(4018, 'Judi', 7, 'Gamba'),
            Candidato(5555, 'Leopoldo', 5, 'Burro'),
            Candidato(3333, 'Thomas', 5, 'Burro'),
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 2)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [ 'Medusa', 'Pinguino emperador',
                          'Caracol de jardin', 'Burro'
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
            Candidato(6400, 'Kellen', 2, 'Pinguino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfun nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Manatu de tierra'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardin'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(2042, 'Jerrie', 5, 'Nutria marina'),
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Foca'),
            Candidato(7695, 'Rosa', 6, 'Mantarraya'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pinguino emperador'),
            Candidato(9999, 'Sophie', 7, 'Mantarraya'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardin'),
            Candidato(4018, 'Judi', 7, 'Medusa')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 3)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [ 
            'Medusa', 
            'Mantarraya'
        ]

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
            Candidato(6400, 'Kellen', 2, 'Pinguino emperador'),
            Candidato(6182, 'Valentin', 2, 'Delfin nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Medusa'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardin'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(2042, 'Jerrie', 5, 'Medusa'),
            Candidato(531, 'Arnoldo', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Pinguino emperador'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Caracol de agua dulce'),
            Candidato(2818, 'Elby', 7, 'Pinguino emperador'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardin'),
            Candidato(4018, 'Judi', 7, 'Pinguino emperador')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 4)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [ 
            'Medusa', 
            'Pinguino emperador'
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
            Candidato(6182, 'Valentin', 2, 'Delfin nariz de botella'),
            Candidato(7691, 'Rosemarie', 2, 'Mantarraya'),
            Candidato(9012, 'Velia', 3, 'Medusa'),
            Candidato(9559, 'Rubye', 3, 'Caracol de jardin'),
            Candidato(7561, 'Jaeden', 3, 'Langostino'),
            Candidato(5385, 'Mose', 4, 'Lagarto'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(2042, 'Jerrie', 5, 'Medusa'),
            Candidato(532, 'Joaquin', 5, 'Burro'),
            Candidato(533, 'Sof', 5, 'Burro'),
            Candidato(534, 'Juan', 5, 'Burro'),
            Candidato(535, 'Bernard', 5, 'Burro'),
            Candidato(536, 'Guido', 5, 'Burro'),
            Candidato(537, 'Flor', 5, 'Burro'),
            Candidato(538, 'Thomas', 5, 'Burro'),
            Candidato(539, 'Helen', 5, 'Burro'),
            Candidato(1006, 'Winter', 5, 'Medusa'),
            Candidato(8094, 'Evander', 6, 'Medusa'),
            Candidato(9330, 'Arielle', 6, 'Pez loro'),
            Candidato(6493, 'Marylyn', 6, 'Medusa'),
            Candidato(2818, 'Elby', 7, 'Medusa'),
            Candidato(3482, 'Elenore', 7, 'Caracol de jardin'),
            Candidato(4018, 'Judi', 7, 'Medusa')
        ]

        generador_entregado = (candidato for candidato in lista_entregada)
        
        resultado_estudiante = especies_postulantes(generador_entregado, 8)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = ['Medusa', 'Burro']

        resultado_lista = [especie for especie in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

   


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
