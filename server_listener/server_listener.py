import socket

class Listener:
	def __init__(self, host, port):
		self.host = host
		self.port = port


	def setup(self):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listener.bind((self.host, self.port))
		listener.listen(5)

		return 'Server Active on {} and port {}'.format(self.host, self.port)

	def run(self):
		clientsocket, addr = listener.accept()
		m = clientsocket.recv(2048)
		message = str(m, 'utf-8')
		return message