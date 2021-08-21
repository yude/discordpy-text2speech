#-*- coding: utf-8 -*-

import os
from os.path import join, dirname
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
import subprocess
import ffmpeg
from generator import WAV

# Import keys from .env or OS environment (e.g. Docker arguments)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("TOKEN")

client = commands.Bot(command_prefix='.')
voice_client = None
tc = ""

@client.event
async def on_ready():
    print('Successfully logged in as {} (ID: {})\n'.format(client.user.name, client.user.id))

@client.command()
async def speech(ctx): # .speech command for connecting to VC.
    print('Retrieving user\'s current VC.')
    vc = ctx.author.voice.channel
    global tc
    tc = ctx.channel.id
    print('Connecting to VC.')
    await vc.connect()

@client.command()
async def dare(ctx): # .dare command for disconnecting from VC.
    print('Disconnecting from VC.')
    await ctx.voice_client.disconnect()

@client.event
async def on_message(message): # Retrieving messages to speech
    global tc
    msgclient = message.guild.voice_client
    if message.content.startswith('.'): # Messages starting with . should be command, passing.
        pass
    else:
        if message.channel.id == tc:
            if message.guild.voice_client:
                print(message.content)
                WAV(message.content)
                source = discord.FFmpegPCMAudio("./data/output.wav")
                message.guild.voice_client.play(source)
            else:
                pass
        else:
            pass
    await client.process_commands(message)

client.run(TOKEN)