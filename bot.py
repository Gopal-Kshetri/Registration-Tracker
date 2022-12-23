import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

from fetch import fetch_data
from friends import friends_quote

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(intents=discord.Intents.all(),command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')


@bot.command(name='help', help='Commands for the Discord bot')
async def help(ctx):
    embed=discord.Embed(
        title="Help", 
        description="Commands for Registration Tracker", 
        color=discord.Color.orange()
        )
    embed.set_author(
        name=ctx.author.display_name, 
        url="https://twitter.com/RealDrewData", 
        icon_url=ctx.author.avatar.url
        )
    embed.set_thumbnail(url="https://res.cloudinary.com/dk128umo9/image/upload/v1669703912/logo-min_u8zcgc.png")

    bot_commands = ['help', 'quote', 'query']
    descriptions = ['Displays commands for the Discord bot', 'Responds with a random quote from Friends', 'Provides you the Registered Teams and Details']
    for (bot_command,description) in zip(bot_commands, descriptions):
        embed.add_field(name=f'**{bot_command}**', value=f'> {description}', inline=False)

    await ctx.send(embed=embed)


@bot.command(name = 'query', help='Embed in Discord')
async def interns(ctx):
    teams_color=discord.Color.magenta()
    embed=discord.Embed(
        title="Hult Prize Registration", 
        url="https://oncampus.hultprize.org/pulchowkcampus", 
        description="Registered Teams", 
        color=teams_color
        )
    embed.set_author(
        name=ctx.author.display_name, 
        url="https://twitter.com/RealDrewData", 
        icon_url=ctx.author.avatar.url
        )
    embed.set_thumbnail(url="https://res.cloudinary.com/dk128umo9/image/upload/v1669703912/logo-min_u8zcgc.png")
        
    teams= fetch_data()
    embed.add_field(name=f'**TOTAL TEAMS: **', value=f'> {len(teams)}', inline=False)
    j=0
    max_val = 40
    for each_team in teams:
        j += 1
        if j%max_val != 0 and j<max_val:
            embed.add_field(name=f'**{each_team[0]}**', value=f'> Team Leader: {each_team[1]} \n> Email: {each_team[2]} \n> Contact:{each_team[3]} \n> Registered Time:{each_team[4]}', inline=False)

        else:
            if j % max_val == 0:
                await ctx.send(embed=embed)
                embed = discord.Embed(
                    title="Continue...", 
                    url="https://oncampus.hultprize.org/pulchowkcampus", 
                    description="Registered Teams", 
                    color=teams_color
                )

        if j > max_val and (j % max_val != 0):
            embed.add_field(name=f'**{each_team[0]}**', value=f'> Team Leader: {each_team[1]} \n> Email: {each_team[2]} \n> Contact:{each_team[3]} \n> Registered Time:{each_team[4]}', inline=False)         

    await ctx.send(embed=embed)

@bot.command(name='quote', help='Responds with a random quote from Brooklyn 99')
async def quote(ctx):
    response = friends_quote()
    await ctx.send(response)
    


bot.run(TOKEN)
