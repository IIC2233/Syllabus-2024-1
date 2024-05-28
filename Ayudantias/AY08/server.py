import socket
import threading
import json
import time
import random


class Servidor:

    def __init__(self, port, host):
        self.max_recv = 2**16
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        #COMPLETAR


    def bind_listen(self):
        
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(250)
        print(f'Servidor escuchando en {self.host} : {self.port}')
        
    def accept_connections(self):
        thread = threading.Thread(
            target=self.accept_connections_thread)
        thread.start()
        
    def accept_connections_thread(self):
        #COMPLETAR
        
    def listen_client_thread(self, client_socket):
        #COMPLETAR

    def chat_management(self, msg):
        msg_to_send = {"type": msg["type"],
                       "username": msg["username"],
                       "data": msg["data"]}
        for skt in self.sockets.keys():
            self.send(msg_to_send, skt)

    def send(self, value, sock):
        str_value = str(value)
        msg_bytes = str_value.encode()
        sock.send(msg_bytes)


if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    server = Servidor(port, host)
