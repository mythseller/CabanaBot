import os
import discord
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents = intents)
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.listen()
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    guild = message.guild
    # Identify target channels just get the channel ID
    alerts_channel = guild.get_channel(961396252774387713)
    # target roles, again just the role ID. Change the names to fit your use case. 
    lotto_role = guild.get_role(961515684351868998)
    intraday_role = guild.get_role(961533314500558868)
    swing_role = guild.get_role(961535201488547871)
    futures_role = guild.get_role(961599574462586900)
    memes_role = guild.get_role(961535641533972492)

    if lotto_role in message.role_mentions:
        msg = message.content.strip(f"<@&{lotto_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0xe91e63,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Lotto")
        embed.set_author(
            name=message.author.display_name 
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await alerts_channel.send(msg + " - " + f"<@&{lotto_role.id}>")
        # await noti.delete()
        target = await alerts_channel.send(embed=embed)
        message = await message.channel.send(embed=embed)
        await message.add_reaction("📥")
        await message.add_reaction("❌")
        await target.add_reaction("🟢")
        await target.add_reaction("🔴")

    elif intraday_role in message.role_mentions:
        msg = message.content.strip(f"<@&{intraday_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0x2ecc71,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Intraday")
        embed.set_author(
            name=message.author.display_name 
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await alerts_channel.send(msg + " - " + f"<@&{intraday_role.id}>")
        # await noti.delete()
        target = await alerts_channel.send(embed=embed)
        message = await message.channel.send(embed=embed)
        await message.add_reaction("📥")
        await message.add_reaction("❌")
        await target.add_reaction("🟢")
        await target.add_reaction("🔴")
        
    elif swing_role in message.role_mentions:
        msg = message.content.strip(f"<@&{swing_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0x3498db,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Swing")
        embed.set_author(
            name=message.author.display_name 
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await alerts_channel.send(msg + " - " + f"<@&{swing_role.id}>")
        # await noti.delete()
        target = await alerts_channel.send(embed=embed)
        message = await message.channel.send(embed=embed)
        await message.add_reaction("📥")
        await message.add_reaction("❌")
        await target.add_reaction("🟢")
        await target.add_reaction("🔴")
        
    elif futures_role in message.role_mentions:
        msg = message.content.strip(f"<@&{futures_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0x9b59b6,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Futures")
        embed.set_author(
            name=message.author.display_name 
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await alerts_channel.send(msg + " - " + f"<@&{futures_role.id}>")
        # await noti.delete()
        target = await alerts_channel.send(embed=embed)
        message = await message.channel.send(embed=embed)
        await message.add_reaction("📥")
        await message.add_reaction("❌")
        await target.add_reaction("🟢")
        await target.add_reaction("🔴")        

    elif memes_role in message.role_mentions:
        msg = message.content.strip(f"<@&{memes_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0xe74b3c,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value="Meme Play")
        embed.set_author(
            name=message.author.display_name 
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti = await alerts_channel.send(msg + " - " + f"<@&{memes_role.id}>")
        # await noti.delete()
        target = await alerts_channel.send(embed=embed)
        message = await message.channel.send(embed=embed)
        await message.add_reaction("📥")
        await message.add_reaction("❌")
        await target.add_reaction("🟢")
        await target.add_reaction("🔴")
        
       
    #elif role_2 in message.role_mentions:
    # Longform Format useful for briefs  
    #    msg = message.content.strip(f"<@&{spy_role.id}>")
    #    embed = discord.Embed(
    #        title="Market Commentary",
    #        description=msg,
    #        color=0x0be60b,
    #        timestamp=datetime.now(),
    #    )
    #    embed.add_field(name="Index:", value=spy_role.mention)
    #    embed.set_author(
    #        name=message.author.display_name, icon_url=message.author.avatar_url
    #    )
    #    embed2 = discord.Embed(
    #        title=msg,
    #        color=0x0be60b,
    #        timestamp=datetime.now(),
    #    )
    #    embed2.set_author(
    #        name=message.author.display_name, icon_url=message.author.avatar_url
    #    )
    #    await second_channel.send("<@&942052888333676634>")
    #    await second_channel.send(embed=embed)
    #    await target3_channel.send(embed=embed2)
    #    await message.channel.send(embed=embed)


@bot.listen()
async def on_message(message):
  '''simple on message to respond if a message containing "hello" is sent'''
  # prevent bot from answering other bots, including self
  if message.author.bot:
     return
  # create message content and channel variables
  content = message.content.lower()
  channel = message.channel
  # check if message includes "hello"
  if 'did we do today' in content:
    msg = await channel.send('yeah, you bank on these dank callouts or fuck it up?')
    await msg.add_reaction("🟢")
    await msg.add_reaction("🔴")
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


if __name__ == "__main__":
    bot.run(TOKEN)
