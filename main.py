import discord
from discord.ext import commands
from discord.flags import Intents
import asyncio



Intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=Intents)


EPIC_LOG = 25
SUPER_LOG = 10 * EPIC_LOG
MEGA_LOG = 10 * SUPER_LOG
HYPER_LOG = 10 * MEGA_LOG
ULTRA_LOG = 10 * HYPER_LOG
GOLDEN_FISH = 15 
EPIC_FISH = 100 * GOLDEN_FISH
BANANA = 15
APPLE = 3

# Verificar se o bot está online
@client.event
async def on_ready():
    print('Bot está online')

@client.event
async def on_message(message):
    # Verificar se o canal é o certo
    id = message.channel.id
    if id == 1084991826156601404:
        # O bot não responde a si mesmo
        if message.author == client.user:
            return    
        # Comando para 
        if message.content.startswith("!log"):
            await message.channel.send('Selecione o tipo de tora que deseja!')
            await message.channel.send('```\nepic\nsuper\nmega\nhyper\nultra```')
            tora_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
            if tora_response.content.lower() == "epic":
                await message.channel.send('Informe a quantidade de toras que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * EPIC_LOG
            elif tora_response.content.lower() == "super":
                await message.channel.send('Informe a quantidade de toras que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * SUPER_LOG
            elif tora_response.content.lower() == "mega":
                await message.channel.send('Informe a quantidade de toras que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * MEGA_LOG
            elif tora_response.content.lower() == "hyper":
                await message.channel.send('Informe a quantidade de toras que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * HYPER_LOG
            elif tora_response.content.lower() == "ultra":
                await message.channel.send('Informe a quantidade de toras que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * ULTRA_LOG
            else:
                await message.channel.send("Tora inválida. Por favor, selecione uma das opções válidas.")
                quantidade_necessaria = 0

            quantidade_necessaria_str = "{:,}".format(quantidade_necessaria)
            if quantidade_necessaria > 0:
                await message.channel.send(f"Para produzir {quantidade_response.content} toras do tipo {tora_response.content}, são necessários {quantidade_necessaria_str} unidades de madeira.")
        if message.content.startswith("!foods"):
            await message.channel.send('Selecione o tipo de receita!')
            await message.channel.send('```\ngolden fish\nepic fish\nbanana\napple\n```')
            food_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
            if food_response.content.lower() == "golden fish":
                await message.channel.send('Informe a quantidade que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * GOLDEN_FISH
            elif food_response.content.lower() == "epic fish":
                await message.channel.send('Informe a quantidade que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * EPIC_FISH
            elif food_response.content.lower() == "banana":
                await message.channel.send('Informe a quantidade que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * BANANA
            elif food_response.content.lower() == "apple":
                await message.channel.send('Informe a quantidade que deseja fazer: ')
                quantidade_response = await client.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel)
                quantidade_necessaria = int(quantidade_response.content) * APPLE
            else:
                await message.channel.send("Receita inválida. Por favor, selecione uma das opções válidas.")
                quantidade_necessaria = 0

            quantidade_necessaria_str = "{:,}".format(quantidade_necessaria)
            if quantidade_necessaria > 0:
                await message.channel.send(f"Para produzir {quantidade_response.content} {food_response.content}, são necessários {quantidade_necessaria_str} unidades de fish/apple/madeira.")
            elif quantidade_necessaria == 0:
                await message.channel.send("Por favor, selecione uma das opções válidas.")
    # Caso não seja o canal certo        
    else:
        if message.content.lower() == "!log":
            # O bot não responde a si mesmo
            if message.author == client.user:
                return
            # Diz que não pode enviar a mensagem
            await message.channel.send('Esse comando não pode ser usado aqui')

client.run('MTA4NTk1OTE2MTAyOTg2NTUwMg.GqUcSF.0fvBT9bZ1QOTLT6Smcfetu0a1aEYDur2IrFG5M')