import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import cantidad_votos_especie_entre_edades, cargar_datos
from utilidades import Animales, Votos, Ponderador
from test_solution import CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_S, CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_M, CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_L

class TestCantidadVotosEspecieEntreEdades(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne el string solicitado, cuando hay un voto que cumple lo pedido.
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

        expected_output = "Hubo 1 votos emitidos por animales entre 1 y 20 años de la especie Gorila."


        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = cantidad_votos_especie_entre_edades(generador_animales, generador_votos, generador_ponderadores, "Gorila", 1, 20)
        self.assertEqual(resultado, expected_output)

    def test_1(self):
        """
         Verifica que retorne el string solicitado, cuando no hay votos que cumplen lo pedido.
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

        expected_output = "Hubo 0 votos emitidos por animales entre 12 y 20 años de la especie Jirafa."


        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = cantidad_votos_especie_entre_edades(generador_animales, generador_votos, generador_ponderadores, "Jirafa", 12, 20)
        self.assertEqual(resultado, expected_output)

    def test_2(self):
        """
         Verifica que retorne el string solicitado, cuando hay varios votos que cumplen lo pedido.
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

        expected_output = "Hubo 2 votos emitidos por animales entre 12 y 1000 años de la especie Gato."


        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = cantidad_votos_especie_entre_edades(generador_animales, generador_votos, generador_ponderadores, "Gato", 12, 1000)
        self.assertEqual(resultado, expected_output)
        
    def test_3(self):
        """
         Verifica que retorne el string solicitado, cuando hay un voto que cumple con lo pedido y la edad tiene el mismo numero entero que el minimo y uno menos que el máximo.
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

        expected_output = "Hubo 1 votos emitidos por animales entre 10 y 11 años de la especie Gorila."


        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = cantidad_votos_especie_entre_edades(generador_animales, generador_votos, generador_ponderadores, "Gorila", 10, 11)
        self.assertEqual(resultado, expected_output)

    def test_4(self):
        """
         Verifica que retorne el string solicitado, cuando hay votos por la especie.
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

        expected_output = "Hubo 0 votos emitidos por animales entre 2 y 90 años de la especie Serpiente."


        generador_animales = (p for p in lista_animales)
        generador_votos = (p for p in lista_votos)
        generador_ponderadores = (p for p in lista_ponderadores)
        resultado = cantidad_votos_especie_entre_edades(generador_animales, generador_votos, generador_ponderadores, "Serpiente", 2, 90)
        self.assertEqual(resultado, expected_output)

    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = cantidad_votos_especie_entre_edades(g_a, g_v, g_p, "Perro", 2, 15)
        expected_output = CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_S

        self.assertCountEqual(resultado, expected_output)
    
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = cantidad_votos_especie_entre_edades(g_a, g_v, g_p, "Perro", 2, 15)
        expected_output = CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_M

        self.assertEqual(resultado, expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = cantidad_votos_especie_entre_edades(g_a, g_v, g_p, "Perro", 2, 15)
        expected_output = CANTIDAD_VOTOS_ESPECIE_ENTRE_EDADES_L
        
        self.assertEqual(resultado, expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
