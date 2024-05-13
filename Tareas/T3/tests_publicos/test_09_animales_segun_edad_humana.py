import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import animales_segun_edad_humana, cargar_datos
from utilidades import Animales, Ponderador
from test_solution import ANIMALES_SEGUN_EDAD_HUMANA_S, ANIMALES_SEGUN_EDAD_HUMANA_M, ANIMALES_SEGUN_EDAD_HUMANA_L

class TestAnimalesSegunEdadHumana(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne los nombres de los animales > a 50.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 13,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 12,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 3,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 3,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 33,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 54,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 23,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 98,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 2,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 2,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador = 0.444),
            Ponderador(especie= "Foca",        ponderador = 10),
            Ponderador(especie= "Perro",       ponderador = 5.5),
            Ponderador(especie= "Lobo",        ponderador = 26.67),
            Ponderador(especie= "Lobo de mar", ponderador = 20),
            Ponderador(especie= "Hipopotamo",  ponderador = 0.053),
            Ponderador(especie= "Ballena",     ponderador = 0.00053),
            Ponderador(especie= "Jirafa",      ponderador = 0.067),
            Ponderador(especie= "Gato",        ponderador = 40),
        ]
        
        expected_output = ["Foca", "Tomy", "Mancha", "Luna", "Luna de mar", "Misifus"]

        generador_animal = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        resultado = animales_segun_edad_humana(generador_animal,generador_ponderador, ">", 50)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne los nombres de los animales < a 8.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 13, peso_kg= 57 , edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 12, peso_kg= 65 , edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 3, peso_kg= 19 , edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 3, peso_kg= 21 , edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 33, peso_kg= 50 , edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 54, peso_kg= 101 , edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 23, peso_kg= 322 , edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 98, peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 2, peso_kg= 32 , edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 2, peso_kg= 8 , edad= 4 , fecha_nacimiento= "2019/11"),
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador = 0.444),
            Ponderador(especie= "Foca",        ponderador = 10),
            Ponderador(especie= "Perro",       ponderador = 5.5),
            Ponderador(especie= "Lobo",        ponderador = 26.67),
            Ponderador(especie= "Lobo de mar", ponderador = 20),
            Ponderador(especie= "Hipopotamo",  ponderador = 0.053),
            Ponderador(especie= "Ballena",     ponderador = 0.00053),
            Ponderador(especie= "Jirafa",      ponderador = 0.067),
            Ponderador(especie= "Gato",        ponderador = 40),
        ]
        
        expected_output = ["Guaton", "Gordis", "Cuello"]

        generador_animal = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        resultado = animales_segun_edad_humana(generador_animal,generador_ponderador, "<", 8)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne los nombres de los animales = a 240, cuando es solo uno.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 13, peso_kg= 57 , edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 12, peso_kg= 65 , edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 3, peso_kg= 19 , edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 3, peso_kg= 21 , edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 33, peso_kg= 50 , edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 54, peso_kg= 101 , edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 23, peso_kg= 322 , edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 98, peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 2, peso_kg= 32 , edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 2, peso_kg= 8 , edad= 4 , fecha_nacimiento= "2019/11"),
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador = 0.444),
            Ponderador(especie= "Foca",        ponderador = 10),
            Ponderador(especie= "Perro",       ponderador = 5.5),
            Ponderador(especie= "Lobo",        ponderador = 26.67),
            Ponderador(especie= "Lobo de mar", ponderador = 20),
            Ponderador(especie= "Hipopotamo",  ponderador = 0.053),
            Ponderador(especie= "Ballena",     ponderador = 0.00053),
            Ponderador(especie= "Jirafa",      ponderador = 0.067),
            Ponderador(especie= "Gato",        ponderador = 40),
        ]
        
        expected_output = ["Luna de mar"]

        generador_animal = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        resultado = animales_segun_edad_humana(generador_animal,generador_ponderador, "=", 240)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
      
    def test_3(self):
        """
         Verifica que retorne los nombres de los animales = a 240, cuando son más de uno.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 13, peso_kg= 57 , edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 12, peso_kg= 65 , edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 3, peso_kg= 19 , edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 3, peso_kg= 21 , edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 33, peso_kg= 50 , edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 54, peso_kg= 101 , edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 10, nombre="Luna de rio" ,  especie= "Lobo de mar", id_comuna= 54, peso_kg= 90 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 23, peso_kg= 322 , edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 98, peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 2, peso_kg= 32 , edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 2, peso_kg= 8 , edad= 4 , fecha_nacimiento= "2019/11"),
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador = 0.444),
            Ponderador(especie= "Foca",        ponderador = 10),
            Ponderador(especie= "Perro",       ponderador = 5.5),
            Ponderador(especie= "Lobo",        ponderador = 26.67),
            Ponderador(especie= "Lobo de mar", ponderador = 20),
            Ponderador(especie= "Hipopotamo",  ponderador = 0.053),
            Ponderador(especie= "Ballena",     ponderador = 0.00053),
            Ponderador(especie= "Jirafa",      ponderador = 0.067),
            Ponderador(especie= "Gato",        ponderador = 40),
        ]
        
        expected_output = ["Luna de mar", "Luna de rio"]

        generador_animal = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        resultado = animales_segun_edad_humana(generador_animal,generador_ponderador, "=", 240)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que retorne los nombres de los animales = a 240, cuando no hay ninguno.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 13, peso_kg= 57 , edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 12, peso_kg= 65 , edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 3, peso_kg= 19 , edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 3, peso_kg= 21 , edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 33, peso_kg= 50 , edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 23, peso_kg= 322 , edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 98, peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 2, peso_kg= 32 , edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 2, peso_kg= 8 , edad= 4 , fecha_nacimiento= "2019/11"),
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador = 0.444),
            Ponderador(especie= "Foca",        ponderador = 10),
            Ponderador(especie= "Perro",       ponderador = 5.5),
            Ponderador(especie= "Lobo",        ponderador = 26.67),
            Ponderador(especie= "Lobo de mar", ponderador = 20),
            Ponderador(especie= "Hipopotamo",  ponderador = 0.053),
            Ponderador(especie= "Ballena",     ponderador = 0.00053),
            Ponderador(especie= "Jirafa",      ponderador = 0.067),
            Ponderador(especie= "Gato",        ponderador = 40),
        ]
        
        expected_output = []

        generador_animal = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        resultado = animales_segun_edad_humana(generador_animal,generador_ponderador, "=", 240)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
        
    def test_5(self):
        """
         Verifica que retorne los nombres de los animales = a 210, cuando se repite un nombre.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 13, peso_kg= 57 , edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1,  nombre="Foco" ,         especie= "Foca",        id_comuna= 12, peso_kg= 65 , edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 11, nombre="Foco" ,         especie= "Foca",       id_comuna= 12, peso_kg= 65 , edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 3, peso_kg= 19 , edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 3, peso_kg= 21 , edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 33, peso_kg= 50 , edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 23, peso_kg= 322 , edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 98, peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 2, peso_kg= 32 , edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 2, peso_kg= 8 , edad= 4 , fecha_nacimiento= "2019/11"),
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador = 0.444),
            Ponderador(especie= "Foca",        ponderador = 10),
            Ponderador(especie= "Perro",       ponderador = 5.5),
            Ponderador(especie= "Lobo",        ponderador = 26.67),
            Ponderador(especie= "Lobo de mar", ponderador = 20),
            Ponderador(especie= "Hipopotamo",  ponderador = 0.053),
            Ponderador(especie= "Ballena",     ponderador = 0.00053),
            Ponderador(especie= "Jirafa",      ponderador = 0.067),
            Ponderador(especie= "Gato",        ponderador = 40),
        ]
        
        expected_output = ["Foco", "Foco"]

        generador_animal = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        resultado = animales_segun_edad_humana(generador_animal,generador_ponderador, "=", 210)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_6(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_p =  cargar_datos("ponderadores", carpeta)
        resultado = animales_segun_edad_humana(g_a, g_p, ">", 11)
        expected_output = ANIMALES_SEGUN_EDAD_HUMANA_S
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p =  cargar_datos("ponderadores", carpeta)
        resultado = animales_segun_edad_humana(g_a, g_p, ">", 11)
        expected_output = ANIMALES_SEGUN_EDAD_HUMANA_M

        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)

    def test_8(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p =  cargar_datos("ponderadores", carpeta)
        resultado = animales_segun_edad_humana(g_a, g_p, ">", 11)
        expected_output = ANIMALES_SEGUN_EDAD_HUMANA_L
        
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertCountEqual(list(resultado), expected_output)  


if __name__ == "__main__":
    unittest.main(verbosity=2)
