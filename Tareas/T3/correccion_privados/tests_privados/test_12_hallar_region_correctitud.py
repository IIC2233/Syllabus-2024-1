import sys
import unittest
import os
import csv
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import hallar_region


class TestHallarRegionCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    def test_0(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada1 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapaca"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 9, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 10, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 11, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 12, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 13, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 14, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 15, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 16, "El Loa", "Antofagasta"),
            Distrito(4, "Distrito 4", 17, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 18, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 19, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 20, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 21, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 22, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 23, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 24, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 25, "Copiapo", "Atacama"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Local = namedtuple(
            "Local", ["id_local", "nombre_local", "id_comuna", "id_votantes"]
        )

        lista_entregada2 = [
            Local(1, "Local 1", 1, [385, 626]), 
            Local(2, "Local 2", 1, [1272, 1763, 1846, 1885, 2055, 2390, 3055]),
            Local(3, "Local 3", 1, [3203, 3227, 3532, 3559, 3618]), 
            Local(4, "Local 4", 1, [3667]),
            Local(5, "Local 5", 1, [3983]),
            Local(6, "Local 6", 1, [3984]), 
            Local(7, "Local 7", 1, [4004]),
            Local(8, "Local 8", 1, [4093, 4217, 4563, 4759, 4908, 5131, 5657, 6257]),
            Local(9, "Local 9", 1, [6344, 6354, 6376, 6617, 6740, 6755, 7114, 7122, 7941, 8453, 9035, 9407]),
            Local(10, "Local 10", 2, [714, 1475]), 
            Local(11, "Local 11", 2, [2095]),
            Local(12, "Local 12", 2, [2100, 2472, 2790, 2903, 3312, 3420]),
            Local(13, "Local 13", 2, [3461, 3968, 4403, 4755, 4909, 4912, 5429, 5634, 6371, 6800]),
            Local(14, "Local 14", 2, [7405, 7551, 7662, 8047, 8817, 9084, 9313]), 
            Local(15, "Local 15", 3, [38, 375, 688, 722, 802]),
            Local(16, "Local 16", 3, [852, 1049]), 
            Local(17, "Local 17", 3, [1236, 1524, 1782, 2007, 2178, 3535, 3567]),
            Local(18, "Local 18", 3, [3732, 3951, 4785, 5020, 5083]), 
            Local(19, "Local 19", 3, [5233, 5292]),
            Local(20, "Local 20", 3, [6073]), 
            Local(21, "Local 21", 3, [6182, 6400, 6815, 7533, 7605, 7691]),
            Local(22, "Local 22", 3, [8018, 8029, 8168, 8451, 8667, 9020, 9056, 9368, 9804, 9901]),
            Local(23, "Local 23", 4, [297, 738, 1177, 1465, 1649, 1794, 1942, 2034, 2090]),
            Local(24, "Local 24", 21, [2677, 3168, 3855, 4772, 5426, 5675, 5740, 6742, 7265, 7385, 7561, 7757]),
            Local(25, "Local 25", 25, [8111])
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = hallar_region(
            generador_entregado1, generador_entregado2, 5426
        )

        self.assertEqual(resultado_estudiante, "Atacama")

    def test_1(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada1 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapaca"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 9, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 10, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 11, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 12, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 13, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 14, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 15, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 16, "El Loa", "Antofagasta"),
            Distrito(4, "Distrito 4", 17, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 18, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 19, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 20, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 21, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 22, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 23, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 24, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 25, "Copiapo", "Atacama"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Local = namedtuple(
            "Local", ["id_local", "nombre_local", "id_comuna", "id_votantes"]
        )

        lista_entregada2 = [
            Local(1, "Local 1", 1, [385, 626]),
            Local(2, "Local 2", 1, [1272, 1763, 1846, 1885, 2055, 2390, 3055]),
            Local(3, "Local 3", 1, [3203, 3227, 3532, 3559, 3618]),
            Local(4, "Local 4", 1, [3667]),
            Local(5, "Local 5", 1, [3983]),
            Local(6, "Local 6", 1, [3984]),
            Local(7, "Local 7", 1, [4004]),
            Local(8, "Local 8", 1, [4093, 4217, 4563, 4759, 4908, 5131, 5657, 6257]),
            Local(9, "Local 9", 1, [
                6344, 6354, 6376, 6617, 6740, 6755, 7114, 7122, 7941, 8453, 9035, 9407
            ]),
            Local(10, "Local 10", 2, [714, 1475]),
            Local(11, "Local 11", 25, [2095]),
            Local(12, "Local 12", 2, [2100, 2472, 2790, 2903, 3312, 3420]),
            Local(13, "Local 13", 2, [3461, 3968, 4403, 4755, 4909, 4912, 5429, 5634, 6371, 6800]),
            Local(14, "Local 14", 2, [7405, 7551, 7662, 8047, 8817, 9084, 9313]),
            Local(15, "Local 15", 3, [38, 375, 688, 722, 802]),
            Local(16, "Local 16", 3, [852, 1049]),
            Local(17, "Local 17", 3, [1236, 1524, 1782, 2007, 2178, 3535, 3567]),
            Local(18, "Local 18", 3, [3732, 3951, 4785, 5020, 5083]),
            Local(19, "Local 19", 3, [5233, 5292]),
            Local(20, "Local 20", 3, [6073]),
            Local(21, "Local 21", 3, [6182, 6400, 6815, 7533, 7605, 7691]),
            Local(22, "Local 22", 3, [8018, 8029, 8168, 8451, 8667, 9020, 9056, 9368, 9804, 9901]),
            Local(23, "Local 23", 12, [297, 738, 1177, 1465, 1649, 1794, 1942, 2034, 2090]),
            Local(24, "Local 24", 13, [2677, 3168, 3855, 4772, 5426, 5675, 5740, 6742, 7265, 7385, 7561, 7757]),
            Local(25, "Local 25", 14, [8111])
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = hallar_region(
            generador_entregado1, generador_entregado2, 1465
        )

        self.assertEqual(resultado_estudiante, "Antofagasta")

    def test_2(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada1 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapaca"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 9, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 10, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 11, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 12, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 13, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 14, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 15, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 16, "El Loa", "Antofagasta"),
            Distrito(4, "Distrito 4", 17, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 18, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 19, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 20, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 21, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 22, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 23, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 24, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 25, "Copiapo", "Atacama"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Local = namedtuple(
            "Local", ["id_local", "nombre_local", "id_comuna", "id_votantes"]
        )

        lista_entregada2 = [
            Local(1, "Local 1", 1, [385, 626]),
            Local(2, "Local 2", 1, [1272, 1763, 1846, 1885, 2055, 2390, 3055]),
            Local(3, "Local 3", 1, [3203, 3227, 3532, 3559, 3618]),
            Local(4, "Local 4", 1, [3667]),
            Local(5, "Local 5", 1, [3983]),
            Local(6, "Local 6", 1, [3984]),
            Local(7, "Local 7", 1, [4004]),
            Local(8, "Local 8", 1, [4093, 4217, 4563, 4759, 4908, 5131, 5657, 6257]),
            Local(9, "Local 9", 1, [
                6344, 6354, 6376, 6617, 6740, 6755, 7114, 7122, 7941, 8453, 9035, 9407
            ]),
            Local(10, "Local 10", 2, [714, 1475]),
            Local(11, "Local 11", 2, [2095]),
            Local(12, "Local 12", 2, [2100, 2472, 2790, 2903, 3312, 3420]),
            Local(13, "Local 13", 2, [3461, 3968, 4403, 4755, 4909, 4912, 5429, 5634, 6371, 6800]),
            Local(14, "Local 14", 2, [7405, 7551, 7662, 8047, 8817, 9084, 9313]),
            Local(15, "Local 15", 3, [38, 375, 688, 722, 802]),
            Local(16, "Local 16", 3, [852, 1049]),
            Local(17, "Local 17", 3, [1236, 1524, 1782, 2007, 2178, 3535, 3567]),
            Local(18, "Local 18", 3, [3732, 3951, 4785, 5020, 5083]),
            Local(19, "Local 19", 3, [5233, 5292]),
            Local(20, "Local 20", 3, [6073]),
            Local(21, "Local 21", 3, [6182, 6400, 6815, 7533, 7605, 7691]),
            Local(22, "Local 22", 3, [8018, 8029, 8168, 8451, 8667, 9020, 9056, 9368, 9804, 9901]),
            Local(23, "Local 23", 4, [297, 738, 1177, 1465, 1649, 1794, 1942, 2034, 2090]),
            Local(24, "Local 24", 4, [
                2677, 3168, 3855, 4772, 5426, 5675, 5740, 6742, 7265, 7385, 7561, 7757
            ]),
            Local(25, "Local 25", 4, [8111])
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = hallar_region(
            generador_entregado1, generador_entregado2, 1236
        )

        self.assertEqual(resultado_estudiante, "Tarapaca")

    def test_3(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada1 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapaca"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 9, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 10, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 11, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 12, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 13, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 14, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 15, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 16, "El Loa", "Antofagasta"),
            Distrito(4, "Distrito 4", 17, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 18, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 19, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 20, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 21, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 22, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 23, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 24, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 25, "Copiapo", "Atacama"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Local = namedtuple(
            "Local", ["id_local", "nombre_local", "id_comuna", "id_votantes"]
        )

        lista_entregada2 = [
            Local(1, "Local 1", 1, [385, 626]),
            Local(2, "Local 2", 1, [1272, 1763, 1846, 1885, 2055, 2390, 3055]),
            Local(3, "Local 3", 1, [3203, 3227, 3532, 3559, 3618]),
            Local(4, "Local 4", 1, [3667]),
            Local(5, "Local 5", 1, [3983]),
            Local(6, "Local 6", 1, [3984]),
            Local(7, "Local 7", 1, [4004]),
            Local(8, "Local 8", 1, [4093, 4217, 4563, 4759, 4908, 5131, 5657, 6257]),
            Local(9, "Local 9", 1, [
                6344, 6354, 6376, 6617, 6740, 6755, 7114, 7122, 7941, 8453, 9035, 9407
            ]),
            Local(10, "Local 10", 2, [714, 1475]),
            Local(11, "Local 11", 2, [2095]),
            Local(12, "Local 12", 2, [2100, 2472, 2790, 2903, 3312, 3420]),
            Local(13, "Local 13", 2, [3461, 3968, 4403, 4755, 4909, 4912, 5429, 5634, 6371, 6800]),
            Local(14, "Local 14", 2, [7405, 7551, 7662, 8047, 8817, 9084, 9313]),
            Local(15, "Local 15", 3, [38, 375, 688, 722, 802]),
            Local(16, "Local 16", 3, [852, 1049]),
            Local(17, "Local 17", 3, [1236, 1524, 1782, 2007, 2178, 3535, 3567]),
            Local(18, "Local 18", 3, [3732, 3951, 4785, 5020, 5083]),
            Local(19, "Local 19", 3, [5233, 5292]),
            Local(20, "Local 20", 3, [6073]),
            Local(21, "Local 21", 3, [6182, 6400, 6815, 7533, 7605, 7691]),
            Local(22, "Local 22", 3, [8018, 8029, 8168, 8451, 8667, 9020, 9056, 9368, 9804, 9901]),
            Local(23, "Local 23", 4, [297, 738, 1177, 1465, 1649, 1794, 1942, 2034, 2090]),
            Local(24, "Local 24", 4, [
                2677, 3168, 3855, 4772, 5426, 5675, 5740, 6742, 7265, 7385, 7561, 7757
            ]),
            Local(25, "Local 25", 4, [8111])
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = hallar_region(
            generador_entregado1, generador_entregado2, 9407
        )

        self.assertEqual(resultado_estudiante, "Arica y Parinacota")

    def test_4(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada1 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapaca"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapaca"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapaca"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 9, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 10, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 11, "Tocopilla", "Tarapaca"),
            Distrito(4, "Distrito 4", 12, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 13, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 14, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 15, "Antofagasta", "Antofagasta"),
            Distrito(4, "Distrito 4", 16, "El Loa", "Antofagasta"),
            Distrito(4, "Distrito 4", 17, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 18, "El Loa", "Antofagasta"),
            Distrito(5, "Distrito 5", 19, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 20, "Tocopilla", "Antofagasta"),
            Distrito(5, "Distrito 5", 21, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 22, "Chañaral", "Atacama"),
            Distrito(5, "Distrito 5", 23, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 24, "Copiapo", "Atacama"),
            Distrito(6, "Distrito 6", 25, "Copiapo", "Atacama"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Local = namedtuple(
            "Local", ["id_local", "nombre_local", "id_comuna", "id_votantes"]
        )

        lista_entregada2 = [
            Local(1, "Local 1", 1, [385, 626]),
            Local(2, "Local 2", 1, [1272, 1763, 1846, 1885, 2055, 2390, 3055]),
            Local(3, "Local 3", 1, [3203, 3227, 3532, 3559, 3618]),
            Local(4, "Local 4", 1, [3667]),
            Local(5, "Local 5", 1, [3983]),
            Local(6, "Local 6", 1, [3984]),
            Local(7, "Local 7", 1, [4004]),
            Local(8, "Local 8", 1, [4093, 4217, 4563, 4759, 4908, 5131, 5657, 6257]),
            Local(9, "Local 9", 1, [
                6344, 6354, 6376, 6617, 6740, 6755, 7114, 7122, 7941, 8453, 9035, 9407
            ]),
            Local(10, "Local 10", 2, [714, 1475]),
            Local(11, "Local 11", 2, [2095]),
            Local(12, "Local 12", 16, [2100, 2472, 2790, 2903, 3312, 3420]),
            Local(13, "Local 13", 2, [3461, 3968, 4403, 4755, 4909, 4912, 5429, 5634, 6371, 6800]),
            Local(14, "Local 14", 2, [7405, 7551, 7662, 8047, 8817, 9084, 9313]),
            Local(15, "Local 15", 3, [38, 375, 688, 722, 802]),
            Local(16, "Local 16", 3, [852, 1049]),
            Local(17, "Local 17", 3, [1236, 1524, 1782, 2007, 2178, 3535, 3567]),
            Local(18, "Local 18", 3, [3732, 3951, 4785, 5020, 5083]),
            Local(19, "Local 19", 4, [5233, 5292]),
            Local(20, "Local 20", 5, [6073]),
            Local(21, "Local 21", 6, [6182, 6400, 6815, 7533, 7605, 7691]),
            Local(22, "Local 22", 8, [8018, 8029, 8168, 8451, 8667, 9020, 9056, 9368, 9804, 9901]),
            Local(23, "Local 23", 10, [297, 738, 1177, 1465, 1649, 1794, 1942, 2034, 2090]),
            Local(24, "Local 24", 22, [
                2677, 3168, 3855, 4772, 5426, 5675, 5740, 6742, 7265, 7385, 7561, 7757
            ]),
            Local(25, "Local 25", 25, [8111])
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        resultado_estudiante = hallar_region(
            generador_entregado1, generador_entregado2, 5426
        )

        self.assertEqual(resultado_estudiante, "Atacama")


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
