import discord
from discord.ext import commands
import time
import animec
import music

cogs = [music]

Intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix="", intents=Intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Anime'))
    print("Let's Go My Darling!")


@client.command()
async def kick(ctx, member:discord.member.Member, *args, reason=""):
    if commands.has_permissions(kick_members=True):
        await member.kick(reason=reason)
    elif commands.has_permissions(kick_members=False):
        ctx.send("Hadi Köyüne...")


@client.command()
async def ban(ctx, member:discord.member.Member, *args, reason=""):
    if commands.has_permissions(ban_members=True):
        await member.ban(reason=reason)
    elif commands.has_permissions(ban_members=False):
        ctx.send("Hadi Köyüne...")


@client.command()
async def question(ctx):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")
    await ctx.message.add_reaction("🇨")
    await ctx.message.add_reaction("🇩")

@client.command()
async def question_4(ctx):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")
    await ctx.message.add_reaction("🇨")
    await ctx.message.add_reaction("🇩")

@client.command()
async def question_6(ctx):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")
    await ctx.message.add_reaction("🇨")
    await ctx.message.add_reaction("🇩")
    await ctx.message.add_reaction("🇪")
    await ctx.message.add_reaction("🇫")

@client.command()
async def question_2(ctx):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")

@client.command()
async def question_3(ctx):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")
    await ctx.message.add_reaction("🇨")

@client.command()
async def question_5(ctx):
    await ctx.message.add_reaction("🇦")
    await ctx.message.add_reaction("🇧")
    await ctx.message.add_reaction("🇨")
    await ctx.message.add_reaction("🇩")
    await ctx.message.add_reaction("🇪")

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="door")
    await channel.send(f"{member}, Hello! Welcome to the server")

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="door")
    await channel.send(f"It Seems The {member} Go Away...")

@client.command()
async def anime(ctx, *, query):
    try:
        anime = animec.Anime(query)
    except:
        await ctx.send('No Matching Anime...')
        return
    embed = discord.Embed(title=anime.title_english, url=anime.url, description=f"{anime.description[:200]}...", color=discord.Color.random())
    embed.add_field(name="Episodes", value=str(anime.episodes))
    embed.add_field(name="Rating", value=str(anime.rating))
    embed.add_field(name="Broadcast", value=str(anime.broadcast))
    embed.add_field(name="Status", value=str(anime.status))
    embed.add_field(name="Type", value=str(anime.type))
    embed.set_thumbnail(url=anime.poster)
    await ctx.send(embed = embed)

@client.command()
async def aninews(ctx, amount:int=5):
    news = animec.Aninews(5)
    links = news.links
    titles = news.titles
    descriptions = news.description

    embed = discord.Embed(title = "Lastest Anime News", color= discord.Color.random())
    embed.set_thumbnail(url=news.images[0])

    for i in range(amount):
        embed.add_field(name = f"{i+1}) {titles[i]}", value = f"{descriptions[i][:200]}...\n[Read More]({links[i]})", inline=False)

    await ctx.send(embed = embed)


@client.command()
async def hi(msg):
    await msg.send("https://c.tenor.com/saF7OqqJkFsAAAAC/darling-in-the-franxx-anime.gif")

@commands.has_permissions(manage_messages=True)
@client.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(":broom: Huh, That's it. :broom:")
    time.sleep(1)
    await ctx.channel.purge(limit=1)

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run('OTI3NDM5NjAwMzA0MTQwMjg5.YdKPbw.S7AVRmHitZjIDrWgiC6yngpQDcg')