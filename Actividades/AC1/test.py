from abc import ABC
import unittest
from unittest.mock import patch
import types

from clases import Vehiculo, AutoBencina, AutoElectrico, FaitHibrido, Camioneta, Telsa


class VerificarClaseVehiculo(unittest.TestCase):

    def test_no_puede_instanciarse(self):
        """
        Verifica correcto instanciamiento de clase Vehiculo
        """
        self.assertRaises(TypeError, Vehiculo, 15)

    def test_metodo_abstracto_definido(self):
        """
        Verifica que Vehiculo es una clase abstracta
        """
        self.assertIn('recorrer', Vehiculo.__abstractmethods__)

    def test_herencia_abc(self):
        """
        Verifica uso de abc
        """
        self.assertIn(ABC, Vehiculo.__mro__)

    def test_property_energia_definida(self):
        """
        Verifica que energia es property
        """
        self.assertIsInstance(Vehiculo.energia, property)

    def test_property_autonomia_definida(self):
        """
        Verifica que autonomia es property
        """
        self.assertIsInstance(Vehiculo.autonomia, property)


class VerificarClaseAutoBencina(unittest.TestCase):

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia se hace correctamente en AutoBencina
        """
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=100)
            mock.assert_called_once()

    def test_herencia_vehiculo(self):
        """
        Verifica que AutoBencina hereda de Vehiculo
        """
        self.assertIn(Vehiculo, AutoBencina.__mro__)

    def test_init_correcto(self):
        """
        Verifica correcto instanciamiento de AutoBencina
        """
        id_inicial = Vehiculo.identificador
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=100)
        self.assertEqual(auto.bencina_favorita, 93)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, 'chev')
        self.assertEqual(auto.energia, 100)
        self.assertEqual(auto.identificador, id_inicial)

        auto2 = AutoBencina(bencina_favorita=95, rendimiento=11, marca='chev2', energia=101)
        self.assertEqual(auto2.bencina_favorita, 95)
        self.assertEqual(auto2.rendimiento, 11)
        self.assertEqual(auto2.marca, 'chev2')
        self.assertEqual(auto2.energia, 101)
        self.assertEqual(auto2.identificador, id_inicial + 1)
    
    def test_init_correcto_con_property(self):
        """
        Verifica correcto setter de la property
        """
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=-9999)
        self.assertEqual(auto.energia, 0)

    def test_valor_energia_por_defecto_correcto_auto_bencina(self):
        """
        Correcto valor por defecto de energia en AutoBencina
        """
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev')
        self.assertEqual(auto.energia, 120)

    def test_metodo_recorrer_definido(self):
        """
        Verifica que el metodo de recorrer de AutoBencina esta bien definido
        """
        self.assertIsInstance(AutoBencina.recorrer, types.FunctionType)

    def test_recorrer_sobre_autonomia(self):
        """
        Verifica que AutoBencina recorre correctamente estando por sobre su autonomia
        """
        auto = AutoBencina(bencina_favorita=93, rendimiento=10, marca='chev', energia=100)
        resultado = auto.recorrer(100000)
        self.assertEqual(auto.energia, 0)
        self.assertEqual(resultado, 'Anduve por 1000Km y gaste 100L de bencina')

    def test_recorrer_bajo_autonomia(self):
        """
        Verifica que AutoBencina recorre correctamente estando bajo su autonomia
        """
        auto = AutoBencina(bencina_favorita=93, rendimiento=11, marca='chev', energia=100)
        resultado = auto.recorrer(99)
        self.assertEqual(auto.energia, 91)
        self.assertEqual(resultado, 'Anduve por 99Km y gaste 9L de bencina')

    def test_autonomia(self):
        """
        Verifica que la autonomia de AutoBencina es bien calculada
        """
        auto = AutoBencina(bencina_favorita=93, rendimiento=3, marca='chev', energia=2)
        self.assertEqual(auto.autonomia, 6)
        auto2 = AutoBencina(bencina_favorita=93, rendimiento=7, marca='chev', energia=3)
        self.assertEqual(auto2.autonomia, 21)


class VerificarClaseAutoElectrico(unittest.TestCase):

    def test_herencia_vehiculo(self):
        """
        Verifica que AutoElectrico hereda de Vehiculo
        """
        self.assertIn(Vehiculo, AutoElectrico.__mro__)

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia se hace correctamente en AutoElectrico
        """
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            AutoElectrico(vida_util_bateria=2, rendimiento=10, marca='c', energia=100)
            mock.assert_called_once()

    def test_init_correcto(self):
        """
        Verifica correcto instanciamiento de AutoElectrico
        """
        auto = AutoElectrico(vida_util_bateria=2, rendimiento=10, marca='c', energia=100)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.vida_util_bateria, 2)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.energia, 100)

        auto2 = AutoElectrico(vida_util_bateria=1, rendimiento=11, marca='c2', energia=101)
        self.assertEqual(auto2.rendimiento, 11)
        self.assertEqual(auto2.vida_util_bateria, 1)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 101)

    def test_valor_energia_por_defecto_correcto_auto_electrico(self):
        """
        Correcto valor por defecto de energia en AutoElectrico
        """
        auto = AutoElectrico(vida_util_bateria=93, rendimiento=10, marca='chev')
        self.assertEqual(auto.energia, 120)

    def test_recorrer_sobre_autonomia(self):
        """
        Verifica que AutoElectrico recorre correctamente estando por sobre su autonomia
        """
        auto = AutoElectrico(vida_util_bateria=93, rendimiento=10, marca='chev', energia=100)
        resultado = auto.recorrer(100000)
        self.assertEqual(auto.energia, 0)
        self.assertEqual(resultado, 'Anduve por 1000Km y gaste 100W de energia electrica')

    def test_recorrer_bajo_autonomia(self):
        """
        Verifica que AutoElectrico recorre correctamente estando bajo su autonomia
        """
        auto = AutoElectrico(vida_util_bateria=93, rendimiento=11, marca='chev', energia=100)
        resultado = auto.recorrer(99)
        self.assertEqual(auto.energia, 91)
        self.assertEqual(resultado, 'Anduve por 99Km y gaste 9W de energia electrica')


