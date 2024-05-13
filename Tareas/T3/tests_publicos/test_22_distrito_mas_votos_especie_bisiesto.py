import sys
import unittest
from collections import namedtuple


# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import distrito_mas_votos_especie_bisiesto, cargar_datos
from test_solution import DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_S, DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_M, DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_L

class TestDistritoMasVotosEspecieBisiesto(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    def test_0(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(595, "Denisse", "Caballo", 1, 0.0282, 84, "1939/2"),
            Animal(596, "Ulysses", "Caballo", 2, 0.0091, 78, "1945/1"),
            Animal(597, "Alexandria", "Caballo", 3, 0.282, 14, "2010/9"),
            Animal(598, "Cassondra", "Caballo", 4, 90.0, 84, "1940/5"),  # bisiesto
            Animal(599, "Ann", "Caballo", 5, 1.38, 58, "1965/3"),
            Animal(600, "Kobe", "Caballo", 6, 414.0, 40, "1984/9"),  # bisiesto
            Animal(601, "Milagros", "Caballo", 7, 0.0222, 88, "1936/9"),  # bisiesto
            Animal(602, "Nery", "Caballo", 8, 2.02, 63, "1960/3"),  # bisiesto
            Animal(603, "Lon", "Caballo", 1, 2.4, 82, "1941/2"),
            Animal(604, "Darren", "Caballo", 2, 72.8, 60, "1963/1"),
            Animal(605, "Tilden", "Caballo", 3, 0.056, 93, "1931/10"),
            Animal(606, "Maryanne", "Caballo", 4, 1.35, 70, "1954/8"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )


        lista_entregada2 = [
            Voto(5, 595, 2, 597),
            Voto(6, 596, 2, 597),
            Voto(7, 597, 2, 597),
            Voto(8, 598, 2, 601),
            Voto(9, 599, 2, 602),
            Voto(10, 600, 3, 600),
            Voto(11, 601, 3, 597),
            Voto(12, 602, 3, 597),
            Voto(13, 603, 3, 600),
            Voto(14, 604, 3, 602),
            Voto(15, 605, 4, 602),
            Voto(16, 606, 5, 603),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada3 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapacá"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapacá"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapacá"),
        ]    

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = distrito_mas_votos_especie_bisiesto(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            "Caballo",
        )


        string_esperado = "El distrito 4 fue el que tuvo más votos emitidos por animales de la especie Caballo nacidos en año bisiesto."

        self.assertEqual(resultado_estudiante, string_esperado)

    def test_1(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(595, "Denisse", "Caballo", 1, 0.0282, 84, "1939/2"),
            Animal(596, "Ulysses", "Perro", 2, 0.0091, 78, "1945/1"),
            Animal(597, "Alexandria", "Caballo", 3, 0.282, 14, "2010/9"),
            Animal(598, "Cassondra", "Perro", 4, 90.0, 84, "1940/5"),  # bisiesto
            Animal(599, "Ann", "Caballo", 5, 1.38, 58, "1965/3"),
            Animal(600, "Kobe", "Caballo", 6, 414.0, 40, "1984/9"),  # bisiesto
            Animal(601, "Milagros", "Caballo", 7, 0.0222, 88, "1936/9"),  # bisiesto
            Animal(602, "Nery", "Caballo", 8, 2.02, 63, "1960/3"),  # bisiesto
            Animal(603, "Lon", "Caballo", 1, 2.4, 82, "1941/2"),
            Animal(604, "Darren", "Caballo", 2, 72.8, 60, "1963/1"),
            Animal(605, "Tilden", "Caballo", 3, 0.056, 93, "1931/10"),
            Animal(606, "Maryanne", "Caballo", 4, 1.35, 70, "1954/8"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )


        lista_entregada2 = [
            Voto(5, 595, 2, 597),
            Voto(6, 596, 2, 597),
            Voto(7, 597, 2, 597),
            Voto(8, 598, 2, 601),
            Voto(9, 599, 2, 602),
            Voto(10, 600, 3, 600),
            Voto(11, 601, 3, 597),
            Voto(12, 602, 3, 597),
            Voto(13, 603, 3, 600),
            Voto(14, 604, 3, 602),
            Voto(15, 605, 4, 602),
            Voto(16, 606, 5, 603),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada3 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapacá"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapacá"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapacá"),

        ]

        generador_entregado3 = (element for element in lista_entregada3)

        resultado_estudiante = distrito_mas_votos_especie_bisiesto(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            "Perro",
        )


        string_esperado = "El distrito 3 fue el que tuvo más votos emitidos por animales de la especie Perro nacidos en año bisiesto."

        self.assertEqual(resultado_estudiante, string_esperado)

    def test_2(self):
        """
        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(595, "Denisse", "Caballo", 1, 0.0282, 84, "1939/2"),
            Animal(596, "Ulysses", "Gallina", 2, 0.0091, 78, "1945/1"),
            Animal(597, "Alexandria", "Caballo", 3, 0.282, 14, "2010/9"),
            Animal(598, "Cassondra", "Caballo", 4, 90.0, 84, "1940/5"),  # bisiesto
            Animal(599, "Ann", "Gato", 5, 1.38, 58, "1965/3"),
            Animal(600, "Kobe", "Caballo", 6, 414.0, 40, "1984/9"),  # bisiesto
            Animal(601, "Milagros", "Gato", 7, 0.0222, 88, "1936/9"),  # bisiesto
            Animal(602, "Nery", "Caballo", 8, 2.02, 63, "1960/3"),  # bisiesto
            Animal(603, "Lon", "Caballo", 1, 2.4, 82, "1941/2"),
            Animal(604, "Darren", "Caballo", 2, 72.8, 60, "1963/1"),
            Animal(605, "Tilden", "Gallina", 3, 0.056, 93, "1931/10"),
            Animal(606, "Maryanne", "Caballo", 4, 1.35, 70, "1954/8"),
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )


        lista_entregada2 = [
            Voto(5, 595, 2, 597),
            Voto(6, 596, 2, 597),
            Voto(7, 597, 2, 597),
            Voto(8, 598, 2, 601),
            Voto(9, 599, 2, 602),
            Voto(10, 600, 3, 600),
            Voto(11, 601, 3, 597),
            Voto(12, 602, 3, 597),
            Voto(13, 603, 3, 600),
            Voto(14, 604, 3, 602),
            Voto(15, 605, 4, 602),
            Voto(16, 606, 5, 603),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada3 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapacá"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapacá"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapacá"),
        ]

        generador_entregado3 = (element for element in lista_entregada3)


        resultado_estudiante = distrito_mas_votos_especie_bisiesto(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            "Caballo"
        )


        string_esperado = "El distrito 4 fue el que tuvo más votos emitidos por animales de la especie Caballo nacidos en año bisiesto."

        self.assertEqual(resultado_estudiante, string_esperado)

    def test_3(self):
        """

        Verifica que el test funcione para para tests pequeños.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ]
        )

        lista_entregada1 = [
            Animal(595, "Denisse", "Caballo", 1, 0.0282, 84, "1939/2"),
            Animal(596, "Ulysses", "Caballo", 2, 0.0091, 78, "1945/1"),
            Animal(597, "Alexandria", "Caballo", 3, 0.282, 14, "2010/9"),
            Animal(598, "Cassondra", "Caballo", 4, 90.0, 84, "1940/5"),  # bisiesto
            Animal(599, "Ann", "Caballo", 5, 1.38, 58, "1965/3"),
            Animal(600, "Kobe", "Perro", 6, 414.0, 40, "1984/9"),  # bisiesto
            Animal(601, "Milagros", "Perro", 7, 0.0222, 88, "1936/9"),  # bisiesto
            Animal(602, "Nery", "Lemur", 4, 2.02, 63, "1960/3"),  # bisiesto
            Animal(603, "Lon", "Caballo", 1, 2.4, 82, "1941/2"),
            Animal(604, "Darren", "Caballo", 2, 72.8, 60, "1963/1"),
            Animal(605, "Tilden", "Caballo", 3, 0.056, 93, "1931/10"),
            Animal(606, "Maryanne", "Caballo", 4, 1.35, 70, "1954/8")
        ]

        generador_entregado1 = (element for element in lista_entregada1)

        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )


        lista_entregada2 = [
            Voto(5, 595, 2, 597),
            Voto(6, 596, 2, 597),
            Voto(7, 597, 2, 597),
            Voto(8, 598, 2, 601),
            Voto(9, 599, 2, 602),
            Voto(10, 600, 3, 600),
            Voto(11, 601, 3, 597),
            Voto(12, 602, 3, 597),
            Voto(13, 603, 3, 600),
            Voto(14, 604, 3, 602),
            Voto(15, 605, 4, 602),
            Voto(16, 606, 5, 603)
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )


        lista_entregada3 = [
            Distrito(1, 'Distrito 1', 1, 'Arica', 'Arica y Parinacota'),
            Distrito(1, 'Distrito 1', 2, 'Parinacota', 'Arica y Parinacota'),
            Distrito(2, 'Distrito 2', 3, 'Iquique', 'Tarapacá'),
            Distrito(3, 'Distrito 3', 4, 'El Tamarugal', 'Tarapacá'),
            Distrito(3, 'Distrito 3', 5, 'Iquique', 'Tarapacá'),
            Distrito(4, 'Distrito 4', 6, 'Iquique', 'Tarapacá'),
            Distrito(4, 'Distrito 4', 7, 'Tocopilla', 'Tarapacá'),
            Distrito(4, 'Distrito 4', 8, 'Tocopilla', 'Tarapacá'),

        ]

        generador_entregado3 = (element for element in lista_entregada3)


        resultado_estudiante = distrito_mas_votos_especie_bisiesto(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            "Lemur"
        )

        string_esperado = "El distrito 3 fue el que tuvo más votos emitidos por animales de la especie Lemur nacidos en año bisiesto."


        self.assertEqual(resultado_estudiante, string_esperado)

    def test_4(self):
        """
        Verifica que el test funcione para para tests pequeños. Caso empate.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(595, "Denisse", "Caballo", 1, 0.0282, 84, "1939/2"),
            Animal(596, "Ulysses", "Leon", 2, 0.0091, 78, "1945/1"),
            Animal(597, "Alexandria", "Caballo", 3, 0.282, 14, "2010/9"),
            Animal(598, "Cassondra", "Tortuga", 1, 90.0, 84, "1940/5"),  # bisiesto
            Animal(599, "Ann", "Tortuga", 1, 1.38, 58, "1965/3"),
            Animal(600, "Kobe", "Tortuga", 2, 414.0, 40, "1984/9"),  # bisiesto
            Animal(601, "Milagros", "Tortuga", 8, 0.0222, 88, "1936/9"),  # bisiesto
            Animal(602, "Nery", "Tortuga", 8, 2.02, 63, "1960/3"),  # bisiesto
            Animal(603, "Lon", "Caballo", 1, 2.4, 82, "1941/2"),
            Animal(604, "Darren", "Gato", 2, 72.8, 60, "1963/1"),
            Animal(605, "Tilden", "Tortuga", 3, 0.056, 93, "1931/10"),
            Animal(606, "Maryanne", "Caballo", 4, 1.35, 70, "1954/8"),
        ]

        
        generador_entregado1 = (element for element in lista_entregada1)


        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada2 = [
            Voto(5, 595, 2, 597),
            Voto(6, 596, 2, 597),
            Voto(7, 597, 2, 597),
            Voto(8, 598, 2, 601),
            Voto(9, 599, 2, 602),
            Voto(10, 600, 3, 600),
            Voto(11, 601, 3, 597),
            Voto(12, 602, 3, 597),
            Voto(13, 603, 3, 600),
            Voto(14, 604, 3, 602),
            Voto(15, 605, 4, 602),
            Voto(16, 606, 5, 603),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada3 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapacá"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapacá"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapacá"),
        ]
        
        generador_entregado3 = (element for element in lista_entregada3)


        resultado_estudiante = distrito_mas_votos_especie_bisiesto(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            "Tortuga",
        )

        string_esperado = "El distrito 1 fue el que tuvo más votos emitidos por animales de la especie Tortuga nacidos en año bisiesto."

        self.assertEqual(resultado_estudiante, string_esperado)

    def test_5(self):
        """
        Verifica que el test funcione para para tests pequeños. Caso no hay animales nacidos en año bisiesto. Como hay empate de "0 votantes", se retorna el distrito con menor id.
        """

        Animal = namedtuple(
            "Registro",
            [
                "id",
                "nombre",
                "especie",
                "id_comuna",
                "peso_kg",
                "edad",
                "fecha_nacimiento",
            ],
        )

        lista_entregada1 = [
            Animal(595, "Denisse", "Caballo", 1, 0.0282, 84, "1939/2"),
            Animal(596, "Ulysses", "Leon", 2, 0.0091, 78, "1945/1"),
            Animal(597, "Alexandria", "Caballo", 3, 0.282, 14, "2010/9"),
            Animal(598, "Cassondra", "Tortuga", 1, 90.0, 83, "1941/5"), 
            Animal(599, "Ann", "Tortuga", 1, 1.38, 58, "1965/3"),
            Animal(600, "Kobe", "Tortuga", 2, 414.0, 39, "1985/9"),  
            Animal(601, "Milagros", "Tortuga", 8, 0.0222, 87, "1937/9"), 
            Animal(602, "Nery", "Tortuga", 8, 2.02, 62, "1961/3"),  
            Animal(603, "Lon", "Caballo", 1, 2.4, 82, "1941/2"),
            Animal(604, "Darren", "Gato", 2, 72.8, 60, "1963/1"),
            Animal(605, "Tilden", "Tortuga", 3, 0.056, 93, "1931/10"),
            Animal(606, "Maryanne", "Caballo", 4, 1.35, 70, "1954/8"),
        ]

        
        generador_entregado1 = (element for element in lista_entregada1)


        Voto = namedtuple(
            "Voto", ["id_voto", "id_animal_votante", "id_local", "id_candidato"]
        )

        lista_entregada2 = [
            Voto(5, 595, 2, 597),
            Voto(6, 596, 2, 597),
            Voto(7, 597, 2, 597),
            Voto(8, 598, 2, 601),
            Voto(9, 599, 2, 602),
            Voto(10, 600, 3, 600),
            Voto(11, 601, 3, 597),
            Voto(12, 602, 3, 597),
            Voto(13, 603, 3, 600),
            Voto(14, 604, 3, 602),
            Voto(15, 605, 4, 602),
            Voto(16, 606, 5, 603),
        ]

        generador_entregado2 = (element for element in lista_entregada2)

        Distrito = namedtuple(
            "Distrito", ["id_distrito", "nombre", "id_comuna", "provincia", "region"]
        )

        lista_entregada3 = [
            Distrito(1, "Distrito 1", 1, "Arica", "Arica y Parinacota"),
            Distrito(1, "Distrito 1", 2, "Parinacota", "Arica y Parinacota"),
            Distrito(2, "Distrito 2", 3, "Iquique", "Tarapacá"),
            Distrito(3, "Distrito 3", 4, "El Tamarugal", "Tarapacá"),
            Distrito(3, "Distrito 3", 5, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 6, "Iquique", "Tarapacá"),
            Distrito(4, "Distrito 4", 7, "Tocopilla", "Tarapacá"),
            Distrito(4, "Distrito 4", 8, "Tocopilla", "Tarapacá"),
        ]
        
        generador_entregado3 = (element for element in lista_entregada3)


        resultado_estudiante = distrito_mas_votos_especie_bisiesto(
            generador_entregado1,
            generador_entregado2,
            generador_entregado3,
            "Tortuga",
        )

        string_esperado = "El distrito 1 fue el que tuvo más votos emitidos por animales de la especie Tortuga nacidos en año bisiesto."

        self.assertEqual(resultado_estudiante, string_esperado)

    def test_6(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = distrito_mas_votos_especie_bisiesto(g_a, g_v, g_d, "Gato")
        expected_output = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_S
        
        self.assertEqual(resultado, expected_output)

    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = distrito_mas_votos_especie_bisiesto(g_a, g_v, g_d, "Gato")
        expected_output = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_M

        self.assertEqual(resultado, expected_output)

    def test_8(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_d = cargar_datos("distritos", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = distrito_mas_votos_especie_bisiesto(g_a, g_v, g_d, "Gato")
        expected_output = DISTRITO_MAS_VOTOS_ESPECIE_BISIESTO_L
        
        self.assertEqual(resultado, expected_output)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
