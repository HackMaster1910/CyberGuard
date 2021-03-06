import discord
from discord.ext import commands
import json
import asyncio
import pymongo
from pymongo import MongoClient


class leveling(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener("on_message")
    async def level(self, ctx):
        mango_url = "mongodb+srv://dbUser:cyberguard@cluster0.25utt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        cluster = MongoClient(mango_url)
        db = cluster["CyberGuardBot"]
        collection = db["levels"]
        author_id = ctx.author.id
        guild_id = ctx.guild.id 

        author = ctx.author

        user_id = {"_id": author_id}

        if ctx.author.bot:
            return

        if(collection.count_documents({}) == 0):
            user_info = {"_id": author_id, "GuildID": guild_id, "Level": 1, "XP": 0}
            collection.insert_one(user_info)

        if(collection.count_documents(user_id) == 0):
            user_info = {"_id": author_id, "GuildID": guild_id, "Level": 1, "XP": 0}
            collection.insert_one(user_info)

        exp = collection.find(user_id)
        for xp in exp:
            cur_xp = xp["XP"]

            new_xp = cur_xp + 1 

        collection.update_one({"_id": author_id}, {"$set":{"XP":new_xp}}, upsert=True)

        lvl = collection.find(user_id)
        for levl in lvl:
            lvl_start = levl["Level"]

            new_level = lvl_start + 1

        if cur_xp >= round(5 * (lvl_start ** 4 / 5)):
            collection.update_one({"_id": author_id}, {"$set":{"Level":new_level}}, upsert=True)
            await ctx.channel.send(f"{author.mention} has leveled up to {new_level}!", delete_after=5)

    @commands.command()
    async def rank(self, ctx):
        mango_url = "mongodb+srv://dbUser:cyberguard@cluster0.25utt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        cluster = MongoClient(mango_url)
        db = cluster["CyberGuardBot"]
        collection = db["levels"]
        author_id = ctx.author.id
        user_id = {"_id": author_id}
        level = collection.find(user_id)
        embed = discord.Embed(title="Rank", description="Here is information about your level and XP!", color=0x03e8fc)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/814784481012482078/f4a22dcefba5aa59cfbcdaa6ba8e5e41.webp")
        for levl in level:
            rlevel = levl["Level"]
            embed.add_field(name="User", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=True)
            embed.add_field(name="Level", value=rlevel,inline=True)
        xp = collection.find(user_id)
        for eXP in xp:
            rxp = eXP["XP"]
            embed.add_field(name="XP", value=rxp, inline=True)
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(leveling(client))
