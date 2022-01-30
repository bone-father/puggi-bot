import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='=', help_command=None, intents=intents)
embed_colour = discord.Colour.from_rgb(117, 211, 240)

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

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="You All Fail ECE"))
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if "mitten" in message.content.lower() and message.guild.id != 826111461734219787:

        sentence = message.content.lower()
        mitten = "mitten"
        lucas = "Well yes, I'd love to cum in your mittens thanks for asking\n"
        count = 0

        for i in range(len(sentence)-5):
            if sentence[i] == 'm':
                word = ""
                for k in range(6):
                    word = word + sentence[i+k]
                if word == mitten:
                    count = count + 1

        if count <= 33:
            await message.channel.send(lucas*count)
        elif count > 33 and count <= 68:
            cum_mittens = discord.Embed(description = lucas*count, colour = embed_colour)
            await message.channel.send(embed=cum_mittens)
        else:
            await message.channel.send("i don't have enough characters for this shit " + "<:void:935298651780161576>")

    if "cope" in message.content.lower():
        await message.channel.send("don't care + didn't ask + cry about it + stay mad + get real + L + mald seethe cope harder + hoes mad + basic + skill issue + ratio + you fell off + the audacity + triggered + any askers + redpilled + get a life + ok and? + cringe + touch grass + donowalled + not based + your're a (insert stereotype) + not funny didn't laugh + you're* + grammar issue + go outside + get good + reported + ad hominem + GG! + ur mom + cope + bluepilled + strawman + slippery slope + gambler's fallacy")

    if "honk" in message.content.lower() or "honque" in message.content.lower():
        await message.channel.send(random.choice(honk_gifs))

    if "coop" in message.content.lower() or "co op" in message.content.lower() or "co-op" in message.content.lower():
        await message.channel.send("interview selections complete")

    if "puggi" in message.content.lower() or '695356435168493598' in message.content:
        await message.channel.send(file=discord.File('images/puggi/' + str(random.randint(1, 27)) + '.jpg'))

    if "nicole" in message.content.lower().replace("=nicole", "") or '807095862747856897' in message.content:
        await message.channel.send(file=discord.File('images/mommy/' + str(random.randint(1, 11)) + '.png'))

    await bot.process_commands(message)

@bot.command()
async def help(ctx):

    if ctx.guild.id == 826111461734219787:

        help = discord.Embed(
            title = "cum",
            description = "prefix is '='\n\napart from commands, bot also responds to \"coop\", \"cope\", \"honk\"/\"honque\", \"nicole\", and \"puggi\"",
            colour = embed_colour
        )

        help.add_field(name="people commands", value="anthony\nbohdan\nelena\ngub\npogman\nsyed\nwendy\nxander\nzach", inline=True)
        help.add_field(name="other stuff idk", value="heart <emoji>\nneutralgnag\npat\nrate\nscream\ntext", inline=True)   

    else:

        help = discord.Embed(
            title = "cum",
            description = "prefix is '='\n\napart from commands, bot also responds to \"coop\", \"cope\", \"honk\"/\"honque\", \"mitten\", \"nicole\", and \"puggi\"",
            colour = embed_colour
    )

        help.add_field(name="people commands", value="anthony\nbohdan\nelena\ngub\nnicole\npogman\nsyed\nwendy\nxander\nzach\nzomer", inline=True)
        help.add_field(name="other stuff idk", value="cock <emoji>\nheart <emoji>\nneutralgnag\npat\nrate\nscream\ntext", inline=True)

    help.set_footer(text="lol get fucked")
    help.set_image(url="https://cdn.discordapp.com/attachments/893186562274234408/935379384116850738/monke.gif")

    await ctx.send(embed=help)

@bot.command()
async def nick(ctx, new_nick):
    if ctx.message.author.id == 700092415910084608:
        member = ctx.guild.get_member(934356062486802452)
        if new_nick.lower() == "reset":
            await member.edit(nick="")
        else:
            await member.edit(nick=new_nick)
    else:
        await ctx.send("uwu only my daddy can do that")

@bot.command()
async def nicole(ctx):
    if ctx.guild.id != 826111461734219787:
        await ctx.send(file=discord.File('images/nicole.jpg'))

@bot.command()
async def zach(ctx):
    await ctx.send(file=discord.File('images/zach.jpg'))

@bot.command()
async def wendy(ctx):
    await ctx.send("go fuck yourself")

@bot.command()
async def syed(ctx):
    await ctx.send(file=discord.File('images/syed.jpg'))

@bot.command()
async def xander(ctx):
    await ctx.send(file=discord.File('images/xander.jpg'))

@bot.command()
async def zomer(ctx):
    if ctx.guild.id != 826111461734219787:
        await ctx.send(file=discord.File('images/zomer.jpg'))

