import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar


class VentanaPantalla(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self) -> None:
        self.posicion = (100, 100)
        self.porte = (640, 360)
        self.setGeometry(*self.posicion, *self.porte)
        self.setWindowTitle('Pantalla')

        self.generar_widgets()
        self.agregar_estilo()  # Descomenta esta sección
                               # para agregarle estilo a la tele.

    def generar_widgets(self) -> None:
        # Generamos y posicionamos los distintos widgets
        self.imagen = QLabel('', self)
        self.imagen.setGeometry(0, 0, *self.porte)

        self.canal = QLabel('Canal: #0', self)
        self.canal.move(20, 20)

        self.volumen = QLabel('Volumen: 0', self)
        self.volumen.move(20, self.porte[1] - 30)

        self.volumen_barra = QProgressBar(self, textVisible=False)
        self.volumen_barra.resize(100, 15)
        self.volumen_barra.move(120, self.porte[1] - 30)

    def agregar_estilo(self) -> None:
        # Agregamos un poco de estilo a los labels
        self.canal.setStyleSheet('''
            color: white;
            background: black;
        ''')
        self.volumen.setStyleSheet('''
            color: white;
            background: black;
        ''')

    def actualizar_volumen(self, nuevo_volumen: int) -> None:
        '''Actualizamos el texto del label que guarda el volumen.'''
        # TODO: COMPLETAR
        self.volumen.setText(f'Volumen: {nuevo_volumen}')
        self.volumen.resize(self.volumen.sizeHint())

        # Actualizamos el valor de la barra del volumen.
        self.volumen_barra.setValue(nuevo_volumen)

    def actualizar_canal(self, nuevo_canal: int) -> None:
        '''Actualizamos el texto del label que guarda el canal actual.'''
        # TODO: COMPLETAR
        self.canal.setText(f'Canal: #{nuevo_canal}')
        self.canal.resize(self.canal.sizeHint())

        '''Cargamos, rescalamos y cambiamos la imagen del canal.'''
        # TODO: COMPLETAR
        # Paso 1: Conseguir el PATH
        path = os.path.join("frontend", "assets", f"{nuevo_canal}.png")
        
        # Paso 2: Crear un objeto tipo imagen (QPixmap)
        pixmap = QPixmap(path)
        
        # Paso 3: Ajustar el tamaño de la imagen al tamaño de la ventana
        pixmap = pixmap.scaled(self.porte[0], self.porte[1],
                               Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        # Lo de arriba es lo mismo que lo de abajo
        # pixmap = pixmap.scaled(*self.porte)
        
        # Paso 4: Llenar mi QLabel con la imagen correspondiente
        self.imagen.setPixmap(pixmap)

    def prender_apagar(self, encendido: bool) -> None:
        if encendido:
            self.show()
        else:
            self.hide()


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = VentanaPantalla()
    ventana.show()
    sys.exit(app.exec())
