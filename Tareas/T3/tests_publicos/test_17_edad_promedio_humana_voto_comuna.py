import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import edad_promedio_humana_voto_comuna, cargar_datos
from utilidades import Animales, Ponderador, Votos
from test_solution import EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_S, EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_M, EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_L

class TestEdadPromedioHumanaVotoComuna(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne el promedio de edad cuando hay un solo voto de una sola comuna
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
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
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 4), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
        ]
        expected_output = 14*26.67


        generador_animales = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        generador_votos = (p for p in lista_votos)
        resultado = edad_promedio_humana_voto_comuna(generador_animales, generador_ponderador, generador_votos, 3, 3)
        #self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertEqual(resultado, expected_output)

    def test_1(self):
        """
         Verifica que retorne el promedio de edad cuando hay un dos votos, pero de distintas comunas.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 7,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
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
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 3), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
        ]
        expected_output = 12*20


        generador_animales = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        generador_votos = (p for p in lista_votos)
        resultado = edad_promedio_humana_voto_comuna(generador_animales, generador_ponderador, generador_votos, 3, 7)
        #self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertEqual(resultado, expected_output)

    def test_2(self):
        """
         Verifica que retorne el promedio de edad cuando hay un dos votos, de la misma comuna.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
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
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 3), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
        ]
        expected_output = (14*26.67 +12*20)/2


        generador_animales = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        generador_votos = (p for p in lista_votos)
        resultado = edad_promedio_humana_voto_comuna(generador_animales, generador_ponderador, generador_votos, 3, 3)
        #self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertEqual(resultado, expected_output)
        
    def test_3(self):
        """
         Verifica que retorne el promedio de edad cuando hay muchos votos de la misma comuna, pero no todos los votos son en la misma comuna.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 2,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Ballena",     id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
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
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 1), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 1), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 1), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 1), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 1), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
        ]
        expected_output = (21*10 +19*5.5 +17*0.00053)/3


        generador_animales = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        generador_votos = (p for p in lista_votos)
        resultado = edad_promedio_humana_voto_comuna(generador_animales, generador_ponderador, generador_votos, 1, 2)
        #self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertEqual(resultado, expected_output)

    def test_4(self):
        """
         Verifica que retorne 0 cuando no hay votos por el candidato en esa comuna.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 2,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Ballena",     id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
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
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), 
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 3), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
        ]
        expected_output = 0.0


        generador_animales = (p for p in lista_animales)
        generador_ponderador = (p for p in lista_ponderadores)
        generador_votos = (p for p in lista_votos)
        resultado = edad_promedio_humana_voto_comuna(generador_animales, generador_ponderador, generador_votos, 9, 10)
        #self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator))
        self.assertEqual(resultado, expected_output)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = edad_promedio_humana_voto_comuna(g_a, g_p, g_v, 7, 2)
        expected_output = EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_S
        
        self.assertEqual(resultado, expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = edad_promedio_humana_voto_comuna(g_a, g_p, g_v, 7, 2)
        expected_output = EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_M

        self.assertEqual(resultado, expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = edad_promedio_humana_voto_comuna(g_a, g_p, g_v, 7, 2)
        expected_output = EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_L
        
        self.assertEqual(resultado, expected_output)

     
if __name__ == "__main__":
    unittest.main(verbosity=2)
