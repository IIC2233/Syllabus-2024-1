import socket
import threading
import pickle
import sys
import os
from typing import List

class Mensaje:
    """
        Esta clase empaqueta los mensajes que serán enviados entre conexiones.
    """
    def __init__(self, operacion=None, data=None, estado=None) -> None:
        # Guarda el tipo de operación: listar o descargar
        self.operacion = operacion
        # Guarda la información necesaria según la consulta
        self.data = data
        # Guarda el resultado de la consulta "ok" o "error"
        self.estado = estado


class Servidor:
    """
        Clase que representa un servidor distribuidor de archivos.
        En cuanto se instancia levanta un socket para escuchar potenciales
        clientes.
    """
    id_clientes = 0

    def __init__(self, port: int, host: str) -> None:
        self.chunk_size = 2**16
        self.host = host
        self.port = port
        self.sockets = {}
        # 0. TODO: Instanciar un socket para que sea servidor y pueda escuchar conexiones

    def bind_listen(self) -> None:
        # 1.TODO: Debe enlazar el puerto y el host, y escuchar conexiones

        # Aquí hay 1 error. Además, el método está incompleto.
        self.socket_server.connect((self.host, self.port))

    def accept_connections(self) -> None:
        # 3. TODO: Debe inicializar el thread encargado de aceptar nuevas
        # conexiones

        # Este método tiene 2 errores.        
        thread = threading.Thread(target=self.accept_connections_thread, daemon=True)
        thread.start()

    def accept_connections_thread(self) -> None:
        # 4. TODO: A cada nueva conexión, le debe inicializar un hilo para escuchar a dicho
        # cliente. (¿Por qué esto no se puede hacer en la función de arriba solamente?)
        while True:
            socket_cliente, address = self.socket_server.accept()
            print(f"Nuevo cliente conectado:", socket_cliente, address)
            self.sockets[socket_cliente] = address
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread, args=(socket_cliente,), daemon=True
            )
            listening_client_thread.start()

    def recibir_bytes(self, socket_cliente: socket, cantidad: int) -> bytearray:
        # 5. TODO: Debe recibir <cantidad> bytes desde el <socket_cliente> y juntarlo
        # en un solo bytearray.
        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            # agregamos los bytes de a poco
            pass

    def listen_client_thread(self, socket_cliente: socket) -> None:
        # 6. TODO: Recibe los mensajes del socket, carga el mensaje y llama al método
        # manejar mensaje.
        while True:
            print(
                f"[{self.sockets[socket_cliente]}] Recibiendo largo del siguiente mensaje"
            )

            # Recibamos primero el largo del mensaje:
            largo_mensaje = None

            print(
                f"[{self.sockets[socket_cliente]}] Recibiendo mensaje de largo {largo_mensaje}"
            )

            # Ahora sabiendo el largo, recibamos el mensaje en sí:
            bytes_mensaje = None

            print(
                f"[{self.sockets[socket_cliente]}] Mensaje de largo {largo_mensaje} recibido"
            )

            # Con el mensaje recibido, intentemos deserializarlo
            # y entregarlo al método manejar_mensaje. Recuerda manejar errores.

    def manejar_mensaje(self, mensaje: Mensaje, socket_cliente: socket) -> None:
        # 7. TODO: Si la operacion del mensaje es listar, debe enviar
        # la lista de archivos. Si la operacion es descargar, debe
        # verificar que el archivo exista, y si existe entonces debe
        # enviarlo utilizando el método enviar_archivo
        print(mensaje.__dict__)

        # Al programar el flujo, toma en cuenta:
        # ¿De donde sacamos el comando enviado?
        # Si queremos descargar un archivo, ¿como el servidor sabrá cuál archivo enviar?
        # ¿Qué pasa si el servidor no tiene el archivo pedido?

    def enviar_mensaje(self, mensaje: Mensaje, socket_cliente: socket) -> None:
        # 8. TODO: Debe enviar el mensaje cumpliendo con las reglas antes mencionadas:
        # Primero enviar 4 bytes con el largo del mensaje, y luego el mensaje

        # Este método tiene 2 errores. ¡Son dificiles de encontrar!
        print(mensaje.__dict__)
        print(f"[{self.sockets[socket_cliente]}] Enviando {mensaje}")
        bytes_mensaje = pickle.dump(mensaje)
        largo_mensaje = len(bytes_mensaje).to_bytes(4, "big")
        mensaje_total = largo_mensaje + bytes_mensaje
        socket_cliente.sendall(mensaje_total)
        print(f"[{self.sockets[socket_cliente]}] {mensaje} enviado")

    def enviar_archivo(self, archivo: str, socket_cliente: socket) -> None:
        # 9. TODO: Debe enviar el archivo al socket
        pass

    def listar_archivos(self) -> List[str]:
        return os.listdir("archivos")


if __name__ == "__main__":
    # 2. TODO: El puerto y el host deben poder pasarse por consola,
    # y en caso de que no se reciban, tener por defecto un valor.

    # Aquí hay 1 error y 1 línea por completar.

    PORT = '3247' if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = None
    server = Servidor(PORT, HOST)

    input('Presione enter para cerrar')
    server.socket_server.close()
    exit(1)
