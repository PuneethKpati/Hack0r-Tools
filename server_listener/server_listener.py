import socket

class Listener:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.listener = None

	def setup(self):
		self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.listener.bind((self.host, self.port))
		self.listener.listen(5)

		return 'Server Active on {} and port {}'.format(self.host, self.port)

	def run(self):
		clientsocket, addr = self.listener.accept()
		m = clientsocket.recv(2048)
		message = str(m, 'utf-8')
		print( message )