from PyQt6.QtWidgets import QApplication
import sys
from client import Cliente
from lobby import MainWindow

app = QApplication([])

PORT = 3245
HOST = 'localhost'
username = sys.argv[1]

cliente = Cliente(PORT, HOST, username)
window = MainWindow()

#COMPLETAR


cliente.send_init_info_to_chat()

#COMPLETAR



window.show()
sys.exit(app.exec_())