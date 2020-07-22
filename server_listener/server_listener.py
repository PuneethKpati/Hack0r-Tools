import socket
import multiprocessing
import time
import discord 
from discord.ext import commands
import asyncio


class Listener:
	def __init__(self, host, port, bot):
		self.host = host
		self.port = port
		self.bot  = bot

	def setup(self, loop):
		self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.listener.bind((self.host, self.port))
		self.listener.listen(5)

		
		print('Server Active on {} and port {}'.format(self.host, self.port))

		asyncio.set_event_loop(loop)
		loop.run_until_complete(self.run())

	async def run(self):
		while True:
			clientsocket, addr = await self.listener.accept()
			m = clientsocket.recv(2048)
			message = str(m, 'utf-8')
			self.bot.dispatch('server_message', message)


	def oneRun(self):
		self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.listener.bind((self.host, self.port))
		self.listener.listen(5)
		clientsocket, addr = self.listener.accept()
		m = clientsocket.recv(2048)
		message = str(m, 'utf-8')
		print(message)
		return message
