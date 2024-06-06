import re
import api
import signal
import yolanda
import platform
import unittest
from datetime import date
from functools import wraps

"""
Código del TimeoutError extraido y adaptado de
https://github.com/pnpnpn/timeout-decorator/tree/master
"""
N_SECOND = 2
R_SECOND = 15

class TimeoutError(AssertionError):

    """Thrown when a timeout occurs in the `timeout` context manager."""

    def __init__(self, value="Timed Out"):
        self.value = value

    def __str__(self):
        return repr(self.value)


def timeout(seconds=None):
    def decorate(function):
        def handler(signum, frame):
            raise TimeoutError("Timeout")

        @wraps(function)
        def new_function(*args, **kwargs):
            new_seconds = kwargs.pop("timeout", seconds)
            if new_seconds:
                old = signal.signal(signal.SIGALRM, handler)
                signal.setitimer(signal.ITIMER_REAL, new_seconds)

            if not seconds:
                return function(*args, **kwargs)

            try:
                return function(*args, **kwargs)
            finally:
                if new_seconds:
                    signal.setitimer(signal.ITIMER_REAL, 0)
                    signal.signal(signal.SIGALRM, old)

        if platform.system().lower() == "windows":
            return function
        return new_function

    return decorate


class VerificarConsultas(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        host = "localhost"
        port = 4444
        database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor = api.Server(host, port, database, mode=2)
        self.yolanda = yolanda.Yolanda(host, port)
        self.servidor.start()

    @classmethod
    def tearDownClass(self):
        self.servidor.w_s.shutdown()
        self.servidor.stop()
        self.servidor.join()
        self.servidor.server_started.wait()

    def setUp(self) -> None:
        """
        Reinicia la base de datos antes de cada test
        """
        self.servidor.mode = 2
        self.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        
    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    #####################
    #      Saludar      #
    #####################
    
    def test_saludar_mode_1_verificar_todo(self):
        """
        Revisa que el método saludar retorne las respuestas correctas
        en el formato correcto.
        """
        self.servidor.mode = 1
        respuesta = self.yolanda.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y es un hermoso día para recibir un horóscopo"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    def test_saludar_mode_2_verificar_todo(self):
        """
        Revisa que el método saludar retorne las respuestas correctas
        en el formato correcto.
        """
        self.servidor.mode = 2
        respuesta = self.yolanda.saludar()
        today = date.today()
        resultado = f"Hoy es {today} y me da gusto escribir horóscopos"

        self.assertIn("status-code", respuesta)
        self.assertIn("saludo", respuesta)
        self.assertEqual(respuesta["status-code"], 200)
        self.assertEqual(respuesta["saludo"], resultado)

    #######################
    # Verificar horóscopo #
    #######################

    def test_verificar_horoscopo_tipo_respuesta(self):
        """
        Verifica que el método retorne un booleano.
        """
        respuesta = self.yolanda.verificar_horoscopo("piscis")
        self.assertIsInstance(respuesta, bool)

    def test_verificar_horoscopo_si_existe(self):
        """
        Verifica que el método retorne True para signos
        presentes en la base de datos.
        """
        respuesta = self.yolanda.verificar_horoscopo("piscis")
        self.assertEqual(respuesta, True)

    def test_verificar_horoscopo_no_existe(self):
        """
        Verifica que el método retorne False para signos
        no presentes en la base de datos.
        """
        respuesta = self.yolanda.verificar_horoscopo("UWU")
        self.assertEqual(respuesta, False)

    #####################
    #   Dar horóscopo   #
    #####################

    def test_dar_horoscopo_verificar_keys(self):
        """
        Verifica que el método retorne un diccionario con
        la estructura pedida
        """
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIn("status-code", respuesta)
        self.assertIn("mensaje", respuesta)

    def test_dar_horoscopo_existe_verificar_status_code(self):
        """
        Verifica que el método retorne el código correcto
        cuando el signo existe en la base de datos.
        """
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["status-code"], 200)

    def test_dar_horoscopo_existe_verificar_mensaje(self):
        """
        Verifica que el método retorne el mensaje correcto
        cuando el signo existe en la base de datos.
        """
        respuesta = self.yolanda.dar_horoscopo("piscis")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database["piscis"])

    def test_dar_horoscopo_no_existe_verificar_todo(self):
        """
        Verifica que el método retorne el código y mensaje correcto
        cuando el signo no existe en la base de datos.
        """
        respuesta = self.yolanda.dar_horoscopo("UWU")
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["status-code"], 400)
        self.assertEqual(respuesta["mensaje"], "El signo no existe")

    ###########################
    # Dar horóscopo aleatorio #
    ###########################

    def test_dar_horoscopo_aleatorio_mode_1(self):
        """
        Verifica que el método retorne un diccionario,
        cuyo mensaje corresponda a uno de los signos de la
        base de datos
        """
        self.servidor.mode = 1
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        signo = list(self.database.keys())[0]
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database[signo])

    def test_dar_horoscopo_aleatorio_mode_2(self):
        """
        Verifica que el método retorne un diccionario,
        cuyo mensaje corresponda a uno de los signos de la
        base de datos
        """
        self.servidor.mode = 2
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        signo = list(self.database.keys())[-1]
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["mensaje"], self.database[signo])

    def test_dar_horoscopo_aleatorio_mode_3(self):
        """
        Verifica que el método falle en ciertos casos,
        dando el mensaje y error correcto.
        """
        self.servidor.mode = 3
        respuesta = self.yolanda.dar_horoscopo_aleatorio()
        self.assertIsInstance(respuesta, dict)
        self.assertEqual(respuesta["status-code"], 500)
        self.assertEqual(respuesta["mensaje"], "ups, no pude")

