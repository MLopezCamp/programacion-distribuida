import socket
import threading

def handle_client(conn, addr):
	print(f"cliente conetado desde {addr}")

	try:
		student_name = conn.recv(1024).decode()
		response = f"Hola {student_name}, estas conectado a un servidor concurrente"
		conn.sendall(response.encode())
	except Exeption as e:
		print(f"Error con {addr} : {e}")
	finally:
		conn.close()
		print(f"Conexion cerrada {addr}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Servidor esperando conexion...")

while True:
	conn, addr = server.accept()
	
	client_thread = threading.Thread(
		target=handle_client,
		args=(conn,addr)
	)
	client_thread.start()
