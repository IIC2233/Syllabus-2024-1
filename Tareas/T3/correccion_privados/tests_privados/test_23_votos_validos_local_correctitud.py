import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_validos_local, cargar_datos
from utilidades import Animales, Votos, Ponderador

class TestVotosValidosLocalCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne el generador solicitado, cuando hay un voto valido en el local.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 10, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Gato",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), # Gorila, edad 23*0.444 = 10.212
            Votos(id_voto= 10, id_animal_votante= 10,  id_local = 2, id_candidato= 1), # Foca, edad 21*10 = 210
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), # Perro, edad 19*5.5 = 104.5
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), # Gato, edad 17*40 = 680
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), # Lobo, edad 14*26.67 = 373.38
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 4), # Lobo de mar, edad 12*20 = 240
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo, edad 10*0.053 =0.53
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), # Ballena, edad 8*0.00053 = 0.00424
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), # Jirafa, edad 6*0.067 = 0.402
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 10, id_candidato= 4), # Gato, edad 4*40 = 160
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador= 0.444),
            Ponderador(especie= "Foca",        ponderador= 10),
            Ponderador(especie= "Perro",       ponderador= 5.5),
            Ponderador(especie= "Lobo",        ponderador= 26.67),
            Ponderador(especie= "Lobo de mar", ponderador= 20),
            Ponderador(especie= "Hipopotamo",  ponderador= 0.053),
            Ponderador(especie= "Ballena",     ponderador= 0.00053),
            Ponderador(especie= "Jirafa",      ponderador= 0.067),
            Ponderador(especie= "Gato",        ponderador= 40),
        ]

        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = votos_validos_local(generador_animales, generador_votos, generador_ponderadores, 2)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        list_resultado = list(resultado)
        resultado_esperado_considerando_el_ano_de_nacimiento = [10]
        resultado_esperado_considerando_la_edad = [10]

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)

    def test_1(self):
        """
         Verifica que retorne el generador solicitado, cuando hay varios votos y todos son validos en el local.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Gato",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), # Gorila, edad 23*0.444 = 10.212
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), # Foca, edad 21*10 = 210
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), # Perro, edad 19*5.5 = 104.5
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 5, id_candidato= 2), # Gato, edad 17*40 = 680
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), # Lobo, edad 15*26.67 = 373.38
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 5, id_candidato= 4), # Lobo de mar, edad 13*20 = 260
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo, edad 10*0.053 =0.53
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), # Ballena, edad 8*0.00053 = 0.00424
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), # Jirafa, edad 6*0.067 = 0.402
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 5, id_candidato= 4), # Gato, edad 5*40 = 200
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador= 0.444),
            Ponderador(especie= "Foca",        ponderador= 10),
            Ponderador(especie= "Perro",       ponderador= 5.5),
            Ponderador(especie= "Lobo",        ponderador= 26.67),
            Ponderador(especie= "Lobo de mar", ponderador= 20),
            Ponderador(especie= "Hipopotamo",  ponderador= 0.053),
            Ponderador(especie= "Ballena",     ponderador= 0.00053),
            Ponderador(especie= "Jirafa",      ponderador= 0.067),
            Ponderador(especie= "Gato",        ponderador= 40),
        ]

        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = votos_validos_local(generador_animales, generador_votos, generador_ponderadores, 5)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        list_resultado = list(resultado)
        resultado_esperado_considerando_el_ano_de_nacimiento = [3,4,5,9]
        resultado_esperado_considerando_la_edad = [3,4,5,9]

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)

    def test_2(self):
        """
         Verifica que retorne el generador solicitado, cuando hay varios votos y no todos son validos en el local.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Gato",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 7, id_candidato= 9), # Gorila, edad 23*0.444 = 10.212
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), # Foca, edad 21*10 = 210
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), # Perro, edad 19*5.5 = 104.5
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 2, id_candidato= 2), # Gato, edad 17*40 = 680
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 7, id_candidato= 3), # Lobo, edad 14*26.67 = 373.38
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 7, id_candidato= 4), # Lobo de mar, edad 12*20 = 240
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo, edad 10*0.053 =0.53
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), # Ballena, edad 8*0.00053 = 0.00424
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 7, id_candidato= 5), # Jirafa, edad 6*0.067 = 0.402
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 2, id_candidato= 4), # Gato, edad 4*40 = 160
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador= 0.444),
            Ponderador(especie= "Foca",        ponderador= 10),
            Ponderador(especie= "Perro",       ponderador= 5.5),
            Ponderador(especie= "Lobo",        ponderador= 26.67),
            Ponderador(especie= "Lobo de mar", ponderador= 20),
            Ponderador(especie= "Hipopotamo",  ponderador= 0.053),
            Ponderador(especie= "Ballena",     ponderador= 0.00053),
            Ponderador(especie= "Jirafa",      ponderador= 0.067),
            Ponderador(especie= "Gato",        ponderador= 40),
        ]

        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = votos_validos_local(generador_animales, generador_votos, generador_ponderadores, 7)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        list_resultado = list(resultado)
        resultado_esperado_considerando_el_ano_de_nacimiento = [4,5]
        resultado_esperado_considerando_la_edad = [4,5]

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)

        
    def test_3(self):
        """
         Verifica que retorne el generador solicitado, cuando no hay votos validos en el local.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Gato",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), # Gorila, edad 23*0.444 = 10.212
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), # Foca, edad 21*10 = 210
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), # Perro, edad 19*5.5 = 104.5
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), # Gato, edad 17*40 = 680
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), # Lobo, edad 14*26.67 = 373.38
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 4), # Lobo de mar, edad 12*20 = 240
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo, edad 11*0.053 =0.53
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), # Ballena, edad 8*0.00053 = 0.00424
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), # Jirafa, edad 6*0.067 = 0.402
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 10, id_candidato= 4), # Gato, edad 4*40 = 160
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador= 0.444),
            Ponderador(especie= "Foca",        ponderador= 10),
            Ponderador(especie= "Perro",       ponderador= 5.5),
            Ponderador(especie= "Lobo",        ponderador=26.67),
            Ponderador(especie= "Lobo de mar", ponderador= 20),
            Ponderador(especie= "Hipopotamo",  ponderador= 0.053),
            Ponderador(especie= "Ballena",     ponderador= 0.00053),
            Ponderador(especie= "Jirafa",      ponderador= 0.067),
            Ponderador(especie= "Gato",        ponderador= 40),
        ]

        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = votos_validos_local(generador_animales, generador_votos, generador_ponderadores, 7)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        list_resultado = list(resultado)
        resultado_esperado_considerando_el_ano_de_nacimiento = []
        resultado_esperado_considerando_la_edad = []

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)


    def test_4(self):
        """
         Verifica que retorne el generador solicitado, cuando no hay votos en el local.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Gato",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 14 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 12 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 10, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 8 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 6 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 4 , fecha_nacimiento= "2019/11"),
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), # Gorila, edad 23*0.444 = 10.212
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), # Foca, edad 21*10 = 210
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), # Perro, edad 19*5.5 = 104.5
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), # Gato, edad 17*40 = 680
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), # Lobo, edad 14*26.67 = 373.38
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 4), # Lobo de mar, edad 12*20 = 240
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo, edad 10*0.053 =0.53
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), # Ballena, edad 8*0.00053 = 0.00424
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), # Jirafa, edad 6*0.067 = 0.402
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 10, id_candidato= 4), # Gato, edad 4*40 = 160
        ]

        lista_ponderadores = [
            Ponderador(especie= "Gorila" ,     ponderador= 0.444),
            Ponderador(especie= "Foca",        ponderador= 10),
            Ponderador(especie= "Perro",       ponderador= 5.5),
            Ponderador(especie= "Lobo",        ponderador= 26.67),
            Ponderador(especie= "Lobo de mar", ponderador= 20),
            Ponderador(especie= "Hipopotamo",  ponderador= 0.053),
            Ponderador(especie= "Ballena",     ponderador= 0.00053),
            Ponderador(especie= "Jirafa",      ponderador= 0.067),
            Ponderador(especie= "Gato",        ponderador= 40),
        ]

        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = votos_validos_local(generador_animales, generador_votos, generador_ponderadores, 11)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        list_resultado = list(resultado)
        resultado_esperado_considerando_el_ano_de_nacimiento = []
        resultado_esperado_considerando_la_edad = []

        try:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_el_ano_de_nacimiento)
        except AssertionError:
            self.assertCountEqual(list_resultado, resultado_esperado_considerando_la_edad)



if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
