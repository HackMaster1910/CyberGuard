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
            with open("level.json", "r", encoding="utf8") as f:
                    user = json.load(f)
            try:
                with open("level.json", "w", encoding="utf8") as f:
                    user[str(message.author.id)]["XP"] = user[str(message.author.id)]["XP"]+1
                    level_start = user[str(message.author.id)]["level"]
                    level_end = user[str(message.author.id)]["XP"] ** (1.5/4)
                    if level_start < level_end:
                        user[str(message.author.id)]["level"] = user[str(message.author.id)]["level"]+1
                        level = user[str(message.author.id)]["level"]
                        await message.channel.send(f"Congrats {message.author.name}! You just leveled up to level {level}!")
                        json.dump(user,f,sort_keys=True,indent=4,ensure_ascii=False)
                        return
                    json.dump(user,f,sort_keys=True,indent=4,ensure_ascii=False)
            except:
                with open("level.json", "w", encoding="utf8") as f:
                    user={}
                    user[str(message.author.id)] = {}
                    user[str(message.author.id)]["level"] = 0
                    user[str(message.author.id)]["XP"] = 0
                    json.dump(user,f,sort_keys=True,indent=4,ensure_ascii=False)
    
