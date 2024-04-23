from PyQt6.QtCore import QObject, pyqtSignal


class Logica(QObject):

    # Señal que provoca que la ventana del dormitorio se cierre
    senal_dormir = pyqtSignal()

    def __init__(self):
        super().__init__()

    def revisar_hora(self, hora):
        # COMPLETAR
        pass
