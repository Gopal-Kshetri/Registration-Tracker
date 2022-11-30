import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

from fetch import fetch_data
from friends import friends_quote

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', help_command=None)

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#         )


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
        icon_url=ctx.author.avatar_url
        )
    embed.set_thumbnail(url="https://res.cloudinary.com/dk128umo9/image/upload/v1669703912/logo-min_u8zcgc.png")

    bot_commands = ['help', 'quote', 'query']
    descriptions = ['Displays commands for the Discord bot', 'Responds with a random quote from Friends', 'Provides you the Registered Teams and Details']
    for (bot_command,description) in zip(bot_commands, descriptions):
        embed.add_field(name=f'**{bot_command}**', value=f'> {description}', inline=False)

    await ctx.send(embed=embed)


@bot.command(name = 'query', help='Embed in Discord')
async def interns(ctx):
    embed=discord.Embed(
        title="Hult Prize Registration", 
        url="https://admin-oncampus.hultprize.org/Account/Login", 
        description="Registered Teams", 
        color=discord.Color.blue()
        )
    embed.set_author(
        name=ctx.author.display_name, 
        url="https://twitter.com/RealDrewData", 
        icon_url=ctx.author.avatar_url
        )
    embed.set_thumbnail(url="https://res.cloudinary.com/dk128umo9/image/upload/v1669703912/logo-min_u8zcgc.png")
        
    teams= fetch_data()
    for each_team in teams:
        # print(title+ '\t' + author + '\t' + date + '\t')
        embed.add_field(name=f'**{each_team[0]}**', value=f'> Team Leader: {each_team[1]} \n> Email: {each_team[2]} \n> Contact:{each_team[3]} \n> Registered Time:{each_team[4]}', inline=False)

    await ctx.send(embed=embed)

@bot.command(name='quote', help='Responds with a random quote from Brooklyn 99')
async def quote(ctx):
    
    brooklyn_99_quotes = [
        'I\'m the human form of the :100: emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool,   '
            'no doubt no doubt no doubt. '
        ),
    ]

    response = friends_quote()
    await ctx.send(response)
    


bot.run(TOKEN)