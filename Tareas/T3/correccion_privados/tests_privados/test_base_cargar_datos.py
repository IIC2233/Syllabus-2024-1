import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from utilidades import Animales, Locales, Candidatos, Distritos, Ponderador, Votos
from consultas import cargar_datos

from timeout_function import timeout
N_SECOND = 20 

class TestCargarDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_s_animales(self):
        """
         Probando con el dataset S de animales
        """
        generador = cargar_datos("animales", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 10000)

        # Revisar posiciones aleatorias
        animales_cargados = [generador[0], generador[11],
                             generador[4444], generador[-1]]

        animales_esperados = [
            Animales(id=1, nombre='Elida', especie='Castor', id_comuna=76,
                     peso_kg=23.23214, edad=60, fecha_nacimiento='1964/6'),
            Animales(id=12, nombre='Katelyn', especie='Bisonte', id_comuna=280,
                     peso_kg=653.20328, edad=17, fecha_nacimiento='2007/7'),
            Animales(id=4445, nombre='Janyce', especie='Tortuga de tierra', id_comuna=244,
                     peso_kg=116.5162, edad=93, fecha_nacimiento='1931/1'),
            Animales(id=10000, nombre='Celesta', especie='Luciernaga', id_comuna=224,
                     peso_kg=0.71402, edad=13, fecha_nacimiento='2011/9')
        ]
    

        self.assertCountEqual(animales_cargados, animales_esperados)

    @timeout(N_SECOND)
    def test_s_candidatos(self):
        """
         Probando con el dataset S de candidatos
        """
        generador = cargar_datos("candidatos", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 234)

        # Revisar posiciones aleatorias
        candidatos_cargados = [generador[0],
                               generador[3], generador[112], generador[-1]]

        candidatos_esperados = [
            Candidatos(id_candidato=5273, nombre='Magen',
                       id_distrito_postulacion=1, especie='Colibri'),
            Candidatos(id_candidato=8395, nombre='Zenas',
                       id_distrito_postulacion=2, especie='Neque'),
            Candidatos(id_candidato=3388, nombre='Skyla',
                       id_distrito_postulacion=44, especie='Saltamontes'),
            Candidatos(id_candidato=1253, nombre='Treva',
                       id_distrito_postulacion=92, especie='Hormiga reina')
        ]

        self.assertCountEqual(candidatos_cargados, candidatos_esperados)

    @timeout(N_SECOND)
    def test_s_distritos(self):
        """
         Probando con el dataset S de distritos
        """
        generador = cargar_datos("distritos", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 343)

        # Revisar posiciones aleatorias
        distritos_cargados = [generador[0],
                              generador[69], generador[312], generador[-1]]

        distritos_esperados = [
            Distritos(id_distrito=1, nombre='Distrito 1', id_comuna=1,
                      provincia='Arica', region='Arica y Parinacota'),
            Distritos(id_distrito=13, nombre='Distrito 13', id_comuna=70,
                      provincia='San Felipe de Aconcagua', region='Valparaiso'),
            Distritos(id_distrito=80, nombre='Distrito 80', id_comuna=313,
                      provincia='Llanquihue', region='Los Lagos'),
            Distritos(id_distrito=92, nombre='Distrito 92', id_comuna=343,
                      provincia='ultima Esperanza', region='Magallanes y de la Antartica Chilena')
        ]

        self.assertCountEqual(distritos_cargados, distritos_esperados)

    @timeout(N_SECOND)
    def test_s_locales(self):
        """
         Probando con el dataset S de locales
        """
        generador = cargar_datos("locales", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 2327)

        # Revisar posiciones aleatorias
        locales_cargados = [generador[0], generador[6],
                            generador[1313], generador[-1]]

        locales_esperados = [
            Locales(id_local=1, nombre_local='Local 1',
                    id_comuna=1, id_votantes=[570, 576, 664, 741, 845, 1455, 1823, 1972, 2120, 2501, 3147, 3308]),
            Locales(id_local=7, nombre_local='Local 7',
                    id_comuna=2, id_votantes=[678, 818, 1895, 1904, 2343]),
            Locales(id_local=1314, nombre_local='Local 1314',
                    id_comuna=197, id_votantes=[]),
            Locales(id_local=2327, nombre_local='Local 2327', id_comuna=343,
                    id_votantes=[9364, 9599])
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_s_ponderadores(self):
        """
         Probando con el dataset S de ponderadores
        """
        generador = cargar_datos("ponderadores", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 190)

        # Revisar posiciones aleatorias
        ponderadores_cargados = [generador[0], generador[18],
                                 generador[42], generador[-1]]

        ponderadores_esperados = [
            Ponderador(especie='Perro', ponderador=0.15),
            Ponderador(especie='Ciervo', ponderador=0.2857),
            Ponderador(especie='Aguila calva', ponderador=13.33),
            Ponderador(especie='Estrella espinosa', ponderador=400.0)
        ]

        self.assertCountEqual(ponderadores_cargados, ponderadores_esperados)

    @timeout(N_SECOND)
    def test_s_votos(self):
        """
         Probando con el dataset S de votos
        """
        generador = cargar_datos("votos", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 10000)

        # Revisar posiciones aleatorias
        votos_cargados = [generador[0], generador[27],
                          generador[4952], generador[-1]]

        votos_esperados = [
            Votos(id_voto=1, id_animal_votante=4618,
                  id_local=2120, id_candidato=5273),
            Votos(id_voto=28, id_animal_votante=794,
                  id_local=1979, id_candidato=6926),
            Votos(id_voto=4953, id_animal_votante=2039,
                  id_local=1102, id_candidato=4114),
            Votos(id_voto=10000, id_animal_votante=9599,
                  id_local=2327, id_candidato=9419)
        ]

        self.assertCountEqual(votos_cargados, votos_esperados)

    @timeout(N_SECOND)
    def test_m_animales(self):
        """
         Probando con el dataset M de animales
        """
        generador = cargar_datos("animales", "m")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 100000)

        # Revisar posiciones aleatorias
        animales_cargados = [generador[0], generador[11],
                             generador[4444], generador[-1]]

        animales_esperados = [
            Animales(id=1, nombre='Sheridan', especie='Trucha', id_comuna=207, peso_kg=1.31448, edad=98, fecha_nacimiento='1926/8'),
            Animales(id=12, nombre='Margarete', especie='Tortuga', id_comuna=326, peso_kg=11.17157, edad=13, fecha_nacimiento='2011/10'),
            Animales(id=4445, nombre='Alvina', especie='Erizo de tierra', id_comuna=15, peso_kg=0.48552, edad=45, fecha_nacimiento='1979/3'),
            Animales(id=100000, nombre='Truman', especie='Nandu', id_comuna=172, peso_kg=25.13471, edad=49, fecha_nacimiento='1975/12')
        ]

        self.assertCountEqual(animales_cargados, animales_esperados)

    @timeout(N_SECOND)
    def test_m_candidatos(self):
        """
         Probando con el dataset M de candidatos
        """
        generador = cargar_datos("candidatos", "m")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 210)

        # Revisar posiciones aleatorias
        candidatos_cargados = [generador[0],
                               generador[3], generador[112], generador[-1]]

        candidatos_esperados = [
            Candidatos(id_candidato=45977, nombre='Fatima', id_distrito_postulacion=1, especie='Narval'),
            Candidatos(id_candidato=16070, nombre='Kobe', id_distrito_postulacion=2, especie='Burro'),
            Candidatos(id_candidato=94669, nombre='Dezzie', id_distrito_postulacion=47, especie='Caballo'),
            Candidatos(id_candidato=94848, nombre='Amir', id_distrito_postulacion=85, especie='Wallaby')
        ]

        self.assertCountEqual(candidatos_cargados, candidatos_esperados)

    @timeout(N_SECOND)
    def test_m_distritos(self):
        """
         Probando con el dataset M de distritos
        """
        generador = cargar_datos("distritos", "m")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 343)

        # Revisar posiciones aleatorias
        distritos_cargados = [generador[0],
                              generador[69], generador[312], generador[-1]]

        distritos_esperados = [
            Distritos(id_distrito=1, nombre='Distrito 1', id_comuna=1,provincia='Arica', region='Arica y Parinacota'),
            Distritos(id_distrito=17, nombre='Distrito 17', id_comuna=70, provincia='San Felipe de Aconcagua', region='Valparaiso'),
            Distritos(id_distrito=71, nombre='Distrito 71', id_comuna=313, provincia='Llanquihue', region='Los Lagos'),
            Distritos(id_distrito=85, nombre='Distrito 85', id_comuna=343, provincia='ultima Esperanza', region='Magallanes y de la Antartica Chilena')
        ]

        self.assertCountEqual(distritos_cargados, distritos_esperados)

    @timeout(N_SECOND)
    def test_m_locales(self):
        """
         Probando con el dataset M de locales
        """
        generador = cargar_datos("locales", "m")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 11270)

        # Revisar posiciones aleatorias
        locales_cargados = [generador[0], generador[6],
                            generador[1313], generador[-1]]

        locales_esperados = [
            Locales(id_local=1, nombre_local='Local 1', id_comuna=1, id_votantes=[218, 474, 518, 1189, 1349, 1523, 2336, 2485, 2685, 3064, 3285, 3876, 3984, 4187, 4546, 4636]),
            Locales(id_local=7, nombre_local='Local 7', id_comuna=1, id_votantes=[14206, 14406, 15079, 15383, 15524, 15724, 16901, 17589]),
            Locales(id_local=1314, nombre_local='Local 1314', id_comuna=40, id_votantes=[12972, 13132, 13172, 13639, 13869, 14011, 14321, 14616, 14972, 14994, 15391, 15443, 16023, 16604, 16699, 16725, 16752, 16981, 17703]),
            Locales(id_local=11270, nombre_local='Local 11270', id_comuna=343, id_votantes=[97534, 97687, 97804, 98188, 98503, 98532, 99993])
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_m_ponderadores(self):
        """
         Probando con el dataset M de ponderadores
        """
        generador = cargar_datos("ponderadores", "m")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 190)

        # Revisar posiciones aleatorias
        ponderadores_cargados = [generador[0], generador[18],
                                 generador[42], generador[-1]]

        ponderadores_esperados = [
            Ponderador(especie='Perro', ponderador=0.15),
            Ponderador(especie='Ciervo', ponderador=0.2857),
            Ponderador(especie='Aguila calva', ponderador=13.33),
            Ponderador(especie='Estrella espinosa', ponderador=400.0)
        ]

        self.assertCountEqual(ponderadores_cargados, ponderadores_esperados)

    @timeout(N_SECOND)
    def test_m_votos(self):
        """
         Probando con el dataset M de votos
        """
        generador = cargar_datos("votos", "m")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 100000)

        # Revisar posiciones aleatorias
        votos_cargados = [generador[0], generador[27],
                          generador[4952], generador[-1]]

        votos_esperados = [
            Votos(id_voto=1, id_animal_votante=96833, id_local=284, id_candidato=45977),
            Votos(id_voto=28, id_animal_votante=39067, id_local=1454, id_candidato=37113),
            Votos(id_voto=4953, id_animal_votante=19318, id_local=552, id_candidato=21210),
            Votos(id_voto=100000, id_animal_votante=99993, id_local=11270, id_candidato=73792)
        ]

        self.assertCountEqual(votos_cargados, votos_esperados)

    @timeout(N_SECOND)
    def test_l_animales(self):
        """
         Probando con el dataset L de animales
        """
        generador = cargar_datos("animales", "l")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 1000000)

        # Revisar posiciones aleatorias
        animales_cargados = [generador[0], generador[11],
                             generador[4444], generador[-1]]

        animales_esperados = [
            Animales(id=1, nombre='Alexander', especie='Numbat', id_comuna=114, peso_kg=0.2851, edad=88, fecha_nacimiento='1936/9'),
            Animales(id=12, nombre='Georgianna', especie='Manta', id_comuna=222, peso_kg=1401.08415, edad=47, fecha_nacimiento='1977/11'),
            Animales(id=4445, nombre='Lawton', especie='AraNa cangrejo', id_comuna=307, peso_kg=0.14026, edad=72, fecha_nacimiento='1952/11'),
            Animales(id=1000000, nombre='Elaine', especie='Comadreja', id_comuna=320, peso_kg=0.2966, edad=37, fecha_nacimiento='1987/2')
        ]

        self.assertCountEqual(animales_cargados, animales_esperados)

    @timeout(N_SECOND)
    def test_l_candidatos(self):
        """
         Probando con el dataset L de candidatos
        """
        generador = cargar_datos("candidatos", "l")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 180)

        # Revisar posiciones aleatorias
        candidatos_cargados = [generador[0],
                               generador[3], generador[112], generador[-1]]

        candidatos_esperados = [
            Candidatos(id_candidato=488302, nombre='Kaia', id_distrito_postulacion=1, especie='Pez loro'),
            Candidatos(id_candidato=516231, nombre='Mora', id_distrito_postulacion=2, especie='Caracol marino'),
            Candidatos(id_candidato=636402, nombre='Kathlene', id_distrito_postulacion=45, especie='Nutria'),
            Candidatos(id_candidato=228541, nombre='Eldora', id_distrito_postulacion=71, especie='Camello')
        ]

        self.assertCountEqual(candidatos_cargados, candidatos_esperados)

    @timeout(N_SECOND)
    def test_l_distritos(self):
        """
         Probando con el dataset L de distritos
        """
        generador = cargar_datos("distritos", "l")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 343)

        # Revisar posiciones aleatorias
        distritos_cargados = [generador[0],
                              generador[69], generador[312], generador[-1]]

        distritos_esperados = [
            Distritos(id_distrito=1, nombre='Distrito 1', id_comuna=1,provincia='Arica', region='Arica y Parinacota'),
            Distritos(id_distrito=17, nombre='Distrito 17', id_comuna=70, provincia='San Felipe de Aconcagua', region='Valparaiso'),
            Distritos(id_distrito=67, nombre='Distrito 67', id_comuna=313, provincia='Llanquihue', region='Los Lagos'),
            Distritos(id_distrito=71, nombre='Distrito 71', id_comuna=343, provincia='ultima Esperanza', region='Magallanes y de la Antartica Chilena')
        ]

        self.assertCountEqual(distritos_cargados, distritos_esperados)

    @timeout(N_SECOND)
    def test_l_locales(self):
        """
         Probando con el dataset L de locales
        """
        g_a = cargar_datos("locales", "l")

        # Revisar tipo de dato
        self.assertIsInstance(g_a, (map, Generator))

        # Revisar largo
        g_a = list(g_a)
        self.assertEqual(len(g_a), 59867)

        # Revisar posiciones aleatorias
        locales_cargados = [g_a[0], g_a[13], g_a[666], g_a[-1]]

        locales_esperados = [
            Locales(id_local=1, nombre_local='Local 1', id_comuna=1,
                    id_votantes=[32, 826, 1394, 1593, 2836, 3251, 3685, 3739, 3944,
								 4566, 4968, 5388, 5967, 6503, 6660, 7191, 7496, 7518,
								 7939, 7962, 8766, 9240, 9408, 9531, 9626, 10275, 10312,
								 10414, 10625, 11012, 11252, 11418, 11949]),

            Locales(id_local=14, nombre_local='Local 14', id_comuna=1,
                    id_votantes=[68958, 69136, 71667, 71977, 72125, 72676, 72693, 72905,
								 73524, 73767, 74399, 75388, 75823, 76416, 76441, 76785]),

            Locales(id_local=667, nombre_local='Local 667', id_comuna=4,
                    id_votantes=[858309, 858404, 858405, 858490, 858526, 859165, 859289,
								 859432, 859747, 859811, 859991, 860076]),

            Locales(id_local=59867, nombre_local='Local 59867', id_comuna=343,
                    id_votantes=[999863])
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_l_ponderadores(self):
        """
         Probando con el dataset L de ponderadores
        """
        generador = cargar_datos("ponderadores", "l")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 190)

        # Revisar posiciones aleatorias
        ponderadores_cargados = [generador[0], generador[18],
                                 generador[42], generador[-1]]

        ponderadores_esperados = [
            Ponderador(especie='Perro', ponderador=0.15),
            Ponderador(especie='Ciervo', ponderador=0.2857),
            Ponderador(especie='Aguila calva', ponderador=13.33),
            Ponderador(especie='Estrella espinosa', ponderador=400.0)
        ]

        self.assertCountEqual(ponderadores_cargados, ponderadores_esperados)

    @timeout(N_SECOND)
    def test_l_votos(self):
        """
         Probando con el dataset L de votos
        """
        generador = cargar_datos("votos", "l")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 1000000)

        # Revisar posiciones aleatorias
        votos_cargados = [generador[0], generador[27],
                          generador[4952], generador[-1]]

        votos_esperados = [
            Votos(id_voto=1, id_animal_votante=782439, id_local=479, id_candidato=488302),
            Votos(id_voto=28, id_animal_votante=450531, id_local=7149, id_candidato=420214),
            Votos(id_voto=4953, id_animal_votante=633958, id_local=283, id_candidato=488302),
            Votos(id_voto=1000000, id_animal_votante=999863, id_local=59867, id_candidato=418805)
        ]

        self.assertCountEqual(votos_cargados, votos_esperados)
    


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)

