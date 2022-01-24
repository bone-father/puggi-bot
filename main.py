import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='=')

honk_gifs = ["https://tenor.com/view/goose-honk-inhale-inhales-untitled-gif-16237480", 
             "https://tenor.com/view/thug-life-deal-with-it-gif-20556615", 
             "https://tenor.com/view/goose-gif-5452772", 
             "https://tenor.com/view/do-the-goose-do-the-goos-goos-goose-desktop-goose-gif-17638837", 
             "https://tenor.com/view/goose-geese-flying-fly-soaring-gif-5452768", 
             "https://tenor.com/view/bird-attack-inside-car-goose-wtf-horror-gif-19141111", 
             "https://tenor.com/view/rock-talk-goose-bird-arms-gif-21082454", 
             "https://tenor.com/view/goose-goose-wc-duck-duck-goose-gif-20838944", 
             "https://tenor.com/view/chaos-nickfifs-fire-goose-hook-gif-20475840", 
             "https://tenor.com/view/goose-grey-mess-with-the-honk-you-get-the-bonk-statewide-rp-gif-17425385", 
             "https://tenor.com/view/goose-geese-gif-5452767", 
             "https://tenor.com/view/tower-unite-goose-lud-spin-goose-spin-gif-22919607", 
             "https://tenor.com/view/geese-goose-cows-animals-funny-gif-13375385", 
             "https://tenor.com/view/goose-you-came-to-the-wrong-neighborhood-come-at-me-bro-gif-5452771", 
             "https://tenor.com/view/goose-cat-get-out-peek-fake-bird-gif-17500553", 
             "https://tenor.com/view/birds-kid-nope-run-attack-gif-11840434", 
             "https://tenor.com/view/little-girl-air-strike-canadian-goose-goose-flight-gif-11694380", 
             "https://tenor.com/view/gooose-goose-revolution-goose-geese-revolution-war-gif-24170085", 
             "https://tenor.com/view/yes-gif-13774575", 
             "https://tenor.com/view/justketh-goose-attack-goose-attack-gif-21405247", 
             "https://tenor.com/view/gotcha-bitch-thug-life-angry-goose-kid-gif-16369726", 
             "https://tenor.com/view/gorillas-geese-goose-chase-attack-gif-3472836", 
             "https://tenor.com/view/goose-gif-15180835", 
             "https://tenor.com/view/goose-greylag-greylag-goose-fly-chase-gif-17035526", 
             "https://tenor.com/view/march-forth-spring-funny-animals-geese-spring-time-gif-13640219"]

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if "mitten" in message.content.lower():
        await message.channel.send("Well yes, I'd love to cum in your mittens thanks for asking")

    if "honk" in message.content.lower() or "honque" in message.content.lower():
        await message.channel.send(random.choice(honk_gifs))

    await bot.process_commands(message)

@bot.command()
async def nicole(ctx):
    await ctx.send(file=discord.File('images/nicole.jpg'))

@bot.command()
async def zach(ctx):
    await ctx.send(file=discord.File('images/zach.jpg'))

@bot.command()
async def wendy(ctx):
    await ctx.send("go fuck yourself")

@bot.command()
async def lucas(ctx):
    await ctx.send(file=discord.File('images/lucas.jpg'))

@bot.command()
async def syed(ctx):
    await ctx.send(file=discord.File('images/syed.jpg'))

@bot.command()
async def xander(ctx):
    await ctx.send(file=discord.File('images/xander.jpg'))

@bot.command()
async def ratemychances(ctx):
    await ctx.send('https://www.conestogac.on.ca/')

@bot.command()
async def scream(ctx):
    await ctx.send('A' + 'H'*309)
    
@bot.command()
async def zomer(ctx):
    await ctx.send('https://cdn.weeb.sh/images/rJ4E1ep7f.gif')
    
bot.run('OTM0MzU2MDYyNDg2ODAyNDUy.Yeu45A._FoadnBB34yHvk4vL6Xrvtwqs9U')
