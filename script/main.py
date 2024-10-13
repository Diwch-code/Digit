import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("bot on")

if __name__ == "__main__":
    bot.run("TOKEN")