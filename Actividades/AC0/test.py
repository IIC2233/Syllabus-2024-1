
import main
import unittest
import subprocess

class VerificarInstanciaUsuario(unittest.TestCase):
    def test_puede_instanciarse_usuario(self):
        """
        Verifica correcta importacion de clase Usuario en main.
        """
        self.assertRaises(TypeError, main.Usuario)

class VerificarInstanciaItem(unittest.TestCase):
    def test_puede_instanciarse_item(self):
        """
        Verifica correcta importacion de clase Item en main.
        """
        self.assertRaises(TypeError, main.Item)

class VerificarMetodos(unittest.TestCase):     
    def test_cargar_items(self):
        """
        Verifica que los items fueron cargados en una lista.
        """
        items = main.cargar_items()
        self.assertEqual(items[4].nombre, 'queso azul')
        self.assertEqual(items[4].puntos, 70)
        self.assertEqual(items[4].precio, 6800)
        
    def test_crear_usuario(self):
        """
        Verifica que se instancia correctamente Usuario al crear usuario.
        """
        user_sin = main.crear_usuario(False)
        user_con = main.crear_usuario(True)
        self.assertEqual(user_sin.suscripcion, False)
        self.assertEqual(user_con.suscripcion, True)
    
    def test_print_crear_usuario(self):
        """
        Verifica que imprime lo pedido al crear usuario.
        """
        process = subprocess.Popen(
            ["python", "-c", "from main import crear_usuario; crear_usuario(True)"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate()
        self.assertEqual(stdout, "> Usuario con suscripcion. Puntos: 0\n")

class VerificarSalidasTerminal(unittest.TestCase):
    def test_flujo_programa(self):
        """
        Verifica la ejecucion del programa.
        """
        process = subprocess.Popen(
            ["python", "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate()
        mensaje_out_con = [
            "> Usuario con suscripcion. Puntos: 0\n",
            "> Items para elegir:\n",
            "1) harina sin polvos: $1500 / 10 puntos\n",
            "2) papas rusticas: $4000 / 50 puntos\n",
            "3) te en hoja: $3500 / 35 puntos\n",
            "4) detergente ropa blanca: $20800 / 200 puntos\n",
            "5) queso azul: $6800 / 70 puntos\n",
            "6) arroz grano largo: $2140 / 22 puntos\n",
            "7) salsa de tomate: $3200 / 32 puntos\n",
            "8) palmitos rodajas: $1800 / 20 puntos\n",
            "9) bistec posta rosada: $4600 / 50 puntos\n",
            "> Canasta actual del usuario:\n",
            "\t1) harina sin polvos: $1500 / 20 puntos\n",
            "\t2) papas rusticas: $4000 / 100 puntos\n",
            "\t3) te en hoja: $3500 / 70 puntos\n",
            "\t4) detergente ropa blanca: $20800 / 400 puntos\n",
            "\t5) queso azul: $6800 / 140 puntos\n",
            "\t6) arroz grano largo: $2140 / 44 puntos\n",
            "\t7) salsa de tomate: $3200 / 64 puntos\n",
            "\t8) palmitos rodajas: $1800 / 40 puntos\n",
            "\t9) bistec posta rosada: $4600 / 100 puntos\n",
            "> Usuario con suscripcion. Puntos: 978\n"
        ]

        mensaje_out_sin = [
            "> Usuario sin suscripcion. Puntos: 0\n",
            "> Items para elegir:\n",
            "1) harina sin polvos: $1500 / 10 puntos\n",
            "2) papas rusticas: $4000 / 50 puntos\n",
            "3) te en hoja: $3500 / 35 puntos\n",
            "4) detergente ropa blanca: $20800 / 200 puntos\n",
            "5) queso azul: $6800 / 70 puntos\n",
            "6) arroz grano largo: $2140 / 22 puntos\n",
            "7) salsa de tomate: $3200 / 32 puntos\n",
            "8) palmitos rodajas: $1800 / 20 puntos\n",
            "9) bistec posta rosada: $4600 / 50 puntos\n",
            "> Canasta actual del usuario:\n",
            "\t1) harina sin polvos: $1500 / 10 puntos\n",
            "\t2) papas rusticas: $4000 / 50 puntos\n",
            "\t3) te en hoja: $3500 / 35 puntos\n",
            "\t4) detergente ropa blanca: $20800 / 200 puntos\n",
            "\t5) queso azul: $6800 / 70 puntos\n",
            "\t6) arroz grano largo: $2140 / 22 puntos\n",
            "\t7) salsa de tomate: $3200 / 32 puntos\n",
            "\t8) palmitos rodajas: $1800 / 20 puntos\n",
            "\t9) bistec posta rosada: $4600 / 50 puntos\n",
            "> Usuario sin suscripcion. Puntos: 489\n"
        ]
        self.assertTrue(stdout == "".join(mensaje_out_sin) or stdout == "".join(mensaje_out_con))

if __name__ == '__main__':
    unittest.main(verbosity=2,buffer=True)