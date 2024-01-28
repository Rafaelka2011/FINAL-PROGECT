import discord
from discord.ext import commands
import os, random
import requests

from model import get_class

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
async def mem(ctx):
    img_name = random.choice(os.listdir('Мемы про глобальное потепление'))
    with open(f'Мемы про глобальное потепление/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def prichini(ctx):
    img_name = random.choice(os.listdir('Причины глобального потепления'))
    with open(f'Причины глобального потепления/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def posledstvia(ctx):
    img_name = random.choice(os.listdir('Последствия глобального потепления'))
    with open(f'Последствия глобального потепления/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def znachenie(ctx):
    img_name = random.choice(os.listdir('О глобальном потеплении'))
    with open(f'О глобальном потеплении/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def borba(ctx):
    img_name = random.choice(os.listdir('Меры борьбы с глобальным потеплением'))
    with open(f'Меры борьбы с глобальным потеплением/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send('Вы забыли загрузить картинку')

bot.run("MTE5ODUzNTA0MDYyODQ0NTIwNA.G8Jdr8.dKCQqvxxxKvRFNIanmtIV83h67b5b7RevgbPX0")