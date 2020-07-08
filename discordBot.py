
import discord
from discord.ext import commands
from base_converter.base import BaseConverter

token = open('token', 'r').read().strip()
bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
	print('Hack0r is ready...')

@bot.command()
async def encode(ctx, message=None):
	if not message:
		await ctx.send('Fam, what do you want me to encode?')
		await ctx.send('```\nUsage: &encode message```')

	encoder = BaseConverter()
	encoded = encoder.encode(message)

	for item in encoded:
		res = '```\n{}\n```'.format(item)
		print(res)
		await ctx.send(res)

	return

@bot.command()
async def decode(ctx, message=None):
	if not message:
		await ctx.send('I can only decode what you give me...')
		await ctx.send('```\nUsage: &decode [message]```')
		return

	decoder = BaseConverter()
	decoded = decoder.decode(message)
	await ctx.send('```\n{}\n```'.format(decoded))

	return

bot.run(token)
