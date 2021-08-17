import discord					
import os						

client = discord.Client()		

@client.event					
async def on_ready():			
    print('Beep Boop Beep...{0.user}'.format(client) + ' is online')

#### MAKE YOUR BOT RESPOND TO A MESSAGE ###

@client.event
async def on_message(message):  #on_message event - everything in this function is executed for EVERY message received
  msg = message.content  #assign the variable msg to be the content of a message (a string)

  if message.author == client.user:  #if the author of the message is the bot itself...
    return  #...then do nothing

  if msg.startswith('$hello'):  #if the message (sent by anyone but the bot) starts with '$hello'...
    await message.channel.send('Hello!')  #...'await' suspends the function while the bot does something
                                          #message.channel.send('Hello!') tells the bot to send 'Hello!' in the same channel the orignal message was sent in.

client.run(os.getenv('TOKEN'))