import sys
import unittest
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from utilidades import Animales, Locales, Candidatos, Distritos, Ponderador, Votos
from consultas import cargar_datos


class TestCargarDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

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
            Animales(id=1, nombre='Anton', especie='Antílope saiga', id_comuna=239,
                     peso_kg=34.0, edad=16, fecha_nacimiento='2007/2'),
            Animales(id=12, nombre='Sienna', especie='Murciélago', id_comuna=74,
                     peso_kg=0.0351, edad=83, fecha_nacimiento='1940/3'),
            Animales(id=4445, nombre='Harrold', especie='Pez gato', id_comuna=13,
                     peso_kg=2.72, edad=104, fecha_nacimiento='1920/5'),
            Animales(id=10000, nombre='Netta', especie='Pez dorado', id_comuna=127,
                     peso_kg=0.094, edad=9, fecha_nacimiento='2015/9')
        ]

        self.assertCountEqual(animales_cargados, animales_esperados)

    def test_s_candidatos(self):
        """
         Probando con el dataset S de candidatos
        """
        generador = cargar_datos("candidatos", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 256)

        # Revisar posiciones aleatorias
        candidatos_cargados = [generador[0],
                               generador[3], generador[112], generador[-1]]

        candidatos_esperados = [
            Candidatos(id_candidato=2055, nombre='Toccara',
                       id_distrito_postulacion=1, especie='Medusa'),
            Candidatos(id_candidato=6182, nombre='Valentin',
                       id_distrito_postulacion=2, especie='Delfín nariz de botella'),
            Candidatos(id_candidato=9411, nombre='Tyshawn',
                       id_distrito_postulacion=47, especie='Escarabajo ciervo'),
            Candidatos(id_candidato=9617, nombre='Leroy',
                       id_distrito_postulacion=104, especie='Puercoespín')
        ]

        self.assertCountEqual(candidatos_cargados, candidatos_esperados)

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
                      provincia=' Arica', region=' Arica y Parinacota'),
            Distritos(id_distrito=22, nombre='Distrito 22', id_comuna=70,
                      provincia=' San Felipe de Aconcagua', region=' Valparaíso'),
            Distritos(id_distrito=93, nombre='Distrito 93', id_comuna=313,
                      provincia=' Llanquihue', region=' Los Lagos'),
            Distritos(id_distrito=104, nombre='Distrito 104', id_comuna=343,
                      provincia=' Última Esperanza', region=' Magallanes y de la Antártica Chilena')
        ]

        self.assertCountEqual(distritos_cargados, distritos_esperados)

    def test_s_locales(self):
        """
         Probando con el dataset S de locales
        """
        generador = cargar_datos("locales", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 2362)

        # Revisar posiciones aleatorias
        locales_cargados = [generador[0], generador[6],
                            generador[1313], generador[-1]]

        locales_esperados = [
            Locales(id_local=1, nombre_local='Local 1',
                    id_comuna=1, id_votantes=[385, 626]),
            Locales(id_local=7, nombre_local='Local 7',
                    id_comuna=1, id_votantes=[4004]),
            Locales(id_local=1314, nombre_local='Local 1314',
                    id_comuna=197, id_votantes=[7293]),
            Locales(id_local=2362, nombre_local='Local 2362', id_comuna=343,
                    id_votantes=[481, 1390, 1611, 1982, 2014, 2377, 3865, 3882, 4987, 5486,
                                 5724, 6589, 7259, 9243, 9262, 9617])
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    def test_s_ponderadores(self):
        """
         Probando con el dataset S de ponderadores
        """
        generador = cargar_datos("ponderadores", "s")

        # Revisar tipo de dato
        self.assertIsInstance(generador, (map, Generator))

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 208)

        # Revisar posiciones aleatorias
        ponderadores_cargados = [generador[0], generador[18],
                                 generador[42], generador[-1]]

        ponderadores_esperados = [
            Ponderador(especie='Perro', ponderador=5.5),
            Ponderador(especie='Ciervo', ponderador=0.444),
            Ponderador(especie='Águila calva', ponderador=13.33),
            Ponderador(especie='Estrella espinosa', ponderador=400.0)
        ]

        self.assertCountEqual(ponderadores_cargados, ponderadores_esperados)

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
            Votos(id_voto=1, id_animal_votante=385,
                  id_local=1, id_candidato=3055),
            Votos(id_voto=28, id_animal_votante=6354,
                  id_local=9, id_candidato=2055),
            Votos(id_voto=4953, id_animal_votante=9923,
                  id_local=1144, id_candidato=1395),
            Votos(id_voto=10000, id_animal_votante=9617,
                  id_local=2362, id_candidato=9617)
        ]

        self.assertCountEqual(votos_cargados, votos_esperados)

    def test_l_locales(self):
        """
         Probando con el dataset L de locales
        """
        g_a = cargar_datos("locales", "l")

        # Revisar tipo de dato
        self.assertIsInstance(g_a, (map, Generator))

        # Revisar largo
        g_a = list(g_a)
        self.assertEqual(len(g_a), 59925)

        # Revisar posiciones aleatorias
        locales_cargados = [g_a[0], g_a[13], g_a[666], g_a[-1]]

        locales_esperados = [
            Locales(id_local=1, nombre_local='Local 1', id_comuna=1,
                    id_votantes=[310, 623, 683, 1670, 1709, 1788, 2528, 2779]),

            Locales(id_local=14, nombre_local='Local 14', id_comuna=1,
                    id_votantes=[86682, 86837, 86858, 87008, 87165, 87908, 88002,
                                 88023, 88310, 89213, 90001, 90424, 90707]),

            Locales(id_local=667, nombre_local='Local 667', id_comuna=4,
                    id_votantes=[770834, 771065, 771420, 772310, 772875, 773303,
                                 773560, 774267, 774439, 774578, 775301, 775498]),

            Locales(id_local=59925, nombre_local='Local 59925', id_comuna=343,
                    id_votantes=[992027, 992216, 992356, 992779, 992826, 993053,
                                 993063, 993135, 993209, 993346, 993376, 994369,
                                 995175, 995391, 995790, 995822, 996033, 996803,
                                 996819, 996945, 997219, 997255, 997257, 997331,
                                 997685, 997829, 998530, 998546, 999150, 999467])
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)


if __name__ == "__main__":
    unittest.main(verbosity=2)
