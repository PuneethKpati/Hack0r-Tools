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

async def test():
	channel = bot.get_channel(734645148394192897)
	for i in range(100):
		print(i)
		time.sleep(i)
	
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
	
	# call the server set up on a new process
	# server will automatically start listening and send responses on discord
	
	print('Listening has started on new process')
	return

@bot.command()
async def listen(ctx, host, port):
	# exception handling for host and port user input

	# create the listener object with input and bot
	listener = Listener(host, int(port), bot)
	# call the server set up on a new process
	# server will automatically start listening and send responses on discord
	new_loop = asyncio.new_event_loop()
	listener_process = multiprocessing.Process(target=listener.setup, args=( new_loop,))
	listener_process.start()
	print('Listening has started on new process')
	return



bot.run(token)
