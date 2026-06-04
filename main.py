import discord
from discord import app_commands
import json

with open('dados.json') as f:
    token = json.load(f)['token']

intents = discord.Intents.default()
client = discord.Client(command_prefix = ".", intents=intents, status = discord.Status.idle, activity = discord.Game("ELBot em desenvolvimento"))

guild = discord.Object(id=1313924353926365237) #código do meu servidor para teste interno

class dependencias(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync(guild=guild) # None = global / guild = server específico
        print('\n -- Comandos sincronizados\n')

client = dependencias()


# evento onready
@client.event
async def on_ready():
    print(f'\nLogged on as {client.user}\n')


# comandos direto no chat
@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    if message.content == '.ping':
        await message.channel.send('pong')
        return


'''
@client.event
async def on_typing(channel, user, when):
    await channel.send('Alguém está digitando...')
    return
'''

# comandos de barra daqui pra baixo
@client.tree.command(name="ping", description="Responde com pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")
    return

@client.tree.command(name="abrido", description="Comando secreto dos enclavos")
async def abrido(interaction: discord.Interaction):
    await interaction.response.send_message("Idoso")
    return

@client.tree.command(name="teste", description="afbjkbjk", guild=guild) #único comando atualmente configurado para funcionar em servidor específico.
async def teste(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} teste')
    return

@client.tree.command(name="join", description="join em call")
async def join(interaction: discord.Interaction):
    if interaction.user.voice is None: #se o usuário não estiver em um canal
        await interaction.response.send_message("Você não está em um canal de voz.")
        return

    if interaction.guild.voice_client is not None: #se o bot já estiver em um canal
        await interaction.response.send_message("Já estou conectado a um canal de voz.")
        return

    await interaction.response.send_message("Conectado!")
    await interaction.user.voice.channel.connect()
    return

client.run(token)