
import discord
from discord.ext import commands

class BugCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def bug(self, ctx, issue: str):
            if issue==None:
                await ctx.channel.send('You have to enter a bug to report! For example: ;bug "<bug>"')
            else:
                embed=discord.Embed(color=0xFF0000)
                embed.add_field(name="Bug Report! 🐛", value=f'Your bug: "{issue}" has been successfully sent!')
                await ctx.channel.send(embed=embed)
                embed=discord.Embed(color=0xFF0000)
                embed.add_field(name="New Bug Report! 🐛", value=f'New bug: "{issue}"')
                embed.set_author(name=ctx.author)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                bugchannel = self.client.get_channel(825713979304968202)
                await bugchannel.send(embed=embed)



def setup(client):
	client.add_cog(BugCommand(client))

