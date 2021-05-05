
import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(color=0xFF0000, name = "Commands Help")
		embed.add_field(
			value='`rank`', 
			name='Levelling 🔢', 
			inline=False)
		embed.add_field(
			value='`work`, `balance`, `give`', 
			name='Currency 💰', 
			inline=False)
		embed.add_field(
			value='`connect`, `play`, `pause`, `stop`, `resume`, `now_playing`, `queue`,`volume`', 
			name='Music 🎵', 
			inline=False)
		embed.add_field(
			value='`afk`,`user`', 
			name='Utilitys 🧰', 
			inline=False)
		embed.add_field(
			value='`kick`, `ban`,`unban`', 
			name='Moderator ⛏', 
			inline=False)
		embed.add_field(
			value='`joke`, `8ball`', name='Fun 🥳', inline=False)
		embed.add_field(
			value='`server`, `members`, `author`', name='Info ℹ', inline=False)
		embed.add_field(
			value='`official`, `bot`, `ping`, `about`, `bug`', name='Bot 🤖', inline=False)
		await ctx.send(embed=embed)



def setup(client):
	client.add_cog(HelpCommand(client))

