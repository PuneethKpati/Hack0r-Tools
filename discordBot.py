import discord
from discord.ext import commands
from base_converter.base import BaseConverter

import socket

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
async def listen(ctx, host, port):
	# exception handling for host and port user input
	if not str.isnumeric(port):
		await ctx.send('Not a Correct Port Number')

	# setup the socket configuration for an open TCP socket
	listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listener.bind((host, int(port)))
	listener.listen(5)
	
	# wait for a connection and then listen to the request sent
	await ctx.send('```\n I am Listening on the host {} at port {} ```'.format(host, port))
	clientsocket, addr = listener.accept()
	m = clientsocket.recv(2048)

	# decode the message from bytes to string
	message = str(m, 'utf-8')

	# send the message to a specified channel 
	channel = bot.get_channel(734645148394192897)
	await channel.send('```\nHi, Someone tried to talk to me\n\n'+message+'```')

	return



bot.run(token)
 