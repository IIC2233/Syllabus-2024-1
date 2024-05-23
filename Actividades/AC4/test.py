import unittest
from main import serializar_tortuga, verificar_rango, codificar_rango, \
    codificar_largo, separar_msg, encriptar, \
    deserializar_tortuga, decodificar_largo, \
    separar_msg_encriptado, decodificar_rango, desencriptar

from clases import Tortuga
from unittest.mock import patch

class TestEncriptar(unittest.TestCase):

    def test_serializar_tortuga(self):
        """
        Verifica el resultado segun lo pedido.
        """
        tama = Tortuga("Tama")
        test = serializar_tortuga(tama)
        res = bytearray(
            b'\x80\x04\x957\x00\x00\x00\x00\x00\x00\x00\x8c\x06clases\x94\x8c\x07Tortuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x04Tama\x94\x8c\x04edad\x94K\x00ub.')

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_serializar_tortuga_excepcion(self):
        """
        Verificar el correcto levantamiento de excepciones
        """
        # Verificar que lavanta excepcion
        def no_serializable(x):
            return x+1

        self.assertRaises(ValueError, serializar_tortuga, no_serializable)

        # Verificar que no levanta excepcion
        serializable = Tortuga("Tama")
        try:
            serializar_tortuga(serializable)
        except:
            self.fail(
                "Se levantó una excepción con un input que si se puede serializar")

    def test_verificar_rango_None(self):
        """
        Verifica que la funcion retorna None
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertIsNone(verificar_rango(mensaje, 1, 2))

    def test_verificar_rango_minimo(self):
        """
        Verificar excepción cuando inicio es menor a 0
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertRaises(AttributeError, verificar_rango, mensaje, -5, 2)

    def test_verificar_rango_maximo(self):
        """
        Verificar excepción cuando fin es mayor al largo
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertRaises(AttributeError, verificar_rango, mensaje, 0, 4444)

    def test_verificar_rango_creciente(self):
        """
        Verificar excepción cuando fin es menor a inicio
        """
        mensaje = bytearray(b'\x00\x01\x02\x03')
        self.assertRaises(AttributeError, verificar_rango, mensaje, 3, 0)

    def test_codificar_secuencia_pequeño(self):
        """
        Verificar correcta codificación con números pequeños
        """
        test = codificar_rango(1, 3)
        res = bytearray(b'\x00\x00\x01\x00\x00\x03')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_codificar_secuencia_grande(self):
        """
        Verificar correcta codificación con números grandes
        """
        test = codificar_rango(1, 4444)
        res = bytearray(b'\x00\x00\x01\x00\x11\\')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_codificar_largo_pequeño(self):
        """
        Verificar correcta codificación con largo pequeño
        """
        test = codificar_largo(4)
        res = bytearray(b'\x00\x00\x04')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_codificar_largo_grande(self):
        """
        Verificar correcta codificación con largo grande
        """
        test = codificar_largo(4242)
        res = bytearray(b'\x00\x10\x92')
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_separar_msg(self):
        """
        Verificar correcta separación de mensaje donde largo es impar
        """
        test = separar_msg(bytearray(b'\x00\x01\x02\x03'), 1, 3)
        res = [bytearray(b'\x03\x02\x01'), bytearray(b'\x00\x00\x01\x02')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_separar_msg_2(self):
        """
        Verificar correcta separación de mensaje donde largo es par
        """
        test = separar_msg(bytearray(b'\x00\x01\x02\x03'), 1, 2)
        res = [bytearray(b'\x01\x02'), bytearray(b'\x00\x00\x01\x03')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_separar_msg_3(self):
        """
        Verificar correcta separación de mensaje donde largo es impar y partiendo de 0
        """
        test = separar_msg(bytearray(b'\x08\x09\x0A\x0B'), 0, 2)
        res = [bytearray(b'\x0A\x09\x08'), bytearray(b'\x00\x01\x02\x0B')]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

class TestDesencriptar(unittest.TestCase):
    def test_deserializar_tortuga(self):
        """
        Verificar resultado correcto de esta función.
        """
        t1 = bytearray(b'\x80\x04\x957\x00\x00\x00\x00\x00\x00\x00\x8c\x06clases\x94\x8c\x07Tortuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x04Tama\x94\x8c\x04edad\x94K\x00ub.')
        test = deserializar_tortuga(t1)
        res = Tortuga("Tama")

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, Tortuga)
        # Verificar resultados
        self.assertDictEqual(test.__dict__, res.__dict__)

    def test_deserializar_tortuga_excepcion(self):
        """
        Verificar el correcto levantamiento de excepciones
        """
        # Verificar que lavanta excepcion
        no_deserializable = b'\x80\x14K\x91.'
        self.assertRaises(
            AttributeError, deserializar_tortuga, no_deserializable)

        # Verificar que no levanta excepcion
        desserializable = bytearray(
            b'\x80\x04\x957\x00\x00\x00\x00\x00\x00\x00\x8c\x06clases\x94\x8c\x07Tortuga\x94\x93\x94)\x81\x94}\x94(\x8c\x06nombre\x94\x8c\x04Tama\x94\x8c\x04edad\x94K\x00ub.')
        try:
            deserializar_tortuga(desserializable)
        except:
            self.fail(
                "Se levantó una excepción con un input que si se puede deserializar")

    def test_decodificar_largo_pequeño(self):
        """
        Verificar decodificación con largo pequeño
        """
        test = decodificar_largo(bytearray(b'\x00\x00\x02'))
        res = 2
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, int)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_decodificar_largo_grande(self):
        """
        Verificar decodificación con largo grande
        """
        test = decodificar_largo(bytearray(b'\xA1\x11\xA0'))
        res = 10555808
        # Verificar tipo de dato pedido
        self.assertIsInstance(test, int)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_separar_msg_encriptado_par(self):
        """
        Verificar que separa el mensaje correctamente
        """
        def new_decodificar_largo(*args, **kwargs):
            return 2

        with patch('main.decodificar_largo', side_effect=new_decodificar_largo):
            test = separar_msg_encriptado(
                bytearray(b'\x00\x00\x02\x02\x01\x03\x00\x01\x00\x00\x00\x01\x00\x00\x04'))
            res = [
                bytearray(b'\x02\x01'),
                bytearray(b'\x03\x00\x01\x00'),
                bytearray(b'\x00\x00\x01\x00\x00\x04')
            ]
            # Verificar tipo de dato pedido
            self.assertIsInstance(res, list)
            # Verificar resultados
            self.assertListEqual(test, res)

    def test_separar_msg_encriptado_impar(self):
        """
        Verificar que separa el mensaje correctamente y lo invierte cuando el largo es impar
        """
        def decodificar_largo(*args, **kwargs):
            return 3

        with patch('main.decodificar_largo', side_effect=decodificar_largo):
            test = separar_msg_encriptado(
                bytearray(b'\x00\x00\x03\x44\x02\x01\x03\x00\x01\x02\x00\x00\x00\x01\x00\x00\x05'))
            res = [
                bytearray(b'\x01\x02\x44'),
                bytearray(b'\x03\x00\x01\x02\x00'),
                bytearray(b'\x00\x00\x01\x00\x00\x05')
            ]
            # Verificar tipo de dato pedido
            self.assertIsInstance(res, list)
            # Verificar resultados
            self.assertListEqual(test, res)

    def test_decodificar_rango_pequeño(self):
        """
        Verificar decodificación de rango con números pequeños
        """
        test = decodificar_rango(bytearray(b'\x00\x00\x01\x00\x00\x03'))
        res = [1, 3]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_decodificar_rango_grande(self):
        """
        Verificar decodificación de rango con números grandes
        """
        test = decodificar_rango(bytearray(b'\x00\x00\x0B\x00\x11\x5C'))
        res = [11, 4444]
        # Verificar tipo de dato pedido
        self.assertIsInstance(res, list)
        # Verificar resultados
        self.assertListEqual(test, res)

    def test_desencriptar(self):
        """
        Verificar correcto armado del mensaje encriptado asumuiendo que "decodificar_largo", "separar" y "decodificar" están buenos
        """
        def separar_msg_encriptado(*args, **kwargs):
            return [bytearray(b'\x80\x02\x04'), 
                    bytearray(b'\x09\x00\x01\x02\x08'), 
                    bytearray(b'\x00\x00\x01\x00\x00\x03')]

        def decodificar_rango(*args, **kwargs):
            return [1, 3]
        
        def decodificar_largo(*args, **kwargs):
            return 3

        with patch('main.decodificar_largo', side_effect=decodificar_largo):
            with patch('main.separar_msg_encriptado', side_effect=separar_msg_encriptado):
                with patch('main.decodificar_rango', side_effect=decodificar_rango):
                    test = desencriptar(
                        bytearray(b'\x00\x00\x03\x04\x02\x80\x09\x00\x01\x02\x08\x00\x00\x01\x00\x00\x03'))
                    res = bytearray(b'\x09\x80\x02\x04\x08')
                    # Verificar tipo de dato pedido
                    self.assertIsInstance(res, bytearray)
                    # Verificar resultados
                    self.assertEqual(test, res)

class TestIntegracion(unittest.TestCase):

    def test_integracion_encriptar(self):
        '''
        Verificar que todo el proceso de encriptar cumple con lo pedido
        '''
        test = encriptar(bytearray(b'\x00\x01\x02\x03\x05'), 1, 3)
        res = bytearray(
            b'\x00\x00\x03\x03\x02\x01\x00\x00\x01\x02\x05\x00\x00\x01\x00\x00\x03')

        # Verificar tipo de dato pedido
        self.assertIsInstance(test, bytearray)
        # Verificar resultados
        self.assertEqual(test, res)

    def test_integracion_desencriptar(self):
        '''
        Verificar que todo el proceso de desencriptar cumple con lo pedido
        '''
        test = desencriptar(
            bytearray(b'\x00\x00\x02\x02\x01\x03\x00\x00\x01\x00\x00\x02\x00\x00\x03'))
        
        res = bytearray(b'\x03\x00\x02\x01')
        self.assertIsInstance(test, bytearray)
        self.assertEqual(test, res)

    def test_integracion_todo_proceso(self):
        '''
        Verificar que todo el proceso de encriptar y desencripar funcionan en conjunto
        '''
        original = Tortuga("tama")
        original.celebrar_anivesario()
        serializado = serializar_tortuga(original)
        encriptado = encriptar(serializado, 3, 14)
        desencriptado = desencriptar(encriptado)
        deserializado = deserializar_tortuga(desencriptado)
        self.assertDictEqual(original.__dict__, deserializado.__dict__)

    def test_integracion_todo_proceso_2(self):
        '''
        Verificar que todo el proceso de encriptar y desencripar funcionan en conjunto
        '''
        original = Tortuga("Pepa")
        original.celebrar_anivesario()
        original.celebrar_anivesario()
        serializado = serializar_tortuga(original)
        encriptado = encriptar(serializado, 5, 44)
        desencriptado = desencriptar(encriptado)
        deserializado = deserializar_tortuga(desencriptado)
        self.assertDictEqual(original.__dict__, deserializado.__dict__)

if __name__ == '__main__':
    unittest.main(verbosity=2)
