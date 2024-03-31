import socket


class Server:
	def __init__(self, port=200):
		self.port = port
		self.host = input('input host address: ')
		self.sock = None

	def __init_server(self):
		while True:
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.bind((self.host, self.port))
				print(f"Server is listening on port {self.port}")
				sock.listen(1)
				return sock
			except IOError:
				print(f"Port {self.port} is already in use, trying the next one...")
				self.port += 1

	def main(self):
		self.sock = self.__init_server()
		while True:
			client_socket, address = self.sock.accept()
			print("Client accepted")
			print("Client address:", address[0])
			print("Client port:", address[1])
			while True:
				data = client_socket.recv(1024)
				if data.decode() == 'exit':
					break
				client_socket.send(data.upper())
			client_socket.close()


server = Server()
server.main()
