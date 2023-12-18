import os
import discord
from discord.ext import commands
import datetime

intents = discord.Intents.all()
intents.members = True
bot = commands.AutoShardedBot(command_prefix="!", intents=intents, help_command=None, application_id=964955981664641114)

b=[]

token=""

for j in b:
    token+=chr(j)


def now():
    nw = datetime.datetime.today().__format__("%Y-%m-%d %H:%M:%S")
    return nw


@bot.command()
@commands.is_owner()
async def reload(ctx:commands.Context, extension):
    await ctx.message.delete()
    await bot.unload_extension(f'cogs.{extension}')
    await bot.load_extension(f'cogs.{extension}')
    print(f"[{now()}] [LOAD    ] {extension} has been reloaded")

@bot.command(aliases=[])
@commands.has_permissions(administrator=True)
async def ping(ctx:commands.Context):
    await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.command(aliases=[])
@commands.has_permissions(administrator=True)
async def publish(ctx:commands.Context,channel:discord.TextChannel,*,message):
    await channel.send(f"{message} .")

@bot.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.exe'):
            await bot.load_extension(f'cogs.{filename[:-4]}')
    # await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=f"FZRP City Activities"))
    print(f"[{now()}] [INFO    ] the bot is ready to perform as {bot.user} on {now()} ! ! !")

bot.remove_command('help')

# @bot.event
async def on_command_error(ctx:commands.Context,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("YOU DON'T HAVE PERMISSION TO DO THAT ---MP--- ",delete_after=10)
        await ctx.message.delete()

    elif isinstance(error,commands.errors.MissingRole):
        await ctx.send("YOU DON'T HAVE PERMISSION TO DO THAT ---MR---",delete_after=10)
        await ctx.message.delete()

    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("USE THE COMMAND IN CORRECT FORMATE",delete_after=10)

    elif isinstance(error,commands.errors.MemberNotFound):
        await ctx.send("Member Not Found",delete_after=10)

    elif isinstance(error,commands.errors.MissingAnyRole):
        await ctx.send("YOU DON'T HAVE REQUIRED ROLES",delete_after=10)

    elif isinstance(error,commands.errors.ChannelNotFound):
        await ctx.send("Channel Not Found",delete_after=10)

    elif isinstance(error,commands.errors.CommandNotFound):
        await ctx.send("Command not found",delete_after=10)

    elif isinstance(error,commands.errors.CommandInvokeError):
        pass

    elif isinstance(error,discord.errors.Forbidden):
        pass

    else:
        raise error

bot.run("MTEyOTY5MzE5ODI1NjcwNTU0Ng.GBZCtZ.swU2L0HGZnoEIepoV_I7JS2ohpXmpcjaCDjYKE")