# Clase que ejecuta los tests
class VerificarModificaciones(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        host = "localhost"
        port = 4444
        database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor = api.Server(host, port, database, mode=2)
        self.yolanda = yolanda.Yolanda(host, port)
        self.servidor.start()

    @classmethod
    def tearDownClass(self):
        self.servidor.w_s.shutdown()
        self.servidor.stop()
        self.servidor.join()
        self.servidor.server_started.wait()

    def setUp(self) -> None:
        """
        Reinicia la base de datos antes de cada test
        """
        self.servidor.mode = 2
        self.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        self.servidor.database = {
            "acuario": "Hoy será un hermoso día",
            "leo": "No salgas de casa.... te lo recomiendo",
            "piscis": "Sé uno con la naturaleza, te traerá buena suerte",
        }
        
    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    #####################
    # Agregar horoscopo #
    #####################
    @timeout(N_SECOND)
    def test_agregar_horoscopo_no_autorizado(self):
        """
        Se comprueba que envía el mensaje pedido
        cuando el error de la API es 401 (no autorizado)
        """
        respuesta = self.yolanda.agregar_horoscopo("leo", "grande messi", "FAIL")
        self.assertEqual(respuesta, "Agregar horóscopo no autorizado")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_signo_ya_existe(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el signo ya existía en
        la base de datos.
        """
        respuesta = self.yolanda.agregar_horoscopo(
            "leo", "grande messi", "morenoiic2233"
        )
        self.assertEqual(respuesta, "El signo ya existe, no puedes modificarlo")
    
    @timeout(N_SECOND)
    def test_agregar_horoscopo_signo_mensaje_muy_corto(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el mensaje a colocar es demasiado corto.
        """
        respuesta = self.yolanda.agregar_horoscopo("leo", "a", "morenoiic2233")
        self.assertEqual(respuesta, "El mensaje debe tener más de 4 caracteres")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_ok_verificar_respuesta(self):
        """
        Se comprueba que envia el mensaje pedido cuando
        la request de la API fue exitosa (200)
        """
        mensaje = "grande messi"
        respuesta = self.yolanda.agregar_horoscopo(
            "Sagitario", mensaje, "morenoiic2233"
        )
        self.assertEqual(respuesta, "La base de YolandAPI ha sido actualizada")

    @timeout(N_SECOND)
    def test_agregar_horoscopo_ok_verificar_base_datos(self):
        """
        Se comprueba que tras realizar una request exitosa a la api,
        el mensaje almacenado en la base de datos haya sido el enviado.
        """
        mensaje = "grande messi"
        self.yolanda.agregar_horoscopo("Sagitario", mensaje, "morenoiic2233")
        self.assertIn("Sagitario", self.servidor.database)
        self.assertEqual(mensaje, self.servidor.database["Sagitario"])

    ########################
    # Actualizar horoscopo #
    ########################
    @timeout(N_SECOND)
    def test_actualizar_horoscopo_no_autorizado(self):
        """
        Se comprueba que envía el mensaje pedido
        cuando el error de la API es 401 (no autorizado)
        """
        respuesta = self.yolanda.actualizar_horoscopo("leo", "grande messi", "FAIL")
        self.assertEqual(respuesta, "Editar horóscopo no autorizado")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_signo_no_existe(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el signo a enviar no existe en la base de datos.
        """
        respuesta = self.yolanda.actualizar_horoscopo(
            "messi", "grande messi", "morenoiic2233"
        )
        self.assertEqual(respuesta, "El signo no existe")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_signo_mensaje_muy_corto(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el mensaje a colocar es demasiado corto.
        """
        respuesta = self.yolanda.actualizar_horoscopo("leo", "a", "morenoiic2233")
        self.assertEqual(respuesta, "El mensaje debe tener más de 4 caracteres")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_ok_verificar_respuesta(self):
        """
        Se comprueba que envia el mensaje pedido cuando
        la request de la API fue exitosa (200)
        """
        mensaje = "grande messi"
        respuesta = self.yolanda.actualizar_horoscopo("leo", mensaje, "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandAPI ha sido actualizada")

    @timeout(N_SECOND)
    def test_actualizar_horoscopo_ok_verificar_base_datos(self):
        """
        Se comprueba que tras realizar una request exitosa a la api,
        el mensaje almacenado en la base de datos haya sido el enviado.
        """
        mensaje = "grande messi"
        self.yolanda.actualizar_horoscopo("leo", mensaje, "morenoiic2233")
        self.assertEqual(mensaje, self.servidor.database["leo"])

    ##################
    # Eliminar signo #
    ##################
    @timeout(N_SECOND)
    def test_eliminar_signo_no_autorizado(self):
        """
        Se comprueba que envía el mensaje pedido
        cuando el error de la API es 401 (no autorizado)
        """
        respuesta = self.yolanda.eliminar_signo("leo", "FAIL")
        self.assertEqual(respuesta, "Eliminar signo no autorizado")

    @timeout(N_SECOND)
    def test_eliminar_signo_signo_no_existe(self):
        """
        Se comprueba que envía el mensaje pedido cuando
        el error de la API es 400 y el signo a borrar no existe en la base de datos.
        """
        respuesta = self.yolanda.eliminar_signo("messi", "morenoiic2233")
        self.assertEqual(respuesta, "El signo no existe")

    @timeout(N_SECOND)
    def test_eliminar_signo_ok_verificar_respuesta(self):
        """
        Se comprueba que envia el mensaje pedido cuando
        la request de la API fue exitosa (200)
        """
        respuesta = self.yolanda.eliminar_signo("leo", "morenoiic2233")
        self.assertEqual(respuesta, "La base de YolandAPI ha sido actualizada")

    @timeout(N_SECOND)
    def test_eliminar_signo_ok_verificar_base_datos(self):
        """
        Se comprueba que tras realizar una request exitosa a la api,
        el signo ya no se encuentre en la base de datos.
        """
        self.yolanda.eliminar_signo("leo", "morenoiic2233")
        self.assertNotIn("leo", self.servidor.database)


# Clase que ejecuta los tests de uso de regex
class RegexTests(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        """
        Levanta una instancia de yolanda para probar las RegEx
        En particular se encarga de comprobar las variables:
        - regex_validador_fechas
        - regex_extractor_signos
        """
        super().__init__(*args, **kwargs)
        self.yolanda = yolanda.Yolanda('', '')

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    ##############################
    #      Validador fechas      #
    ##############################

    @timeout(R_SECOND)
    def test_validar_fechas_validas(self):
        """
        Todos los elementos de la lista de casos_validos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_validador_fechas`
        """
        casos_validos = [
            "07\tde AgosTo de 95",
            "18 de abril de\n2018",
            "30 de JUNIO\tde 2023",
            "8 de ctbr de 01",
            "14 de carzo de 2010",
            "11 de\tnoviembre de 22",
            "46 de ABRIL de 1999",
        ]

        for i, texto in enumerate(casos_validos):
            with self.subTest(msg=texto):
                respuesta = re.match(self.yolanda.regex_validador_fechas, texto)
                self.assertIsInstance(respuesta, re.Match)
                self.assertEqual(respuesta.group(0), texto)

    @timeout(R_SECOND)
    def test_validar_fechas_invalidas(self):
        """
        Ninguno de los elementos de la lista de casos_invalidos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_validador_fechas`
        """
        casos_invalidos = [
            "007 de agosto de 1995",
            "11 de noviembre de 022",
            "0 de sept de 20220",
            "18 de abril de 2118",
            "30 de junIO de 1823",
            "8, octubre de 2001",
            "14/marzo/2010",
            "6 de 07 de 1999",
        ]

        for i, texto in enumerate(casos_invalidos):
            with self.subTest(msg=texto):
                respuesta = re.search(self.yolanda.regex_validador_fechas, texto)
                self.assertEqual(respuesta, None)

    #######################################
    #      Verificar extractor signo      #
    #######################################
    @timeout(R_SECOND)
    def test_extraer_signo_valido(self):
        """
        Todos los elementos de la lista de casos_validos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_extractor_signo`
        """
        casos_validos = [
            "Los   capricornianos pueden   dormir la mejor siesta del semestre.",
            "Las\tSAGITARIANAS\t\n\tpueden vivir el mejor día de su vida.",
            "Las\nacuarianas pueden volver a escuchar la mejor canción de su vida.",
            "Los    escorpianos pueden escuchar música con las aquarianas.",
            "Las liBRianas pueden ser libres por 1 día.",
            "Los cncrianos    pueden ver su serie favorita en la noche.",
            "Las pisqianas pueden    comer su poste favorito mañana.",
        ]
        signos_casos = [
            "capricornianos",
            "SAGITARIANAS",
            "acuarianas",
            "escorpianos",
            "liBRianas",
            "cncrianos",
            "pisqianas",
        ]

        for i, texto in enumerate(casos_validos):
            with self.subTest(msg=texto):
                respuesta = re.search(self.yolanda.regex_extractor_signo, texto)
                self.assertIsInstance(respuesta, re.Match)
                signo = respuesta.group(1)
                self.assertEqual(signo, signos_casos[i])

    @timeout(R_SECOND)
    def test_extraer_signo_invalido(self):
        """
        Ninguno de los elementos de la lista de casos_invalidos abajo
        son textos que deberían ser capturados por la
        RegEx `regex_extractor_signo`
        """
        casos_invalidos = [
            "Los_arianos pueden   dormir la mejor siesta del semestre.",                # No hay espacio entre Los y signo
            "Las pisqianas_pueden    comer su poste favorito mañana.",                  # No hay espacio entre signo y pueden
            "Lis   tiirinis  pueden   vivir el mejor día de su vida.",                  # Lis no es Las o Los
            "los\tacuarianas\npueden volver a escuchar la mejor canción de su vida.",   # Los no parte con mayúscula
            "Los escorpio pueden escuchar música con las aquarianas.",                  # Signo no está en plural
            "Las liBRianas serán libres por 1 día.",                                    # Falta pueden después del signo
            "Los cncrianos    pueden ver su serie favorita en la noche",                # Falta el punto al final
        ]

        for i, texto in enumerate(casos_invalidos):
            with self.subTest(msg=texto):
                respuesta = re.search(self.yolanda.regex_extractor_signo, texto)
                self.assertEqual(respuesta, None)

if __name__ == "__main__":
    unittest.main(verbosity=2)
