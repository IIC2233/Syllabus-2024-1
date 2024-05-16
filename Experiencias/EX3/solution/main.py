from PyQt6.QtWidgets import QApplication
from frontend import VentanaInicio, VentanaJuego
import sys
from backend import Juego


class ProtegeDCCity:
    def __init__(self) -> None:
        """
        Instanciamos todas las ventanas y clases necesarias
        """
        self.frontend_inicio = VentanaInicio()
        self.frontend_juego = VentanaJuego()
        self.backend = Juego()

    def conectar(self) -> None:
        """
        Conectamos todas las señales entre ventanas y backend

        En este método hay 2 errores 😱.
        """
        # RONDA 2.3
        # ERROR 😱: Faltaba conectar "senal_seleccionar_dificultad"
        #           con el método seleccionar_dificultad del backend.
        # Actual ❌: no había nada
        # Solución : conectar la señal al método indicado.
        self.frontend_inicio.senal_seleccionar_dificultad.connect(
            self.backend.seleccionar_dificultad
        )

        # RONDA 1.3
        # Backend le avisa al frontend del juego que empieza el juego
        # ERROR 😱: Señal mal conectada. Faltaba el método .connect(...)
        # Actual ❌: self.backend.senal_empezar_juego(self.frontend_juego.empezar_juego)
        # Solución : usar .connect()
        self.backend.senal_empezar_juego.connect(self.frontend_juego.empezar_juego)

        # Frontend_juego notifica al backend cuando se hace click en pantalla
        self.frontend_juego.senal_click_pantalla.connect(self.backend.click_pantalla)

        # Backend notifica al frontend_juego cuando aparece, se mueve
        # y desaparece el meteorito
        self.backend.senal_aparecer_meteorito.connect(
            self.frontend_juego.aparecer_meteorito
        )
        self.backend.senal_mover_meteorito.connect(self.frontend_juego.mover_meteorito)
        self.backend.senal_remover_meteorito.connect(
            self.frontend_juego.remover_meteorito
        )

        # Backend notifica al frontend_juego cuando se cambia la población
        self.backend.senal_actualizar_poblacion.connect(
            self.frontend_juego.actualizar_poblacion
        )

    def iniciar(self) -> None:
        """
        Definimos qué sucede cuando empieza el juego. En este caso, que
        la ventana de inicio se muestre.

        En este método hay 1 error 😱.
        """
        # RONDA 1.4
        # ERROR 😱: show es un método no un atributo. Hay que ejecutarlo
        # Actual ❌: self.frontend_inicio.show
        # Solución : self.frontend_inicio.show()
        self.frontend_inicio.show()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    juego = ProtegeDCCity()
    juego.conectar()
    juego.iniciar()

    sys.exit(app.exec())
