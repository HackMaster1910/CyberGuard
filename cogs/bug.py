
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
                embed=discord.Embed(Color=0xFF0000)
                embed.add_field(name="Bug Report! 🐛", value=f'Your bug: "{issue}" has been successfully sent!')
                await ctx.channel.send(embed=embed)
                bugchannel = self.client.get_channel(825713979304968202)
                await bugchannel.send(f'{ctx.author} just sent the bug: "{issue}"')



def setup(client):
	client.add_cog(BugCommand(client))

