import discord
import os
from yahoo_fin import stock_info as si
from replit import db  #import the database package

client = discord.Client()

@client.event
async def on_ready():
  print('Beep Boop Beep...{0.user}'.format(client) + ' is online')

#### MAKE YOUR BOT STORE A TO-DO LIST IN A DATABASE ###

@client.event
async def on_message(message):
  msg = message.content
  author = message.author
  if author == client.user:
    return

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  if msg.startswith('!price'):
    ticker = msg[7:]
    price = round(si.get_live_price(ticker),2)
    await message.channel.send('Price of ' + ticker + ' is $' + str(price))

  if msg.startswith('!todo'):
    new_td=msg[6:]
    db[str(author)] = new_td  #in the database, create an entry with the key set as the message author (must be a string) and the associated value as new_td
    await message.channel.send('Note *' + new_td + '* stored!')  #send a message telling message author that that the note has been stored
  
  if msg.startswith('?todo'):
    todo = db[str(author)]  #retrieve the database value for the message author
    await message.channel.send('Here is your To Do list: *' + todo + '*')  #send a message with the database entry for that author

client.run(os.getenv('TOKEN'))