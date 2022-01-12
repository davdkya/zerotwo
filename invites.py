import discord
from discord.ext import commands
import DiscordUtils


Intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
bot = commands.AutoShardedBot(command_prefix="")
tracker = DiscordUtils.InviteTracker(bot)

@bot.event
async def on_ready():
    await tracker.cache_invites()
    print("Ready!")

@bot.event
async def on_invite_create(invite):
    await tracker.update_invite_cache(invite)

@bot.event
async def on_guild_join(guild):
    await tracker.update_guild_cache(guild)

@bot.event
async def on_invite_delete(invite):
    await tracker.remove_invite_cache(invite)

@bot.event
async def on_guild_remove(guild):
    await tracker.remove_guild_cache(guild)

@bot.event
async def on_member_join(member):
    inviter = await tracker.fetch_inviter(member)  # inviter is the member who invited
    data = await bot.invites.find(inviter.id)
    if data is None:
        data = {"_id": inviter.id, "count": 0, "userInvited": []}

    data["count"] += 1
    data["usersInvited"].append(member.id)
    await bot.invites.upsert(data)

    channel = discord.utils.get(member.guild.text_channels, name="door")
    embed = discord.Embed(
            title=f"Welcome {member.display_name}",
            description=f"Invited by: {inviter.mention}\nInvites: {data['count']}",
            timestamp=member.joined_at
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)
    await channel.send(embed=embed)


bot.run("OTI3NDM5NjAwMzA0MTQwMjg5.YdKPbw.S7AVRmHitZjIDrWgiC6yngpQDcg")