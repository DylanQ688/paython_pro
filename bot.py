import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def iniciar():

    print(f'Hola mi bot {bot.user} esta listo')

@bot.command()
async def hola(ctx):

    await ctx.send('hola que mas')






#Lo que esto hace es permitirte recargar las referencias cuando realizas un cambio en la extensión.
bot.reload_extension('reset')
#lo que hase la proxima cosa es que va ha decirnos que estan reiniciandose.
@bot.command()
async def setup(ctx):
    await ctx.send('I am being loaded!')
#hay differentes formas de haserlo como el teardown y el setup aunque la unica differencia es que el teardown las funciones son ignoradas y la extensión sigue descargada.
@bot.command()
async def teardown(ctx):
    await ctx.send('I am being unloaded!')
#hice algunos errores como fue el que no me acordaba de poner
token = ''

bot.run(token)