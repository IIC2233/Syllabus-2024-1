from PyQt6.QtCore import QObject, pyqtSignal


class Logica(QObject):

    senal_dormir = pyqtSignal()

    def __init__(self):
        super().__init__()

    def revisar_hora(self, hora):
        separado = hora.split(":")
        if (int(separado[0]) >= 20) or (int(separado[0]) <= 5 and int(separado[0]) >= 0):
            self.senal_dormir.emit()
