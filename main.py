import discord
from discord import app_commands
import token

intents = discord.Intents.default()
intents.message_content = True # Permissao para ler o chat
intents.members = True # Permissao para ler os membros do servidor
client = discord.Client(command_prefix = ".", intents=intents, status = discord.Status.idle, activity = discord.Game("ELBot em desenvolvimento"))


guild = discord.Object(id=1362952956684668988) #código do meu servidor para teste interno

class dependencias(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync(guild=guild) # None = global / guild = server específico
        print('\n Comandos sincronizados\n')

client = dependencias()


# evento onready
@client.event
async def on_ready():
    if intents.message_content == True:
        print("Permissão para ler o chat")
    if intents.members == True:
        print("Permissão para ler membros")
    print(f'\nLogged on as {client.user}\n')


# comandos direto no chat
@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    if message.content == '.ping':
        await message.channel.send('pong')
        return


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


client.run(token.TOKEN)