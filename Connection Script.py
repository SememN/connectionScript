import discord
from discord.ext import commands
import time
import asyncio
"This sript was written by SememN (Vk: https://vk.com/rijiy_chelik, github: https://github.com/SememN)"
print("This sript was written by SememN (Vk: https://vk.com/rijiy_chelik, github: https://github.com/SememN)")

bot = commands.Bot(".", self_bot=True)
TOKEN = input("введи свой токен: ")
@bot.command()
async def connect(ctx, voiceChannelName):
    Guild = ctx.author.guild
    VoiceChannels = Guild.voice_channels
    for name in VoiceChannels:
        if name.name == voiceChannelName:
            if name.user_limit == len(name.members) or name.user_limit <= len(name.members):
                print("channel is full, reconnecting...")
                time.sleep(1)
                await ctx.send(".connect " + voiceChannelName)
                await connect(ctx, voiceChannelName)
            elif name.user_limit > len(name.members):
                print("connecting")
                await name.connect()
                print("connected")
                print("stopping script...")
                input("Можешь выключать этот скрипт, ты подключен к войс-чату)")
            elif name.user_limit == None:
                print("connecting")
                await name.connect()
                print("connected")
                print("stopping script...")
                input("Можешь выключать этот скрипт, ты подключен к войс-чату)")

bot.run(TOKEN, bot=False)