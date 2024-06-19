import sys
import unittest
from collections import namedtuple
from typing import Generator

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import votos_interespecie

class TestVotosInterespecieCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
         Verifica que el test funcione para para tests pequeños. Test con true.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Pez sierra', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Tortuga', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Coati', 292, 7.8, 31, '1992/11'),
                Animal(531, 'Johanna', 'Langosta', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 84, '1939/2'),
                Animal(596, 'Ulysses', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(597, 'Alexandria', 'Estrella espinosa', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(600, 'Kobe', 'Pez sierra', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 60, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9'),
                Animal(81, 'Joetta', 'Buho', 1, 0.44, 13, '2011/9')
        ]
        
        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 531),
            Voto(2, 1763, 1, 2055),
            Voto(3, 2055, 2, 81),
            Voto(4, 531, 2, 2055),
            Voto(5, 595, 2, 2055),
            Voto(6, 596, 2, 3055),
            Voto(8, 598, 2, 2055),
            Voto(9, 599, 2, 531),
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado2 = (element for element in lista_entregada2)
        
        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada3 = [
            Candidato(2055, 'Toccara', 1, 'Pez sierra'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
        ]

        generador_entregado3 = (element for element in lista_entregada3)   

        resultado_estudiante = votos_interespecie(generador_entregado1, generador_entregado2, generador_entregado3, True)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
             Animal(600, 'Kobe', 'Pez sierra', 273, 414.0, 40, '1984/9'),
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_1(self):
        """
         Verifica que el test funcione para para tests pequeños. Test con false.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Estrella espinosa', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Coati', 292, 7.8, 31, '1992/11'),
                Animal(531, 'Johanna', 'Langosta', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 85, '1939/2'),
                Animal(596, 'Antonio', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(597, 'Alexandria', 'Estrella espinosa', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(600, 'Kobe', 'Pez sierra', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 61, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9'),
                Animal(81, 'Joetta', 'Buho', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 531),
            Voto(2, 1763, 1, 2055),
            Voto(3, 2055, 2, 3055),
            Voto(4, 531, 2, 531),
            Voto(5, 595, 2, 2055),
            Voto(6, 596, 2, 3055),
            Voto(7, 597, 2, 3055),
            Voto(8, 598, 2, 2055),
            Voto(9, 599, 2, 531),
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada3 = [
            Candidato(2055, 'Toccara', 1, 'Pez dorado'),
            Candidato(3055, 'Phil', 1, 'Estrella espinosa'),
            Candidato(81, 'Joetta', 4, 'Buho'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_interespecie(generador_entregado1, generador_entregado2, generador_entregado3, False)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Pez dorado', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 85, '1939/2'),
                Animal(596, 'Antonio', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(600, 'Kobe', 'Pez sierra', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9')
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_2(self):
        """
         Verifica que el test funcione para para tests pequeños. Test con true.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Langosta', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Zorro volador', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Tortuga', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Coati', 292, 7.8, 31, '1992/11'),
                Animal(531, 'Johanna', 'Langosta', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 85, '1939/2'),
                Animal(596, 'Ulysses', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(597, 'Alexandria', 'Estrella espinosa', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(600, 'Kobe', 'Pez sierra', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Tortuga', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 61, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 531),
            Voto(2, 1763, 1, 2055),
            Voto(3, 2055, 2, 3055),
            Voto(4, 531, 2, 531),
            Voto(5, 595, 2, 2055),
            Voto(6, 596, 2, 3055),
            Voto(7, 597, 2, 3055),
            Voto(8, 598, 2, 2055),
            Voto(9, 599, 2, 531),
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 3984, 6, 2055),
            Voto(18, 3, 6, 3)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada3 = [
            Candidato(3, 'Ernst', 1, 'Llama'),
            Candidato(2055, 'Toccara', 1, 'Zorro volador'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(531, 'Johanna', 2, 'Langosta'),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_interespecie(generador_entregado1, generador_entregado2, generador_entregado3, True)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
            Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
            Animal(385, 'Gay', 'Langosta', 190, 288.0, 45, '1979/11'),
            Animal(602, 'Nery', 'Tortuga', 212, 2.02, 64, '1960/3'),
            Animal(531, 'Johanna', 'Langosta', 248, 0.525, 67, '1957/12'), 
            Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9')
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_3(self):
        """
         Verifica que el test funcione para para tests pequeños. Test con false.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Medusa', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Tortuga', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Coati', 292, 7.8, 31, '1992/11'),
                Animal(531, 'Johanna', 'Langosta', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 85, '1939/2'),
                Animal(596, 'Ulysses', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(597, 'Alexandria', 'Estrella espinosa', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(600, 'Kobe', 'Medusa', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 61, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9'),
                Animal(6400, 'Kellen', 'Pinguino emperador', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 531),
            Voto(2, 1763, 1, 2055),
            Voto(3, 2055, 2, 3055),
            Voto(4, 531, 2, 531),
            Voto(5, 595, 2, 2055),
            Voto(6, 596, 2, 3055),
            Voto(7, 597, 2, 3055),
            Voto(8, 598, 2, 2055),
            Voto(9, 599, 2, 531),
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 3984, 6, 2055),
            Voto(18, 3, 5, 2055),
            Voto(19, 3056, 6, 2055)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada3 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(6400, 'Kellen', 2, 'Pinguino emperador'),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_interespecie(generador_entregado1, generador_entregado2, generador_entregado3, False)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Coati', 292, 7.8, 31, '1992/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Medusa', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 85, '1939/2'),
                Animal(596, 'Ulysses', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(597, 'Alexandria', 'Estrella espinosa', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 61, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9')
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)

    def test_4(self):
        """
         Verifica que el test funcione para para tests pequeños. Test con false por defecto.
        """

        Animal = namedtuple('Registro', ['id', 'nombre', 'especie', 'id_comuna', 'peso_kg', 'edad', 'fecha_nacimiento'])

        lista_entregada1 = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Medusa', 248, 0.525, 67, '1957/12'),
                Animal(3055, 'Phil', 'Tortuga', 248, 0.525, 67, '1957/12'),
                Animal(3, 'Ernst', 'Llama', 116, 81.0, 60, '1964/9'),
                Animal(3056, 'Shreya', 'Coati', 292, 7.8, 31, '1992/11'),
                Animal(531, 'Johanna', 'Langosta', 248, 0.525, 67, '1957/12'),
                Animal(595, 'Denisse', 'Gamba', 139, 0.0282, 85, '1939/2'),
                Animal(596, 'Ulysses', 'Caracol de tierra', 68, 0.0091, 79, '1945/1'),
                Animal(597, 'Alexandria', 'Tortuga', 16, 0.282, 14, '2010/9'),
                Animal(598, 'Cassondra', 'Serpiente piton', 281, 90.0, 84, '1940/5'),
                Animal(599, 'Ann', 'Suricata', 5, 1.38, 59, '1965/3'),
                Animal(600, 'Kobe', 'Medusa', 273, 414.0, 40, '1984/9'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 61, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9'),
                Animal(6400, 'Kellen', 'Pinguino emperador', 1, 0.44, 13, '2011/9')
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple('Voto', ['id_voto', 'id_animal_votante', 'id_local', 'id_candidato'])

        lista_entregada2 = [
            Voto(1, 385, 1, 531),
            Voto(2, 1763, 1, 2055),
            Voto(3, 2055, 2, 3055),
            Voto(10, 600, 3, 2055),
            Voto(11, 601, 3, 3055),
            Voto(12, 602, 3, 3055),
            Voto(13, 603, 3, 2055),
            Voto(14, 604, 3, 3055),
            Voto(15, 605, 4, 2055),
            Voto(16, 606, 5, 2055),
            Voto(17, 3984, 6, 2055)
        ]

        generador_entregado2 = (element for element in lista_entregada2)
        
        Candidato = namedtuple('Candidato', ['id_candidato', 'nombre', 'id_distrito_postulacion', 'especie'])

        lista_entregada3 = [
            Candidato(2055, 'Toccara', 1, 'Medusa'),
            Candidato(3055, 'Phil', 1, 'Tortuga'),
            Candidato(531, 'Johanna', 5, 'Langosta'),
            Candidato(6400, 'Kellen', 2, 'Pinguino emperador'),
        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = votos_interespecie(generador_entregado1, generador_entregado2, generador_entregado3)

        self.assertIsInstance(resultado_estudiante, (list, tuple, set, filter, map, Generator, zip))

        lista_esperada = [
                Animal(385, 'Gay', 'Tortuga marina', 190, 288.0, 45, '1979/11'),
                Animal(1763, 'Lexi', 'Gecko', 61, 0.071, 34, '1957/8'),
                Animal(2055, 'Toccara', 'Medusa', 248, 0.525, 67, '1957/12'),
                Animal(601, 'Milagros', 'Escarabajo ciervo', 178, 0.0222, 88, '1936/9'),
                Animal(602, 'Nery', 'Lemur', 212, 2.02, 64, '1960/3'),
                Animal(603, 'Lon', 'Bagre', 201, 2.4, 83, '1941/2'),
                Animal(604, 'Darren', 'Foca', 41, 72.8, 61, '1963/1'),
                Animal(605, 'Tilden', 'Pez dorado', 23, 0.056, 93, '1931/10'),
                Animal(606, 'Maryanne', 'Pato', 293, 1.35, 70, '1954/8'),
                Animal(3984, 'Hollie', 'Zorro volador', 1, 0.44, 13, '2011/9')
        ]

        resultado_lista = [animal for animal in resultado_estudiante]

        self.assertCountEqual(resultado_lista, lista_esperada)


if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
