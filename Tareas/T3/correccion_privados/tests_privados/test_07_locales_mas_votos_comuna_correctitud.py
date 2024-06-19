import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import locales_mas_votos_comuna, cargar_datos
from utilidades import Locales

class TestLocalesMasVotosComunaCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne los id de los locales con 0 o mas votantes y solo hay una comuna.
        """
        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 1, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 1, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 1, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 1, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 1, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 1, id_votantes= [190, 138, 361]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 1, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 1, id_votantes= [217, 374] ),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 1, id_votantes= [377, 210]),
        ]
        
        expected_output = [0,1,2,3,4,5,6,7,8]

        generador = (p for p in lista_locales)
        resultado = locales_mas_votos_comuna(generador, 0, 1)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne los id de los locales con 3 o mas votantes y solo hay una comuna.
        """
        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 1, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 1, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 1, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 1, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 1, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 1, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 1, id_votantes= [445, 235, 496]),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 1, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= [153, 57]),
        ]
        
        expected_output = [0,1,2,3,4,6]

        generador = (p for p in lista_locales)
        resultado = locales_mas_votos_comuna(generador, 3, 1)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne los id de los locales con 0 o mas votantes, solo hay una comuna y hay lugares sin votantes.
        """
        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 1, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 1, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 1, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 1, id_votantes= [190, 138]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 1, id_votantes= [217, 374, 982] ),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 1, id_votantes= []),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= []),
        ]
        
        expected_output = [0,1,4,5,7,8,9]

        generador = (p for p in lista_locales)
        resultado = locales_mas_votos_comuna(generador, 0, 1)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
        
    def test_3(self):
        """
         Verifica que retorne los id de los locales cuando no hay locales que cumplan el requisito.
        """
        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 1, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 1, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 1, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 1, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 1, id_votantes= [342, 106, 319]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 1, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 1, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 1, id_votantes= [217, 374, 982] ),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 1, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 1, id_votantes= [153, 57]),
            Locales(id_local= 10, nombre_local="Local 10" , id_comuna= 1, id_votantes= [1, 2]),
        ]
        
        expected_output = []

        generador = (p for p in lista_locales)
        resultado = locales_mas_votos_comuna(generador, 6, 1)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que retorne los id de los locales con 3 o mas votantes y hay varias comunas.
        """
        lista_locales = [
            Locales(id_local= 0, nombre_local="Local 0" , id_comuna= 1, id_votantes= [68, 388, 359, 337, 18]),
            Locales(id_local= 1, nombre_local="Local 1" , id_comuna= 2, id_votantes= [188, 58, 77, 105, 111]),
            Locales(id_local= 2, nombre_local="Local 2" , id_comuna= 1, id_votantes= [89, 480, 158, 41]),
            Locales(id_local= 3, nombre_local="Local 3" , id_comuna= 2, id_votantes= [306, 179, 412, 139]),
            Locales(id_local= 4, nombre_local="Local 4" , id_comuna= 2, id_votantes= [342, 106]),
            Locales(id_local= 5, nombre_local="Local 5" , id_comuna= 2, id_votantes= [190, 138]),
            Locales(id_local= 6, nombre_local="Local 6" , id_comuna= 1, id_votantes= [445, 235, 496]),
            Locales(id_local= 7, nombre_local="Local 7" , id_comuna= 4, id_votantes= [217, 374, 982] ),
            Locales(id_local= 8, nombre_local="Local 8" , id_comuna= 4, id_votantes= [377, 210]),
            Locales(id_local= 9, nombre_local="Local 9" , id_comuna= 3, id_votantes= [153, 57]),
        ]
        
        expected_output = [1, 3]

        generador = (p for p in lista_locales)
        resultado = locales_mas_votos_comuna(generador, 3, 2)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
