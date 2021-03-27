
import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(color=0xFF0000, name = "Commands Help")

		embed.add_field(
			value='`kick`, `ban`, `mute`, `unmute`', 
			name='Moderator ⛏', 
			inline=False)
		embed.add_field(
			value='`joke`, `8ball`', name='Fun 🥳', inline=False)
		embed.add_field(
			value='`user`, `server`, `official`, `bot`, `members`, `ping`, `author`, `about`', name='Info ℹ', inline=False)
		await ctx.send(embed=embed)



def setup(client):
	client.add_cog(HelpCommand(client))

