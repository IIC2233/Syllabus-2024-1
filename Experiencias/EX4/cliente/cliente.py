import socket
import sys
import os
import string
import pickle


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


class Cliente:
    """
        Clase que representa un cliente del distribuidor de archivos.
        En cuanto se instancia trata de conectarse al servidor y 
        posee métodos para comunicarse con este.
    """

    def __init__(self, port: int, host: str) -> None:
        """
            Inicializador de la clase y entabla conexión con el servidor.
        """
        self.conectado = False # Parte desconectado
        self.port = port
        self.host = host
        self.chunk_size = 2**16
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Vamos a tratar de conectarnos. Si funciona, activamos el menú
        # para interactuar. En caso de error, terminamos el programa.
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
        except ConnectionError:
            print("Conexion terminada")
            self.socket_cliente.close()
            self.conectado = False
            exit()
        self.menu()

    def menu(self) -> None:
        """
            Interfaz con la que puede interactuar el usuario.
        """
        opciones = {
            "1": self.pedir_lista_archivos,
            "2": self.descargar_archivo,
            "3": self.salir,
        }
        while self.conectado:
            opcion = input(
"""
    ¿Qué deseas hacer?
    [1]Pedir lista de archivos
    [2]Descargar Archivo
    [3]Salir
"""
            )
            if opcion in opciones:
                opciones[opcion]()
            else:
                print(f"{opcion} no es una opcion válida")

    def recibir_bytes(self, cantidad: int) -> bytearray:
        """
            Recibe N cantidad de bytes, los concatena y retorna como un 
            único bytearray.
        """
        bytes_leidos = bytearray()
        while len(bytes_leidos) < cantidad:
            cantidad_restante = cantidad - len(bytes_leidos)
            bytes_leer = min(self.chunk_size, cantidad_restante)
            # Importante recv(N) va a leer hasta N bytes que le manden. Si le mandan
            # menos, por ejemplo, K (con K < N) entonces respuesta será de largo K
            respuesta = self.socket_cliente.recv(bytes_leer)
            bytes_leidos += respuesta
        return bytes_leidos

    def recibir_mensaje(self) -> any:
        """
            Lee cuantos bytes vendrán y luego carga un mensaje a partir
            de un bytearray
        """
        largo = int.from_bytes(self.recibir_bytes(4), "big")
        return pickle.loads(self.recibir_bytes(largo))

    def pedir_lista_archivos(self) -> None:
        """
            Le pide al servidor la lista de archivos presentes y los imprime.
        """
        mensaje = Mensaje(operacion="listar")
        self.enviar_mensaje(mensaje)
        respuesta = self.recibir_mensaje()
        print("Los archivos disponibles para descarga son:")
        for archivo in respuesta.data:
            print(f"- {archivo}")

    def descargar_archivo(self) -> None:
        """
            Pide el nombre del archivo, y solicita al servidor que se envíe.
            En caso de recibirlo, activa el método correspondiente.
        """
        archivo = input("Ingrese el nombre del archivo que quieres descargar: ")
        mensaje = Mensaje(operacion="descargar", data=archivo)
        self.enviar_mensaje(mensaje)
        respuesta = self.recibir_mensaje()
        if respuesta.estado == "ok":
            self.guardar_archivo(archivo, respuesta.data)
            print("Archivo descargado")
        elif respuesta.estado == "error":
            print(">> Error al intentar descargar el archivo")

    def enviar_mensaje(self, mensaje: Mensaje) -> None:
        """
            Serializar un mensaje y enviarlo al servidor siguiendo 
            el formato necesario.
        """
        bytes_mensaje = pickle.dumps(mensaje)
        self.socket_cliente.sendall(len(bytes_mensaje).to_bytes(4, "big"))
        self.socket_cliente.sendall(bytes_mensaje)

    def guardar_archivo(
            self,
            nombre_archivo: string,
            archivo: bytearray,
        ) -> None:
        """
            Almacena los bytes en un archivo local del computador bajo
            el nombre pedido.
        """
        # Crear carpeta si es que no existe
        os.makedirs("descargas", exist_ok=True)

        # Guardar archivo
        with open(os.path.join("descargas", nombre_archivo), "wb") as file:
            file.write(archivo)

    def salir(self) -> None:
        """
            Cierra la conexión con el servidor.
        """
        self.socket_cliente.close()
        self.conectado = False


if __name__ == "__main__":
    # Recibimos el puerto y host por consola,
    # pero si no se entregan damos argumentos por defecto
    PORT = 3247 if len(sys.argv) < 2 else int(sys.argv[1])
    HOST = "localhost" if len(sys.argv) < 3 else sys.argv[2]
    client = Cliente(PORT, HOST)
