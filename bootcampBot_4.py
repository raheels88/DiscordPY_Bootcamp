import discord
import os
from yahoo_fin import stock_info as si
from replit import db

client = discord.Client()

@client.event
async def on_ready():
  print('Beep Boop Beep...{0.user}'.format(client) + ' is online')

#### MAKE YOUR BOT DO SOMETHING WHEN A USER REACTS TO A MESSAGE WITH AN EMOJI ###

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
    db[str(author)] = new_td 
    await message.channel.send('Note *' + new_td + '* stored!')  
  
  if msg.startswith('?todo'):
    todo = db[str(author)]  
    await message.channel.send('Here is your To Do list: *' + todo + '*') 

@client.event
async def on_raw_reaction_add(payload): #This event is called when a message has a reaction added (i.e. emoji). Takes payload (which is a RawReactionActionEvent) as argument
  message_id = payload.message_id #the message ID of the message the reaction was added to
  channel_id = payload.channel_id #the channel ID of the message the reaction was added to
  channel = client.get_channel(channel_id) #the channel in which the reaction was added. Since payload doesn't have a get_channel method, we have to do it this way
  user = payload.member #the user who reacted with the payload/emoji

  if isinstance(channel, discord.channel.DMChannel) == False: #make sure the channel we're in isn't a DM channel
    emoji = payload.emoji #assign variable 'emoji' to be the emoji a user has reacted with
    message = await channel.fetch_message(message_id) #again, since payload doesn't have a get_message method, we have to fetch it this way

    if emoji.name == "🔖": #this can be any emoji
      await user.send("**Bookmark Created:** " + message.jump_url) 

client.run(os.getenv('TOKEN'))