class VerificarClaseCamioneta(unittest.TestCase):

    def test_herencia_vehiculo_bencina(self):
        """
        Verifica que Camioneta hereda de AutoBencina
        """
        self.assertIn(AutoBencina, Camioneta.__mro__)

    def test_init_correcto(self):
        """
        Verifica correcto instanciamiento de Camioneta
        """
        auto = Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                         energia=100, bencina_favorita=93)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.bencina_favorita, 93)
        self.assertEqual(auto.energia, 100)

        auto2 = Camioneta(capacidad_maleta=1, rendimiento=1, marca='c2',
                          energia=101, bencina_favorita=95)
        self.assertEqual(auto2.rendimiento, 1)
        self.assertEqual(auto2.bencina_favorita, 95)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 101)

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia de Vehiculo se hace correctamente en Camioneta
        """
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                      energia=100, bencina_favorita=92)
            mock.assert_called_once()

    def test_llama_init_auto_bencina(self):
        """
        Verifica que la herencia de AutoBencina se hace correctamente en Camioneta
        """
        with patch('clases.AutoBencina.__init__') as mock:
            mock.return_value = None
            Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                      energia=100, bencina_favorita=92)
            mock.assert_called_once()

    def test_no_llama_init_auto_electrico(self):
        """
        Verifica que la herencia no viene de AutoElectrico en Camioneta
        """
        with patch('clases.AutoElectrico.__init__') as mock:
            mock.return_value = None
            Camioneta(capacidad_maleta=10, rendimiento=10, marca='c',
                      energia=100, bencina_favorita=92)
            mock.assert_not_called()
    
    def test_recorrer_Camioneta(self):
        """
        Verifica que el metodo recorrer de Camioneta hace lo pedido
        """
        auto2 = Camioneta(capacidad_maleta=1, rendimiento=1, marca='c2',
                          energia=101, bencina_favorita=95)
        res = auto2.recorrer(10)
        self.assertEqual(res, 'Anduve por 10Km y gaste 10L de bencina')


class VerificarClaseTelsa(unittest.TestCase):

    def test_herencia_vehiculo_Electrico(self):
        """
        Verifica que Telsa hereda de AutoElectrico
        """
        self.assertIn(AutoElectrico, Telsa.__mro__)

    def test_init_correcto(self):
        """
        Verifica correcto instanciamiento de Telsa
        """
        auto = Telsa(rendimiento=10, marca='c', energia=100, vida_util_bateria=3)
        self.assertEqual(auto.rendimiento, 10)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.energia, 100)
        self.assertEqual(auto.vida_util_bateria, 3)

        auto2 = Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
        self.assertEqual(auto2.rendimiento, 1)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 101)
        self.assertEqual(auto2.vida_util_bateria, 1)

    def test_llama_init_vehiculo(self):
        """
        Verifica que la herencia de Vehiculo se hace correctamente en Telsa
        """
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            Telsa(capacidad_maleta=1, vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            mock.assert_called_once()

    def test_no_llama_init_auto_bencina(self):
        """
        Verifica que la herencia no viene de AutoBencina en Telsa
        """
        with patch('clases.AutoBencina.__init__') as mock:
            mock.return_value = None
            Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            mock.assert_not_called()

    def test_llama_init_auto_electrico(self):
        """
        Verifica que la herencia de AutoElectrico se hace correctamente en Telsa
        """
        with patch('clases.AutoElectrico.__init__') as mock:
            mock.return_value = None
            Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
            mock.assert_called_once()

    def test_llama_recorrer_clase_padres(self):
        """
        Verifica que el metodo recorrer de Telsa utiliza correctamente
         el metodo de su clase padre AutoElectrico
        """
        try:
            with patch('clases.AutoElectrico.recorrer') as mock_1:
                mock_1.return_value = 'test'
                auto = Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
                res = auto.recorrer(12)
                mock_1.assert_called_once_with(auto, 12)
                self.assertEqual(res, 'test de forma inteligente')
        except AssertionError:
            with patch('clases.AutoElectrico.recorrer') as mock_1:
                mock_1.return_value = 'test'
                auto = Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
                res = auto.recorrer(12)
                mock_1.assert_called_once_with(12) 
                self.assertEqual(res, 'test de forma inteligente')

    def test_recorrer_Telsa(self):
        """
        Verifica que el metodo recorrer de Telsa hace lo pedido
        """
        auto = Telsa(vida_util_bateria=1, rendimiento=1, marca='c2', energia=101)
        res = auto.recorrer(12)
        self.assertEqual(res, 'Anduve por 12Km y gaste 12W de energia electrica de forma inteligente')


class VerificarClaseFaitHibrido(unittest.TestCase):

    def test_herencia_vehiculo_Electrico(self):
        """
        Verifica que FaitHibrido hereda de AutoElectrico
        """
        self.assertIn(AutoElectrico, FaitHibrido.__mro__)

    def test_herencia_vehiculo_Bencina(self):
        """
        Verifica que FaitHibrido hereda de AutoBencina
        """
        self.assertIn(AutoBencina, FaitHibrido.__mro__)

    def test_init_correcto(self):
        """
        Verifica correcto instanciamiento de FaitHibrido
        """
        auto = FaitHibrido(rendimiento=7, marca='c', energia=101, bencina_favorita=95)
        self.assertEqual(auto.rendimiento, 7)
        self.assertEqual(auto.marca, 'c')
        self.assertEqual(auto.energia, 101)
        self.assertEqual(auto.vida_util_bateria, 5)

        auto2 = FaitHibrido(rendimiento=2, marca='c2', energia=131, bencina_favorita=95)
        self.assertEqual(auto2.rendimiento, 2)
        self.assertEqual(auto2.marca, 'c2')
        self.assertEqual(auto2.energia, 131)
        self.assertEqual(auto2.vida_util_bateria, 5)

    def test_llama_init_vehiculo_solo_una_vez(self):
        """
        Verifica que la herencia de Vehiculo se hace correctamente en FaitHibrido
        """
        with patch('clases.Vehiculo.__init__') as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
            mock.assert_called_once()

    def test_llama_recorrer_clases_padres(self):
        """
        Verifica que el metodo recorrer de FaitHibrido utiliza correctamente
         el metodo de sus clases padres AutoElectrico y AutoBencina
        """
        with patch('clases.AutoBencina.recorrer') as mock:
            mock.return_value = 'a'
            with patch('clases.AutoElectrico.recorrer') as mock2:
                mock2.return_value = 'b'
                auto = FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
                res = auto.recorrer(12)
                mock.assert_called_once_with(auto, 6.0)
                mock2.assert_called_once_with(auto, 6.0)
                self.assertIn(res, ['a b', 'b a'])

    def test_llama_recorrer_clases_padres2(self):
        with patch('clases.AutoBencina.recorrer') as mock:
            mock.return_value = 'd'
            with patch('clases.AutoElectrico.recorrer') as mock2:
                mock2.return_value = 'c'
                auto2 = FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
                res = auto2.recorrer(10)
                mock.assert_called_once_with(auto2, 5.0)
                mock2.assert_called_once_with(auto2, 5.0)
                self.assertIn(res, ['c d', 'd c'])

    def test_no_llama_init_auto_bencina(self):
        """
        Verifica que la herencia de AutoBencina se hace correctamente en FaitHibrido
        """
        with patch('clases.AutoBencina.__init__') as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
            mock.assert_called_once()

    def test_llama_init_auto_electrico(self):
        """
        Verifica que la herencia de AutoElectrico se hace correctamente en FaitHibrido
        """
        with patch('clases.AutoElectrico.__init__') as mock:
            mock.return_value = None
            FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
            mock.assert_called_once()
    
    def test_recorrer_FaitHibrido(self):
        """
        Verifica que el metodo recorrer de FaitHibrido hace lo pedido
        """
        auto2 = FaitHibrido(rendimiento=1, marca='c2', energia=101, bencina_favorita=95)
        res = auto2.recorrer(10)
        self.assertIn(res, ['Anduve por 5.0Km y gaste 5W de energia electrica Anduve por 5.0Km y gaste 5L de bencina',
                            'Anduve por 5.0Km y gaste 5L de bencina Anduve por 5.0Km y gaste 5W de energia electrica'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
