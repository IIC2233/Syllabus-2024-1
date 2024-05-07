import sys
from PyQt6.QtWidgets import QApplication
from frontend_DCCastillo.ventana_principal import Castillo
from frontend_DCCastillo.ventana_secundaria import Secundaria
from backend_DCCastillo.logica import Logica

if __name__ == '__main__':
    app = QApplication([])

    logica = Logica()
    ventana_1 = Castillo()
    ventana_2 = Secundaria("Dormitorio", "20:57")
    ventana_3 = Secundaria("Baño", "20:57")
    ventana_1.show()

    ventana_1.senal_abrir_ventana.connect(ventana_2.abrir_ventana)
    ventana_1.senal_abrir_ventana.connect(ventana_3.abrir_ventana)
    ventana_2.senal_abrir_castillo.connect(ventana_1.abrir_nuevamente)
    ventana_3.senal_abrir_castillo.connect(ventana_1.abrir_nuevamente)
    ventana_2.senal_hora.connect(logica.revisar_hora)
    logica.senal_dormir.connect(ventana_2.dormir)

    sys.exit(app.exec())
