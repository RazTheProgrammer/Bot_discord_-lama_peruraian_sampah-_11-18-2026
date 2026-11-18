import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def trash(ctx, *, trash_name):
    if trash_name == "kantong plastik":
        await ctx.send("Terurai dalam waktu sekitar 10-20 tahun")
    if trash_name == "kaleng aluminium":
        await ctx.send("Terurai dalam waktu sekitar 80-200 tahun")
    if trash_name == "botol plastik":
            await ctx.send("Terurai dalam waktu sekitar 450 tahun")

bot.run("")
