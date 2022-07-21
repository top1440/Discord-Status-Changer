import discord
from discord.ext import commands
from webserver import keep_alive
import colorama
from colorama import Fore

stream_url = "https://www.twitch.tv/putanything"

token="TOKEN"

prefix =","

Top = commands.Bot(command_prefix={prefix}, self_bot=True, help_command=None)

@Top.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(
        "```Discord Status Changer \n Streaming, Listening, Playing, Watching \n Example: \n ,s top | ,p top | ,l top | ,w top \n if you would like to view the aliases type ,aliases``` ")


@Top.command()
async def aliases(ctx):
    await ctx.message.delete()
    await ctx.send(
        "```> Streaming = ,stream | ,streaming | s \n > Playing | ,playing |,play | ,p | ,game  \n > Listening | ,listen | ,l \n > Watching | ,watch | ,w```")
      
@Top.command(aliases=["streamings", "s"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(content=f"``Set Streaming to {message}``", delete_after=3),
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Top.change_presence(activity=stream)
    print(f"{Fore.BLUE}[-] Set Streaming Status To: {Fore.RED}{message}")


@Top.command(aliases=["play", "p", "game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(content=f"``Set Playing to {message}``", delete_after=3),
    game = discord.Game(
        name=message
    )
    await Top.change_presence(activity=game)
    print(f"{Fore.BLUE}[-] Set Playing Status To: {Fore.RED}{message}")


@Top.command(aliases=["listen", "l"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(content=f"``Set Listening to {message}``", delete_after=3),
    await Top.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    print(f"{Fore.BLUE}[-] Set Listening Status To: {Fore.RED}{message}")


@Top.command(aliases=["watch", "w"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(content=f"``Set Watching to {message}``", delete_after=3),
    await Top.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))
    print(f"{Fore.BLUE}[-] Set Watching Status To: {Fore.RED}{message}")


@Top.command(aliases=["sav", "stopstatus", "stoplistening", "stopplaying", "stopwatching", "stopsreaming"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await ctx.send(content=f"``Stop Activity``", delete_after=3),
    await Top.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{Fore.BLUE}Stoped {Fore.RED}Activity")
  
keep_alive()
Top.run(token, bot=False)
