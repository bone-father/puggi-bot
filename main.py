import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if "mitten" in message.content.lower():
        await message.channel.send("Well yes, I'd love to cum in your mittens thanks for asking")

client.run('OTM0MzU2MDYyNDg2ODAyNDUy.Yeu45A._FoadnBB34yHvk4vL6Xrvtwqs9U')