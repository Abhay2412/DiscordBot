#Module of Discord which we will use
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= ',')

@bot.event
async def on_ready():
    print('The bot is ready to go.')

@bot.event
async def on_member_join(member):
    print(f'{member} has joined in our server. Please use the commands to make your time in this server more productive')

@bot.event
async def on_member_leave(member):
    print(f'{member} sad to see you go. Come back soon')
    
bot.run('ODYyODI1ODA5NzQwMTY5Mjg2.YOd_Jw.SJv1aoKDFhmMCW-10yWiuEBdPtA')
