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

# Conexión de señales y slots
cliente.send_username.connect(window.get_username)
cliente.update_lobby_chat.connect(window.update_chat)

window.send_msg_signal.connect(cliente.receive_msg_from_lobby)

#COMPLETAR
cliente.send_init_info_to_chat()

window.show()
sys.exit(app.exec())