import discord

from discord.ext import commands

import os

import asyncio

description = "By: L4MEK"

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents, case_insensitive = True) #deixar em True permite o bot ler mensagens maiusculas ou não. command_prefix='/' escolhe qual caractere vai acionar o comando, exemplo: /comando, vc pode mudar

#teste

@bot.command()

async def cx(ctx):

  await ctx.send(f'Oi, {ctx.author}, estou vivo! :)') #o "CX" apos o async def é o comando escolhido

#info embed

@bot.command()

async def info(ctx): #info é o comando que ativa o embed title = titulo da msg. description = descrição 

	embed1 = discord.Embed(    title = f'Olá, {ctx.author}{os.linesep}Sou um bot em fase **Experimental**, para mais informações fale com @🇪🇬፝⃟♘𝕷𝖆𝖒𝖊𝖐✰᭄♞#0589',

    description = " ",

    colour = 6950317

	) #a cor do embed em decimal

	embed1.set_author(name= 'Informações',

	icon_url='<iframe src="https://giphy.com/embed/iUioRia66dyc3gF0lN" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/SportsManias-sports-world-cup-sportsmanias-iUioRia66dyc3gF0lN">via GIPHY</a></p>') #Link do gif ou foto para seu embed

	await ctx.send(embed = embed1,delete_after=10) #o 10 determina em quantos segundos a mensagem vai sumir

#fim

bot.run('MTEzNTE3Nzc0NDkzMDU5MDg1MQ.GTF3Kn.EfJ6RbIhz-HfLKewSpb_5V1Y8ZX6lZNK7Dc1jY')

#AJUDA

#AS "#" são comentarios para lhe ajudar, se o codigo der erro voce pode apagar elas e o que esta escrito nela

#{ctx.author} menciona o autor do comando

#para adicionar novos comandos basta você copiar um abaixo e modificar., não crie comandos com o mesmo nome

#@bot.command()

#async def ComandoQueAtivaOBot(ctx):

#  await ctx.send(f'Oi, {ctx.author}, COMANDO PERSONALIZADO') #Mensagem basica

#@bot.command()

#async def COMANDO_PERSONALIZADO(ctx): 

#	embed1 = discord.Embed(

#    title = f'Olá, {ctx.author}{os.linesep} MODIFIQUE AQUI',

#    description = " ",

#    colour = 6950317

#	)

#	embed1.set_author(name= 'Informações',

#	icon_url='https://pa1.narvii.com/6213/57dd83feacd8e68f3d78488b2273bce1d0d6852d_hq.gif')

#	await ctx.send(embed = embed1,delete_after=10)
