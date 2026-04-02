import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load your secret keys from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with "intents" (permissions)
intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Ready to climb! What champion are we checking?')

bot.run(TOKEN)
print("hi joby")