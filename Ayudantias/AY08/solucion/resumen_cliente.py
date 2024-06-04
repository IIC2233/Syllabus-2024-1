#Aquí se ve un cliente funcional, se le agrega un input() para
#que uno puedo elegir el mensaje a enviar :)



import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname() 

sock.connect((host, port))

print("Entrega el mensaje que quieres enviar al servidor")
mensaje = input()
mensaje_bytes = mensaje.encode('utf-8') 
sock.sendall(mensaje_bytes)

data = sock.recv(4096) 
print(data.decode("utf-8")) 

sock.close()