import sys
from PyQt6.QtWidgets import QApplication

from backend.logica import ControladorLogico
from frontend.control_remoto import VentanaControlRemoto
from frontend.pantalla import VentanaPantalla


if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])

    # Instanciamos las clases
    controlador_logico = ControladorLogico()
    control_remoto = VentanaControlRemoto()
    pantalla = VentanaPantalla()

    '''Conectamos las señales

    [Control remoto] senal_volumen --------> [Controlador Lógico] cambiar_volumen 
    [Control remoto] senal_canal ----------> [Controlador Lógico] cambiar_canal 
    [Control remoto] senal_encendido ------> [Controlador Lógico] prender_apagar 
    
    [Controlador Lógico] senal_volumen ----> [Pantalla] actualizar_volumen 
    [Controlador Lógico] senal_canal ------> [Pantalla] actualizar_canal
    [Controlador Lógico] senal_encendido --> [Pantalla] prender_apagar
    [Controlador Lógico] senal_empezar ----> [Pantalla] show + [Control remoto] show
    '''
    # TODO: COMPLETAR

    # Empezamos la ejecución del programa
    controlador_logico.empezar()

    sys.exit(app.exec())
