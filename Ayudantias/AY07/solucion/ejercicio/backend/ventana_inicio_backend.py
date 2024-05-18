import os
import sys

from PyQt6.QtCore import pyqtSignal, QObject, QUrl
from PyQt6.QtWidgets import QApplication
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect


class VentanaInicioBackend(QObject):
    # DEBES MODIFICAR ESTA CLASE

    senal_mensaje_error = pyqtSignal()
    senal_empezar_juego = pyqtSignal(str)

    def __init__(self, ruta_cancion):
        # NO MODIFICAR ESTE MÉTODO
        super().__init__()
        self.musica = Musica(ruta_cancion)
        self.start()
    
    def verificar_usuario(self, usuario):
        # DEBES MODIFICAR ESTE METODO
        if len(usuario) > 0 and "," not in usuario:
            self.senal_empezar_juego.emit(usuario)
        else:
            self.senal_mensaje_error.emit()

    def start(self):
        # NO MODIFICAR ESTE MÉTODO
        self.musica.comenzar()


class Musica(QObject):
    # NO MODIFICAR ESTA CLASE

    def __init__(self, ruta_cancion):
        super().__init__()
        self.ruta_cancion = ruta_cancion
        self.media_player_wav = QSoundEffect(self)
        file_url = QUrl.fromLocalFile(self.ruta_cancion)
        self.media_player_wav.setSource(file_url)
        self.media_player_wav.setVolume(0.3)  # Opcional

    def comenzar(self):
        try:
            self.media_player_wav.play()
        except Exception as error:
            print('No se pudo iniciar la canción', error)