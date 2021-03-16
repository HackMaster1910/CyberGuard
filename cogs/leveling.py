import discord
from discord.ext import commands
import json

class leveling(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
def setup(client):
        client.add_cog(leveling(client))

        @commands.Cog.listener()
        async def on_message(self, message):
            print("test")
