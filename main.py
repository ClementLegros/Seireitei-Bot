#Importation des librairies
import discord #Discord
import os #Variable secret
import time
from keep_alive import keep_alive
from function import *

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event

async def on_message(message):
  if message.author == client.user:
    return

  #Minecraft
  if message.content.startswith('!minecraft'):
    await message.channel.send('lesloulous.mine.fun')
  
  #Rocket League

  if message.content.startswith('!tournament'):
    await message.channel.send(get_Tournament())

  if message.content.startswith('!mode de jeux'):
    await message.channel.send(get_mode_de_jeux())

  if message.content.startswith('!car'):
    await message.channel.send(get_car())

  if message.content.startswith('!mutateurBasic'):
    await message.channel.send(get_Mutateur())

  if message.content.startswith('!mutateurComplet'):
    await message.channel.send(get_Mutateur_Complet())

  if message.content.startswith('!equipe'):
    await message.channel.send(get_Equipe())

  if message.content.startswith('!game'):    
    await message.channel.send(get_Game())

  #API

  if message.content.startswith('!quote'):
    quote = get_quote()
    await message.channel.send("Quote : "  + quote['quote'] +" Par : " + quote['character'] + " Dans l'anime : " + quote['anime'])

  if message.content.startswith('!joke'):
    jokeJson = get_joke()
    await message.channel.send(jokeJson['joke'], tts = True)
    time.sleep(5)
    await message.channel.send(jokeJson['answer'], tts = True)

  #HELP
  if message.content.startswith('!help'):
    await message.channel.send('COMMANDE ROCKET LEAGUE: !car, !mode de jeux')
    


TOKEN = os.environ['token']

keep_alive()
client.run(TOKEN)

