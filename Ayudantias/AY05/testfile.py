import sys
import os
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QHBoxLayout, QLineEdit)
# Usa este archivo para correr los ejemplos!

# Pega aquí la definición de las clases


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instanciar clases/Conectar señales

    sys.exit(app.exec())
