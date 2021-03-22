
import discord
from discord.ext import commands

class AutoModCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

@commands.Cog.listener
async def on_message(ctx):
    if not (msg.author.name == "HackMaster" or "Dom's Bot"):
        if not (msg.author.discriminator == "0190" or "9264"):
            for word in filtered_words:
                if word in msg.content:
                    await msg.delete()
                    await msg.channel.send(
                        f"{msg.author.name} that word is not allowed! :0")



def setup(client):
	client.add_cog(HelpCommand(client))