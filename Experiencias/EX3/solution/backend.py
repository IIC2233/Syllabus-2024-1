from PyQt6.QtCore import QObject, QTimer, pyqtSignal, QMutex, QThread
from random import randint
import time
import parametros as p


class Meteorito(QThread):
    identificador = 0

    def __init__(self, x: int, y: int, mutex: QMutex,
                 senal_fin_meteorito: pyqtSignal,
                 senal_mover: pyqtSignal) -> None:
        super().__init__()

        self.id = Meteorito.identificador
        Meteorito.identificador += 1
        self.mutex = mutex
        self.x = x
        self.y = y
        self.senal_mover = senal_mover
        self.senal_fin_meteorito = senal_fin_meteorito
        self._destruido = False
        self._distancia_a_recorrer = randint(
            p.DISTANCIA_MINIMA, p.DISTANCIA_MAXIMA)

    def run(self) -> None:
        """
        Método encargado de mover constantemente el meteorito hacia abajo.
        Si llega a una posición indicada en "p.POSICION_Y", entonces llegó
        a la ciudad y hay que notificar que debe ser destruido junto con
        reducir la población de la ciudad.
        Solo 1 meteorito a la vez puede chocar con la ciudad.

        En este método hay 1 error 😱.
        """
        print(f"[Back] Soy meteorito {self.id} y comienzo mi caída")
        while not self.destruido:
            time.sleep(p.TIEMPO_CAIDA_METEORO)
            self.y += self._distancia_a_recorrer
            self.senal_mover.emit(self.id, self.x, self.y)
            if self.y >= p.POSICION_Y:
                # Desaparecer haciendo daño
                self._destruido = True

                # Solo 1 meteoro notifica que debe hacer daño al mismo tiempo
                self.mutex.lock()
                self.senal_fin_meteorito.emit(self.id, True)

                # Ronda 4.4
                # ERROR 😱: no se libera el lock compartido entre meteoritos
                # Actual ❌: No había nada
                # Solución : self.mutex.unlock()
                self.mutex.unlock()

    @property
    def destruido(self) -> bool:
        return self._destruido

    @destruido.setter
    def destruido(self, destruido: bool) -> None:
        """
        Setter encargado de notificar cuando es necesario
        eliminar el meteorito
        """
        if destruido is True:
            self._destruido = destruido

            # Desaparecer sin hacer daño
            self.senal_fin_meteorito.emit(self.id, False)

    @property
    def centro_x(self) -> int:
        return self.x + 15

    @property
    def centro_y(self) -> int:
        return self.y + 192


class Ciudad:
    def __init__(self, nombre: str, senal_actualizar_poblacion: pyqtSignal) -> None:
        self.nombre = nombre
        self._poblacion = p.POBLACION_MAXIMA
        self.senal_actualizar_poblacion = senal_actualizar_poblacion

    @property
    def poblacion(self) -> int:
        return self._poblacion

    @poblacion.setter
    def poblacion(self, nueva_poblacion: int) -> None:
        """
        Setter encargado de notificar al frontend cuando debe
        cambiar el texto a mostrar sobre la población
        """
        self._poblacion = nueva_poblacion
        if self.poblacion <= 0:
            self.senal_actualizar_poblacion.emit(
                f'{self.nombre} ha perdido todos sus ciudadanos')
        else:
            self.senal_actualizar_poblacion.emit(
                f'{self.nombre} tiene {self.poblacion} ciudadanos')


