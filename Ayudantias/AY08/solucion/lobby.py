import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType("DCChat.ui")

class MainWindow(window_name, base_class):

    send_msg_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.sendButton.clicked.connect(self.send_msg_to_client)
        self.displayWidget.setReadOnly(True)
        self.show()

    def salir(self, event):
        sys.exit()
 
    def send_msg_to_client(self):
        print(self.userInputWidget.toPlainText())
        data = {    
            "type": "chat", 
            "username": self.username, 
            "data": self.userInputWidget.toPlainText() 
        }
        self.send_msg_signal.emit(data)
        self.userInputWidget.setPlainText('')

    def get_username(self, event):
        self.username = event
        print('Username seted')

    def update_chat(self, event):
        self.displayWidget.setPlainText(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    sys.exit(app.exec())