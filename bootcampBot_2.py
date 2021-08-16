import discord
import os
from yahoo_fin import stock_info as si		#import yahoo_fin Python package - used to scrape stock price data from Yahoo Finance

client = discord.Client()

@client.event
async def on_ready():
  print('Beep Boop Beep...{0.user}'.format(client) + ' is online')

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    return

  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  if msg.startswith('!price'):					#if the message (sent by anyone but the bot) starts with '$price'...
    ticker = msg[7:]							#assign the variable 'ticker' to be the contents of the message from the 7th character onwards
    price = round(si.get_live_price(ticker),2)	#get_live_price is a method in the yahoo_fin package - this line gets the live price and rounds to 2 decimal places, and assigns the value to 'price'
    await message.channel.send('Price of ' + ticker + ' is $' + str(price))		#Concatenate ticker and price variables with a + sign

client.run(os.getenv('TOKEN'))