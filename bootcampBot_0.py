import discord  #imports the discord.py library.
import os  #imports os library, used for fetching 'TOKEN' variable

client = discord.Client()  #create an instance of a Client, which is the connection to Discord

@client.event  #used to register any event - this line must precede any event you want your bot to register
async def on_ready():  #on_ready event - anything in this function is executed whenever the bot is online and ready
    print('Beep Boop Beep...{0.user}'.format(client) + ' is online')  #prints a message in terminal to say bot is online

client.run(os.getenv('TOKEN'))  #runs the bot with your unique login token - must be the final line. Login token NOT TO BE SHARED!!!