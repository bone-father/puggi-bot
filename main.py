import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if "mitten" in message.content.lower():
        await message.channel.send("Well yes, I'd love to cum in your mittens thanks for asking")

    await bot.process_commands(message)

@bot.command()
async def nicole(ctx):
    await ctx.send(file=discord.File('images/nicole.jpg'))

@bot.command()
async def zach(ctx):
    await ctx.send(file=discord.File('images/zach.jpg'))

bot.run('OTM0MzU2MDYyNDg2ODAyNDUy.Yeu45A._FoadnBB34yHvk4vL6Xrvtwqs9U')
