import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.1.1", 5000))
server.listen(1)

print("Servidor esperando conexion...")

conn, addr = server.accept()
print("Cliente conectado:", addr)

conn.sendall(b"Hola Mauricio Lopez")
conn.close()
