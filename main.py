import discord
from discord.ext import commands
from discord import app_commands
DISCORD_TOKEN = 'MTI1MzAyMjExMzY3NDAzOTM2Nw.GyoajF.ni8MPd_nqKvSJ7XCDseec8bZnAhoXYTtLeJESo'
client = discord.Client(command_prefix='S', intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=671050960449044490))
    print("encendido")
@tree.command(
    name="test",
    description="My first application Command",
    guild=discord.Object(id=671050960449044490)
)
async def test(interaction):
    await interaction.response.send_message("probando")
client.run(DISCORD_TOKEN)
