import token
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged on as', self.user)

    async def on_message(self, message):
        # Confere se a mensagem é de si mesmo
        if message.author == self.user:
            return
        #ping pong básico
        if message.content == 'ping':
            await message.channel.send('pong')
            return

    async def on_command(self, command):
        if command == 'ping':
            await command.send('pong')
            return


intents = discord.Intents.default()
intents.message_content = True # para ler o chat
# futuramente aprender a usar comando de barra
client = MyClient(command_prefix = ".", intents=intents)

# Token do bot
client.run(token.TOKEN)



'''
código antigo arquivado para referência
usa o método MyClient, que é mais simples, mas não tem suporte a comandos de barra
'''