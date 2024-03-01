import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def bottone(ctx):
    """
    Function to send a message with 'ciao' and a gray button without emoji when user types '!bottone'.

    Parameters:
    - ctx: Context
        The context in which the command is being invoked.

    Returns:
    - None
        Sends a message with 'ciao' and a gray button without emoji.
    """

    # Creating a discord.Embed object for the message
    embed = discord.Embed(description='ciao', color=discord.Color.light_grey())

    # Adding a gray button to the message
    embed.add_field(name='\u200b', value='\u200b', inline=False)

    # Sending the message with the embed
    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
