import discord
from discord.ext import commands
import json
import asyncio
import pymongo
from pymongo import MongoClient
import random

responses = [
            "Hey! Well done you earned", "Terrible work! >:( You only earned", "AMAZING! I'm proud of you! You earned", "Don't come back! You earned"
]

class currencysys(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def work(self, ctx):
        mango_url = "mongodb+srv://dbUser:cyberguard@cluster0.25utt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        cluster = MongoClient(mango_url)
        db = cluster["CyberGuardBot"]
        collection = db["currency"]  
        randomnumber = random.randint(100,3000)
        author_id = ctx.author.id

        author = ctx.author

        user_id = {"_id": author_id}

        if ctx.author.bot:
            return

        if(collection.count_documents({}) == 0):
            user_info = {"_id": author_id, "money": 0}
            collection.insert_one(user_info)

        if(collection.count_documents(user_id) == 0):
            user_info = {"_id": author_id, "money": 0}
            collection.insert_one(user_info)

        emoney = collection.find(user_id)
        for money in emoney:
            cur_money = money["money"]

            new_money = cur_money + randomnumber

        collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        embed = discord.Embed(title="Work Shift", description="Your work shift has ended!")
        embed.add_field(name="Message from boss!", value=f"{str(random.choice(responses))} {randomnumber}!")
        await ctx.reply(embed=embed)
        
    @commands.command()
    async def balance(self, ctx):
        mango_url = "mongodb+srv://dbUser:cyberguard@cluster0.25utt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        cluster = MongoClient(mango_url)
        db = cluster["CyberGuardBot"]
        collection = db["currency"]  
        author_id = ctx.author.id
        user_id = {"_id": author_id}
        emoney = collection.find(user_id)
        if(collection.count_documents({}) == 0):
            user_info = {"_id": author_id, "money": 0}
            collection.insert_one(user_info)

        if(collection.count_documents(user_id) == 0):
            user_info = {"_id": author_id, "money": 0}
            collection.insert_one(user_info)
        for money in emoney:
            cur_money = money["money"]
            embed = discord.Embed(title="Cash Balance", description="Here is your current cash!", color=0xfc0303)
            embed.add_field(name="Cash:", value=f"{cur_money}", inline=False)
            embed.add_field(name="Wallet:", value="nil",inline=False)
            embed.add_field(name="User:", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
            await ctx.reply(embed=embed)

    @commands.command()
    async def give(self, ctx, member: discord.Member, cash: int):
        mango_url = "mongodb+srv://dbUser:cyberguard@cluster0.25utt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        cluster = MongoClient(mango_url)
        db = cluster["CyberGuardBot"]
        collection = db["currency"]  
        author_id = ctx.author.id
        new_member = member.id
        user_id = {"_id": author_id}
        givemember = {"_id": new_member}
        old_owner = collection.find(user_id)
        new_owner = collection.find(givemember)

        if(collection.count_documents(givemember) == 0):
            user_info = {"_id": new_member, "money": 0}
            collection.insert_one(user_info)

        for minus in old_owner:
            cur_money = minus["money"]
            if cur_money < cash:
                return await ctx.channel.send("You don't have enough money!")
            if cur_money >= cash:
                new_money = cur_money - cash
                collection.update_one({"_id": author_id}, {"$set":{"money":new_money}}, upsert=True)
        
        for plus in new_owner:
            cur_money = plus["money"]
            new_money = cur_money + cash
            collection.update_one({"_id": new_member}, {"$set":{"money":new_money}}, upsert=True)
            await ctx.channel.send(f"Successfully sent {cash} to {member.mention}!")
    
    @commands.command()
    async def shop(self, ctx, page=1):
        if page==1:
            embed=discord.Embed(color=0xFF0000,title="Shop!", description="Here are all the items!")
            embed.add_field(name="Cent <:ItemCent:838121727032033350> -- ⚙ 1", value="Well uhh you don't have to be exactly rich to own this...")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(currencysys(client))
    