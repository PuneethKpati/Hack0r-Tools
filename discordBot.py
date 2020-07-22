import discord
from discord.ext import commands
from base_converter.base import BaseConverter
from server_listener.server_listener import Listener
import asyncio
import socket
import multiprocessing
import concurrent.futures
import time

# retrive the token stored in the same directory
token = open('token', 'r').read().strip()
bot = commands.Bot(command_prefix='&')


# Signifies if the bot is ready 
@bot.event
async def on_ready():
	print('Hack0r is ready...')



# Command takes in message and encodes it through BaseConverter.encode
# Prints the encoded messages in the same chat 
@bot.command()
async def encode(ctx, message=None):
	# If no message is provided to be encoded then provide usage details
	if not message:
		await ctx.send('Fam, what do you want me to encode?')
		await ctx.send('```\nUsage: &encode [message]```')
		return 

	# Call the encoding scripts
	encoder = BaseConverter()
	encoded = encoder.encode(message)

	# For each encoded base message print it in indented code blocks
	for item in encoded:
		res = '```\n{}\n```'.format(item)
		print(res)
		await ctx.send(res)

	return

# Command takes in message and decodes it through BaseConverter.decode
# Prints the decoded messages in the same chat
@bot.command()
async def decode(ctx, message=None):
	# If no message is provided to be decoded then provide usage details
	if not message:
		await ctx.send('I can only decode what you give me...')
		await ctx.send('```\nUsage: &decode [message]```')
		return

	# Call the decoding scripts
	decoder = BaseConverter()
	decoded = decoder.decode(message)
	# Print the decoded message in the same given chat
	await ctx.send('```\n{}\n```'.format(decoded))

	return

@bot.command()
async def test(ctx):
	bot.dispatch("server_message", 'm')
	return
	
@bot.command()
async def nc(ctx, host, port):
	# exception handling for host and port user input

	# create the listener object with input and bot
	listener = Listener(host, int(port), bot)
	message = listener.oneRun()

	m = """```
	{}
	```""".format(message)
	await ctx.send(m)

	return

#===========================================================================================

@bot.command()
async def listen(ctx, host, port):
	# exception handling for host and port user input
	
	# create the listener object with input and bot
	# listener = Listener(host, int(port), bot)
	# # call the server set up on a new process
	# # server will automatically start listening and send responses on discord
	# new_loop = asyncio.new_event_loop()
	# listener_process = multiprocessing.Process(target=listener.setup, args=( new_loop,))
	# listener_process.start()
	# print('Listening has started on new process')
	return
#==============================================================================================
def server_listen(listener):
	clientsocket, addr = listener.accept()
	m = clientsocket.recv(2048)
	message = str(m, 'utf-8')
	print(message)
	bot.dispatch("server_message", message)

@bot.command()
async def listen2(ctx):
	bot.dispatch("server_message", 'm')
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listener.bind(('127.0.0.1', 12005))
	listener.listen(5)
	while True:
		clientsocket, addr = await listener.accept()
		m = clientsocket.recv(2048)
		message = str(m, 'utf-8')
		print(message)
		
	# listener_process = multiprocessing.Process(target=server_listen)
	# listener_process.start()
	return

#===============================================================================================

@bot.event
async def on_server_message(message):
	print('hjello')
	channel = bot.get_channel(734645148394192897)
	await channel.send(message)



bot.run(token)
 