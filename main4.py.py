import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def adios(ctx, count_adios = 5):
    await ctx.send("adios_amigo" * count_adios)

@bot.command()
async def do_you_love_me(ctx, count_do_you_love_me = 5):
    await ctx.send("yes_i_do" * count_do_you_love_me)

bot.run("MTE1ODAxOTQ2MTM3MTEzNDA5Mw.Gq1E5b.sSe7Aa0JDMYTbgn34BFZ3BNLb7OstTsIlhIiRY")