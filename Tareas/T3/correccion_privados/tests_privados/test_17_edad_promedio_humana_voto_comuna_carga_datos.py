import sys
import unittest

# Advertencia, la siguiente línea solo es utilizada por el cuerpo docente.
# Se considerará una mala práctica ocuparlo en sus evaluaciones.
sys.path.append("..")

from consultas import edad_promedio_humana_voto_comuna, cargar_datos
from utilidades import Animales, Ponderador, Votos
from test_solution import EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_S, EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_M, EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_L

from timeout_function import timeout
N_SECOND = 20 

class TestEdadPromedioHumanaVotoComunaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None
    
    @timeout(N_SECOND)
    def test_5(self):
        """
         Verifica que se retorne los votantes cuando se manejan pequeños datos.
        """
        carpeta = "s"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = edad_promedio_humana_voto_comuna(g_a, g_p, g_v, 5088, 19)
        expected_output = EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_S
        
        self.assertEqual(resultado, expected_output)
    
    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne los votantes cuando se manejan medianos datos.
        """
        carpeta = "m"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = edad_promedio_humana_voto_comuna(g_a, g_p, g_v, 11825, 105)
        expected_output = EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_M
        self.assertEqual(resultado, expected_output)

    @timeout(40)    
    def test_7(self):
        """
        Verifica que se retorne los votantes cuando se manejan grandes datos.
        """
        carpeta = "l"
        g_a = cargar_datos("animales", carpeta)
        g_p = cargar_datos("ponderadores", carpeta)
        g_v =  cargar_datos("votos", carpeta)
        resultado = edad_promedio_humana_voto_comuna(g_a, g_p, g_v, 995616, 5)
        expected_output = EDAD_PROMEDIO_HUMANA_VOTO_COMUNA_L
        
        self.assertEqual(resultado, expected_output)
     
if __name__ == "__main__":
    from io import StringIO  
    
    from unittest.mock import patch

    with patch("sys.stdout", new=StringIO()):
        unittest.main(verbosity=2)
