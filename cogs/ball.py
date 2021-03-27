
import discord
from discord.ext import commands
import random

responses = [
    "Yes", "No", "Maybe", "My sources say no", "You can make it happen.",
    "I seem to have lost my connection with you try another question!",
    "As I see it, yes.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
    "It is certain.", "It is decidedly so."
]

class BallCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name="8ball")
	async def magicball(self, ctx):
		    embed = discord.Embed(color=0xFF0000)

		    embed.add_field(
			value=f'{random.choice(responses)}', 
			name='8ball 🎱', 
			inline=False)
		    await ctx.send(embed=embed)



def setup(client):
	client.add_cog(BallCommand(client))


