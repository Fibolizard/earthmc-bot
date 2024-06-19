import discord
from discord import app_commands
from discord.ext import commands
import requests

DISCORD_TOKEN = 'MTI1MzAyMjExMzY3NDAzOTM2Nw.GyoajF.ni8MPd_nqKvSJ7XCDseec8bZnAhoXYTtLeJESo'
client = commands.Bot(command_prefix='S', intents=discord.Intents.all())
#player_data = requests.get("https://api.earthmc.net/v2/aurora/residents/").json()
@client.event
async def on_ready():

    print("encendido")
@client.hybrid_group(fallback="get", description="Te permite saber cuando una ciudad caerá")
async def fall(ctx, town):

   # mayor = player_data[town]
   # mayor_last_online = player_data['mayor']['lastOnline']

    town_data = requests.get(f"https://api.earthmc.net/v2/aurora/towns/{town}").json()
    amount_residents = len(town_data['residents'])
  #  if residents == 1:
    embed = discord.Embed(title=f"¿Cuándo caerá {town}?",
                                 description=f"**Cantidad de residentes**: {amount_residents}",
                                colour=discord.Colour.brand_green())
    embed.add_field(name='Alcalde', value=f'test')
    await ctx.channel.send(embed=embed)


client.run(DISCORD_TOKEN)
