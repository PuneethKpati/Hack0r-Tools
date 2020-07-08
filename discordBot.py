
import discord
from discord.ext import commands

token = open('token', 'r').read().strip()
bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
	print('Hack0r is ready...')


bot.run(token)
