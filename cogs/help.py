
from logging import disable
import discord
from discord.ext import commands
from datetime import datetime
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

now = datetime.now()

class HelpCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(color=0xFF0000, name = "Commands Help", title = "						Commands")
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
		current_time = now.strftime("%H:%M")
		embed.set_footer(text=f"CyberGuard • Requested today at {current_time} • Page 1", icon_url="https://cdn.discordapp.com/avatars/814784481012482078/f4a22dcefba5aa59cfbcdaa6ba8e5e41.png")
		msg = await ctx.channel.send(embed=embed,
			components = [[Button(style=ButtonStyle.red, label="<", disabled=True), Button(style=ButtonStyle.blue, label="X"), Button(style=ButtonStyle.green, label=">")]],
		)
		while True:
			res1 = await self.client.wait_for("button_click")
			if res1.channel == ctx.channel and res1.user == ctx.author:
				if res1.component.label == ">":
					embed = discord.Embed(color=0xFF0000, name = "Commands Help", title = "						Commands")
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
					embed.set_footer(text=f"CyberGuard • Requested today at {current_time} • Page 2", icon_url="https://cdn.discordapp.com/avatars/814784481012482078/f4a22dcefba5aa59cfbcdaa6ba8e5e41.png")
					msg = await ctx.channel.edit(embed=embed, components = [[Button(style=ButtonStyle.red, label="<"), Button(style=ButtonStyle.blue, label="X"), Button(style=ButtonStyle.green, label=">", disabled=True)]],)
				if res1.component.label == "X":
					msg.edit("-- Closed --")
					print(msg)
				if res1.component.label == "<":
					embed = discord.Embed(color=0xFF0000, name = "Commands Help", title = "						Commands")
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
					current_time = now.strftime("%H:%M")
					embed.set_footer(text=f"CyberGuard • Requested today at {current_time} • Page 1", icon_url="https://cdn.discordapp.com/avatars/814784481012482078/f4a22dcefba5aa59cfbcdaa6ba8e5e41.png")
					msg = await ctx.channel.send(embed=embed,
						components = [[Button(style=ButtonStyle.red, label="<", disabled=True), Button(style=ButtonStyle.blue, label="X"), Button(style=ButtonStyle.green, label=">")]],
					)





def setup(client):
	client.add_cog(HelpCommand(client))

