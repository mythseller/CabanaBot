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
    intraday_role = guild.get_role(123456789)
    swing_role = guild.get_role(123456789)
    futures_role = guild.get_role(123456789)
    memes_role = guild.get_role(123456789)

    if lotto_role in message.role_mentions:
        msg = message.content.strip(f"<@&{lotto_role.id}>")
        embed = discord.Embed(
            title=msg,
            color=0xad1357,
            timestamp=datetime.now(),
        )
        embed.add_field(name="Trade type:", value=lotto_role.mention)
        embed.set_author(
            name=message.author.display_name 
        )
        embed.set_thumbnail(url=message.author.avatar_url)
        noti1 = await alerts_channel.send(msg + " - " + "<@&961515684351868998>")
        # await noti1.delete()
        await alerts_channel.send(embed=embed)
        message1 = await message.channel.send(embed=embed)

    elif role_2 in message.role_mentions:
        msg = message.content.strip(f"<@&{role_2.id}>")
        embed = discord.Embed(title=msg, color=0xe0dd12, timestamp=datetime.now())
        embed.add_field(name="Trade Type:", value=role_2.mention)
        embed.set_author(
            name=message.author.display_name, icon_url=message.author.avatar_url
        )
        await target1_channel.send(embed=embed)
        await message.channel.send(embed=embed)
        


        
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
