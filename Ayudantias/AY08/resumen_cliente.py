#Importamos la librería socket
import socket 

#Generamos el objeto
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Ponemos una TUPLA con (ip, puerto) 

host = socket.gethostname() #En este caso especificamos que la ip será la nuestra
port = 8726

sock.connect((host, port))

#Si quiero que se entreguen todos, ocupo en vez de send, sendall
print("Entrega el mensaje que quieres enviar al servidor")
mensaje = input()
mensaje_bytes = mensaje.encode('utf-8') #pasamos todo a bytes
sock.sendall(mensaje_bytes)

data = sock.recv(4096) #Recibimos 4096 bytes de respuesta (si sobran no importa)
print(data.decode("utf-8")) #Veamos que nos responden

#Cerramos la conexión SIEMPRE CIERREN SUS CONEXIONES, sino se ocupan recursos en su computador :(
sock.close()