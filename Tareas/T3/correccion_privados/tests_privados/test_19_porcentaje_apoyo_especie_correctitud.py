import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import porcentaje_apoyo_especie, cargar_datos
from utilidades import Animales, Candidatos, Votos

class TestPorcentajeApoyoEspecieCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
         Verifica que retorne los candidatos con su porcentaje para un candidato.
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

        lista_candidatos = [
            Candidatos(id_candidato=10, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Gato')
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 9), 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 1), 
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 2), 
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 2), # GATO VOTO CANDIDATO 2
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 3), 
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 10), 
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), 
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), 
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 5), 
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 10, id_candidato= 10), # GATO VOTO CANDIDATO 4
        ]
        expected_output = [(10,50)]


        generador_animales = (p for p in lista_animales)
        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = porcentaje_apoyo_especie(generador_animales, generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_1(self):
        """
         Verifica que retorne los candidatos con su porcentaje para varios candidatos. Todos de distinta especie.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
        ]

        
        lista_candidatos = [
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Gorila'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=2,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Jirafa'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Ballena')
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 2), # Gorila Voto 2 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 2), # Foca Voto 2
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 4), # Perro Voto 4
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 3), # Perro Voto 3
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 6), # Loco Voto 6
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 6), # Loco de mar Voto 6
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo Voto 6
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 6), # Ballena Voto 6
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 7), # Jirafa Voto 7
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 9, id_candidato= 6), # Gato Voto 6
        ]
        expected_output = [(2, 100), (3, 50), (4, 0), (6, 100), (7, 0)]


        generador_animales = (p for p in lista_animales)
        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = porcentaje_apoyo_especie(generador_animales, generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_2(self):
        """
         Verifica que retorne los candidatos con su porcentaje para varios candidatos. Algunos de la misma especie.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
        ]

        
        lista_candidatos = [
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Gorila'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=2,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Ballena')
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 2), # Gorila Voto 2 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 2), # Foca Voto 2
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 4), # Perro Voto 4
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 3), # Perro Voto 3
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 6), # Loco Voto 6
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 6), # Loco de mar Voto 6
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo Voto 6
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 6), # Ballena Voto 6
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 7), # Jirafa Voto 7
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 9, id_candidato= 6), # Gato Voto 6
        ]
        expected_output = [(2, 100), (3, 50), (4, 0), (6, 100), (7, 0)]


        generador_animales = (p for p in lista_animales)
        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = porcentaje_apoyo_especie(generador_animales, generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)
    
    def test_3(self):
        """
         Verifica que retorne los candidatos con su porcentaje para varios candidatos. Algunos de la misma especie y con resultados no enteros.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,  peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,  peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,  peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,  peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,  peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 7, nombre="Gordis" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 3111 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
            Animales(id= 10, nombre="Tronquito" ,   especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 11, nombre="Flaquis" ,     especie= "Ballena",     id_comuna= 4,  peso_kg= 3121 , edad= 9 , fecha_nacimiento= "2015/8"),
            Animales(id= 12, nombre="Mocha" ,       especie= "Ballena",     id_comuna= 4,  peso_kg= 4111 , edad= 11 , fecha_nacimiento= "2013/8"),
        ]

        
        lista_candidatos = [
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Gorila'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=2,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Ballena')
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 2), # Gorila Voto 2 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 2), # Foca Voto 2
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 4), # Perro Voto 4
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 3), # Perro Voto 3
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 6), # Loco Voto 6
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 6), # Loco de mar Voto 6
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo Voto 6
            Votos(id_voto= 7, id_animal_votante= 7,  id_local = 8, id_candidato= 7), # Ballena Voto 7
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 7), # Jirafa Voto 7
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 9, id_candidato= 4), # Gato Voto 4
            Votos(id_voto= 10, id_animal_votante= 10,  id_local = 9, id_candidato= 6), # Perro Voto 6
            Votos(id_voto= 11, id_animal_votante= 11,  id_local = 9, id_candidato= 7), # Ballena Voto 7
            Votos(id_voto= 12, id_animal_votante= 12,  id_local = 9, id_candidato= 2), # Ballena Voto 2
        ]
        expected_output = [(2, 100), (3, 33), (4, 100), (6, 0), (7, 67)]


        generador_animales = (p for p in lista_animales)
        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = porcentaje_apoyo_especie(generador_animales, generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)

    def test_4(self):
        """
         Verifica que retorne los candidatos con su porcentaje para varios candidatos. Algunos sin votos en su especie.
        """
        lista_animales = [
            Animales(id= 0, nombre="Enrique" ,      especie= "Gorila" ,     id_comuna= 1,   peso_kg= 57 ,   edad= 23 , fecha_nacimiento= "2001/1"),
            Animales(id= 1, nombre="Foca" ,         especie= "Foca",        id_comuna= 1,   peso_kg= 65 ,   edad= 21 , fecha_nacimiento= "2003/2"),
            Animales(id= 2, nombre="Tomy" ,         especie= "Perro",       id_comuna= 2,   peso_kg= 19 ,   edad= 19 , fecha_nacimiento= "2005/3"),
            Animales(id= 3, nombre="Mancha" ,       especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
            Animales(id= 4, nombre="Luna" ,         especie= "Lobo",        id_comuna= 3,   peso_kg= 50 ,   edad= 15 , fecha_nacimiento= "2009/5"),
            Animales(id= 5, nombre="Luna de mar" ,  especie= "Lobo de mar", id_comuna= 3,   peso_kg= 101 ,  edad= 13 , fecha_nacimiento= "2011/6"),
            Animales(id= 6, nombre="Guaton" ,       especie= "Hipopotamo",  id_comuna= 4,   peso_kg= 322 ,  edad= 11, fecha_nacimiento= "2013/7"),
            Animales(id= 8, nombre="Cuello" ,       especie= "Jirafa",      id_comuna= 5,   peso_kg= 32 ,   edad= 7 , fecha_nacimiento= "2017/9"),
            Animales(id= 9, nombre="Misifus" ,      especie= "Gato",        id_comuna= 5,   peso_kg= 8 ,    edad= 5 , fecha_nacimiento= "2019/11"),
            Animales(id= 10, nombre="Tronquito" ,   especie= "Perro",       id_comuna= 2,   peso_kg= 21 ,   edad= 17 , fecha_nacimiento= "2007/4"),
        ]

        
        lista_candidatos = [
            Candidatos(id_candidato=2, nombre='Sr. Cortizona',              id_distrito_postulacion=2,   especie='Gorila'),
            Candidatos(id_candidato=3, nombre='Calvo Calvin',               id_distrito_postulacion=2,   especie='Perro'),
            Candidatos(id_candidato=4, nombre='Alan Brito Delgado',         id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=6, nombre='Lalo',                       id_distrito_postulacion=3,   especie='Gato'),
            Candidatos(id_candidato=7, nombre='Maria',                      id_distrito_postulacion=7,   especie='Ballena')
        ]
        
        lista_votos = [
            Votos(id_voto= 0, id_animal_votante= 0,  id_local = 1, id_candidato= 4), # Gorila Voto 2 
            Votos(id_voto= 1, id_animal_votante= 1,  id_local = 2, id_candidato= 2), # Foca Voto 2
            Votos(id_voto= 2, id_animal_votante= 2,  id_local = 3, id_candidato= 4), # Perro Voto 4
            Votos(id_voto= 3, id_animal_votante= 3,  id_local = 4, id_candidato= 3), # Perro Voto 3
            Votos(id_voto= 4, id_animal_votante= 4,  id_local = 5, id_candidato= 6), # Loco Voto 6
            Votos(id_voto= 5, id_animal_votante= 5,  id_local = 6, id_candidato= 6), # Loco de mar Voto 6
            Votos(id_voto= 6, id_animal_votante= 6,  id_local = 7, id_candidato= 6), # Hipopotamo Voto 6
            Votos(id_voto= 8, id_animal_votante= 8,  id_local = 9, id_candidato= 7), # Jirafa Voto 7
            Votos(id_voto= 9, id_animal_votante= 9,  id_local = 9, id_candidato= 6), # Gato Voto 6
            Votos(id_voto= 10, id_animal_votante= 10,  id_local = 9, id_candidato= 6), # Perro Voto 6
        ]
        expected_output = [(2, 0), (3, 33), (4, 0), (6, 100), (7, 0)]


        generador_animales = (p for p in lista_animales)
        generador_candidatos = (p for p in lista_candidatos)
        generador_votos = (p for p in lista_votos)
        resultado = porcentaje_apoyo_especie(generador_animales, generador_candidatos, generador_votos)
        self.assertIsInstance(resultado, (list, tuple, set, filter, map, Generator, zip))
        self.assertCountEqual(list(resultado), expected_output)



if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
