import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='=', help_command=None)

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

        sentence = message.content.lower()
        mitten = "mitten"
        count = 0

        for i in range(len(sentence)-5):
            if sentence[i] == 'm':
                word = ""
                for k in range(6):
                    word = word + sentence[i+k]
                if word == mitten:
                    count = count + 1

        if count > 33:
            await message.channel.send("i don't have enough characters for this shit " + "<:void:935298651780161576>")
        else:
            await message.channel.send("Well yes, I'd love to cum in your mittens thanks for asking\n"*count)

    if "honk" in message.content.lower() or "honque" in message.content.lower():
        await message.channel.send(random.choice(honk_gifs))

    if "coop" in message.content.lower() or "co-op" in message.content.lower():
        await message.channel.send("interview selections complete")

    await bot.process_commands(message)

@bot.command()
async def help(ctx):
    help = discord.Embed(
        title = "cum",
        description = "prefix is '='",
        colour = discord.Colour.from_rgb(117, 211, 240)
    )

    help.add_field(name="people commands", value="bohdan\nlucas\nnicole\nsyed\nwendy\nxander\nzach\nzomer", inline=True)
    help.add_field(name="other stuff idk", value="heart <emoji>\nratemychances\nscream", inline=True)
    help.set_footer(text="lol get fucked")
    help.set_image(url="https://cdn.discordapp.com/attachments/893186562274234408/935379384116850738/monke.gif")

    await ctx.send(embed=help)

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
async def zomer(ctx):
    await ctx.send('https://cdn.weeb.sh/images/rJ4E1ep7f.gif')

@bot.command()
async def bohdan(ctx):
    await ctx.send(file=discord.File('images/bohdan.jpg'))

@bot.command()
async def ratemychances(ctx):
    await ctx.send('https://www.conestogac.on.ca/')

@bot.command()
async def scream(ctx):
    await ctx.send('A' + 'H'*309)

@bot.command()
async def heart(ctx, emoji):
    cock = '<:x_:935311266845712384>'
    heart = [(cock + emoji*2 + cock*3 + emoji*2 + cock + '\n'), (emoji*4 + cock + emoji*4 + '\n'), 
                (emoji*9 + '\n'), (cock + emoji*7 + cock + '\n'), (cock*2 + emoji*5 + cock*2 + '\n'), 
                (cock*3 + emoji*3 + cock*3 + '\n'), (cock*4 + emoji + cock*4)]
    heart_2 = heart[0] + heart[1] + heart[2]*2 + heart[3] + heart[4] + heart[5] + heart[6]
    character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`-=~_+[]\;\',./{}|:"<>?'
    emoji_id = emoji[-19:-1:1]
    message_sent = False

    for i in ctx.guild.emojis:
        if len(emoji_id) == 18 and emoji[0] == '<' and emoji[-1] == '>' and emoji_id in str(i):
            if len(emoji) > 29:
                await ctx.send("i don't have enough characters for this shit " + "<:void:935298651780161576>")
            await ctx.send(heart_2)
            message_sent = True
            break

    if message_sent == False:
        for char in emoji:
            if char in character_list:
                break
            else:
                await ctx.send(heart_2)
                break

    if emoji == "gub":
        r_1 = "_               _ gub gub gub                                        gub gub gub \n"
        r_2 = "        gub gub gub gub gub                         gub gub gub gub gub\n"
        r_3 = "    gub gub gub gub gub gub                 gub gub gub gub gub gub\n"
        r_4 = "gub gub gub gub gub gub gub         gub gub gub gub gub gub gub\n"
        r_5_8 = "gub gub gub gub gub gub gub gub gub gub gub gub gub gub gub\n"
        r_9 = "    gub gub gub gub gub gub gub gub gub gub gub gub gub gub\n"
        r_10 = "        gub gub gub gub gub gub gub gub gub gub gub gub gub\n"
        r_11 = "                gub gub gub gub gub gub gub gub gub gub gub\n"
        r_12 = "                        gub gub gub gub gub gub gub gub gub\n"
        r_13 = "                                gub gub gub gub gub gub gub\n"
        r_14 = "                                        gub gub gub gub gub\n"
        r_15 = "                                                gub gub gub\n"
        r_16 = "                                                        gub"
        await ctx.send(r_1 + r_2 + r_3 + r_4 + r_5_8*4 + r_9 + r_10 + r_11 + r_12 + r_13 + r_14 + r_15 + r_16)

bot.run('OTM0MzU2MDYyNDg2ODAyNDUy.Yeu45A._FoadnBB34yHvk4vL6Xrvtwqs9U')
