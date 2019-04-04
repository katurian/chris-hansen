import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import requests
import json

client = Bot(description="NSFW filter by kat", command_prefix="!", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Made by Kate Kulinski')
	return await client.change_presence(game=discord.Game(name='Pixlab'))

@client.event
async def on_message(message):
	if (message.author.bot == True):
		return
	if message.content.startswith('http'):
		img = str(message.content)
		key = 'API-KEY'
		req = requests.get('https://api.pixlab.io/nsfw', params={'img': img, 'key': key})
		reply = req.json()
		if reply['status'] != 200:
			return
		elif reply['score'] < 0.5:
			return
		else:
			await client.delete_message(message)
			msg = 'Why don’t you take a seat? {0.author.mention}'.format(message)
			await client.send_message(message.channel, msg)
	else:
		return

client.run('BOT-TOKEN')