@bot.command()
async def pat(ctx):
    await ctx.send('https://cdn.weeb.sh/images/rJ4E1ep7f.gif')

@bot.command()
async def bohdan(ctx):
    await ctx.send(file=discord.File('images/bohdan.jpg'))

@bot.command()
async def rate(ctx):
    await ctx.send('https://www.conestogac.on.ca/')

@bot.command()
async def scream(ctx):
    await ctx.send('A' + 'H'*805)

@bot.command()
async def heart(ctx, emoji):
    cock = '<:x_:935311266845712384>'
    heart = [(cock + emoji*2 + cock*3 + emoji*2 + cock + '\n'), (emoji*4 + cock + emoji*4 + '\n'), 
                (emoji*9 + '\n'), (cock + emoji*7 + cock + '\n'), (cock*2 + emoji*5 + cock*2 + '\n'), 
                (cock*3 + emoji*3 + cock*3 + '\n'), (cock*4 + emoji + cock*4)]
    heart_2 = heart[0] + heart[1] + heart[2]*2 + heart[3] + heart[4] + heart[5] + heart[6]
    heart_3 = discord.Embed(title = "uwu <3", description = heart_2, colour = embed_colour)
    character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`-=~_+[]\;\',./{}|:"<>?'
    emoji_id = emoji[-19:-1:1]
    message_sent = False

    for i in ctx.guild.emojis:
        if len(emoji_id) == 18 and emoji[0] == '<' and emoji[-1] == '>' and emoji_id in str(i):
            await ctx.send(embed=heart_3)
            message_sent = True
            break

    if message_sent == False:
        for char in emoji:
            if char in character_list:
                break
            else:
                await ctx.send(embed=heart_3)
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

@bot.command()
async def cock(ctx, emoji):
    if ctx.guild.id != 826111461734219787:
        cock = '<:x_:935311266845712384>'
        dick = [(cock*3 + emoji*3 + cock*3 + '\n'), (cock*2 + emoji + cock + emoji + cock + emoji + cock*2 + '\n'), 
                (cock*2 + emoji + cock*3 + emoji + cock*2 + '\n'), (cock*2 + emoji*5 + cock*2 + '\n'), 
                (cock + emoji*2 + cock*3 + emoji*2 + cock + '\n'), (emoji + cock*7 + emoji + '\n'), 
                (emoji + cock*3 + emoji + cock*3 + emoji + '\n'), (cock + emoji*3 + cock + emoji*3 + cock + '\n')]
        dick_2 = dick[0] + dick[1] + dick[2] + dick[3] + dick[2]*3 + dick[4] + dick[5]*2 + dick[6] + dick[7]
        dick_3 = discord.Embed(title = "uwu 🍆💦", description = dick_2, colour = embed_colour)
        character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()`-=~_+[]\;\',./{}|:"<>?'
        emoji_id = emoji[-19:-1:1]
        message_sent = False

        for i in ctx.guild.emojis:
            if len(emoji_id) == 18 and emoji[0] == '<' and emoji[-1] == '>' and emoji_id in str(i):
                await ctx.send(embed=dick_3)
                message_sent = True
                break

        if message_sent == False:
            for char in emoji:
                if char in character_list:
                    break
                else:
                    await ctx.send(embed=dick_3)
                    break

@bot.command()
async def text(ctx):
    await ctx.send(file=discord.File('images/text.jpg'))

@bot.command()
async def pogman(ctx):
    await ctx.send("Oh hi there! I saw you at the engineering campfire last night. I just wanted to say, it's really cool to see a woman in engineering. You may already know me, but my name is pogman. Since we're already friends, you can call me poggy. Yes, I'm pretty famous around here (I'm THE owner of the ECE 26 discord server, which is the most active one if you didn't know). Do you want to be admin in there? It would be very poggers if you would.\n\nHonestly though, I'm not sure we'd get along well; I don't want \"girl\" and \"crush\" to be in my vocabulary this year lol. But yeah, DM me if you wanna hang out. I hate sexism!")

@bot.command()
async def neutralgnag(ctx):
    await ctx.send(file=discord.File('images/neutralgnag.png'))

@bot.command()
async def anthony(ctx):
    await ctx.send(file=discord.File('images/anthony.gif'))

@bot.command()
async def gub(ctx):
    await ctx.send(file=discord.File('images/will.jpg'))

@bot.command()
async def elena(ctx):
    await ctx.send('https://tenor.com/view/ant-gif-24107201')

bot.run('OTM0MzU2MDYyNDg2ODAyNDUy.Yeu45A._FoadnBB34yHvk4vL6Xrvtwqs9U')