class Juego(QObject):
    """
    La clase tiene 1 error 😱.
    """
    # RONDA 1.2
    # ERROR 😱: Juego no hereda de QObject así que tiene conflictos
    #           con crear y pasar una señal
    # Actual ❌: class Juego
    # Solución : class Juego(QObject)
    senal_empezar_juego = pyqtSignal()
    senal_mover_meteorito = pyqtSignal(int, int, int)
    senal_aparecer_meteorito = pyqtSignal(int, int, int)
    senal_remover_meteorito = pyqtSignal(int)
    senal_fin_meteorito = pyqtSignal(int, bool)
    senal_actualizar_poblacion = pyqtSignal(str)

    def __init__(self) -> None:
        """
        En este método hay 1 error 😱.
        """
        super().__init__()

        self.ciudad = Ciudad("DCCity", self.senal_actualizar_poblacion)
        self.meteoritos = []

        self.mutex = QMutex()
        self.timer_meteoritos = QTimer(self)
        self.timer_meteoritos.timeout.connect(self.caer_meteorito)

        # Ronda 4.3
        # ERROR 😱: el timer generador de meteoritos es singleton
        # Actual ❌: self.timer_meteoritos.setSingleShot(True)
        # Solución : eliminar o hacer self.timer_meteoritos.setSingleShot(False)
        self.timer_meteoritos.setSingleShot(False)

        self.senal_fin_meteorito.connect(self.fin_meteorito)

    def seleccionar_dificultad(self, dificultad: str) -> None:
        """
        Método encargado de definir el tiempo de creación de cada meteorito
        según la dificultad elegida, inicializar el QTimer y finalmente
        avisar al frontend que empieza el juego
        """
        print(f"[BACK] Dificultad recibida: {dificultad}")
        self.timer_meteoritos.setInterval(p.DIFICULTAD[dificultad])
        self.senal_empezar_juego.emit()
        self.timer_meteoritos.start()

    def caer_meteorito(self) -> None:
        """
        Método encargado de crear la lógica de un meteorito y notificar al
        frontend que debe aparecer un nuevo meteorito.
        Luego empiece su ejecución y guarda el meteorito en memoria.

        En este método hay 2 errores 😱.
        """

        meteorito = Meteorito(
            x=randint(50, p.ANCHO_JUEGO - 50),
            y=-p.ALTURA_METEORO,
            mutex=self.mutex,
            senal_fin_meteorito=self.senal_fin_meteorito,
            senal_mover=self.senal_mover_meteorito
        )
        print(f"[BACK] Creando nuevo meteorito con id={meteorito.id}")
        self.senal_aparecer_meteorito.emit(meteorito.id,
                                           meteorito.x, meteorito.y)
        # Ronda 3.3
        # ERROR 😱: el meteorito no empieza su movimiento
        # Actual ❌: No había nada
        # Solución : meteorito.start()
        meteorito.start()

        # Ronda 3.4
        # ERROR 😱: no estamos guardando el QThread en memoria
        # Actual ❌: No había nada
        # Solución : self.meteoritos.append(meteorito)
        self.meteoritos.append(meteorito)

    def fin_meteorito(self, id_meteorito: int, daño: bool) -> None:
        """
        Método encargado de gestionar el fin de un meteorito. Esto implica
        Avisar al frontend cuando hay que eliminar,
        reducir la población en caso que el meteorito haga daño
        y si no queda población, detener la caída de meteoritos

        En este método hay 1 error 😱.
        """
        print(f"[BACK] Meteorito {id_meteorito} será eliminado")

        # Ronda 4.2
        # Eliminar visualmente el meteorito
        # ERROR 😱: no estamos eliminando los meteoritos
        # Actual ❌: No había nada
        # Solución : self.senal_remover_meteorito.emit(id_meteorito)
        self.senal_remover_meteorito.emit(id_meteorito)

        if daño:  # Si hay daño, disminuir población
            self.ciudad.poblacion -= p.AFECTADOS

        # Si no quedan personas. Parar los meteoritos
        if self.ciudad.poblacion <= 0:
            self.timer_meteoritos.stop()

    def click_pantalla(self, x: int, y: int) -> None:
        """
        Método encargado de buscar el meteorito activo
        más cercano al click del mouse y si está dentro del radio esperado
        lo destruye.
        """
        print(f"[BACK] Presioné en {x},{y}")
        for meteorito in self.meteoritos:
            if not meteorito.destruido:  # Solo verificar meteoritos sin destruir
                if self.chequear_colision(x, y, meteorito):
                    # Si el click es válido, se destruye el meteorito
                    meteorito.destruido = True

                    # Dejo de buscar más meteoritos porque ya destruí uno.
                    return

    def chequear_colision(self, x: int, y: int, meteorito: Meteorito) -> bool:
        """
        Método encargado de revisar si la distancia euclidiana entre el centro
        del meteorito y la posición (X,Y) es menor a un radio determinado
        """
        distancia = ((x - meteorito.centro_x)**2 +
                     (y - meteorito.centro_y)**2)**(1/2)

        return distancia < p.DISTANCIA_IMPACTO
