from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
import discord
from discord.ext import ipc

app = Quart(__name__)
ipc_client = ipc.Client(secret_key = "CyberGuard1999")

app.config["SECRET_KEY"] = "CyberGuard1999"
app.config["DISCORD_CLIENT_ID"] = 814784481012482078   # Discord client ID.
app.config["DISCORD_CLIENT_SECRET"] = "emdSrRwg29RhBja62heqIiHJpZCfQdQd"   # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "http://127.0.0.1:5000/callback"   

discord = DiscordOAuth2Session(app)

@app.route("/")
async def home():
	return await render_template("index.html")

@app.route("/login")
async def login():
	return await discord.create_session()

@app.route("/callback")
async def callback():
	try:
		await discord.callback()
	except:
		return redirect(url_for("login"))

	user = await discord.fetch_user()
	return redirect(url_for("dashboard")) #f"User: {user.name}#{user.discriminator} Email: {user.email}" #You should return redirect(url_for("dashboard")) here

@app.route("/dashboard")
async def dashboard():
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild_count = await ipc_client.request("get_guild_count")
	guild_ids = await ipc_client.request("get_guild_ids")

	user_guilds = await discord.fetch_guilds()

	guilds = []

	for guild in user_guilds:
		if guild.permissions.manage_guild:			
			guild.class_color = "green-border" if guild.id in guild_ids else "red-border"
			guilds.append(guild)

	guilds.sort(key = lambda x: x.class_color == "red-border")
	name = (await discord.fetch_user()).name
	user = await discord.fetch_user()
	return await render_template("dashboard.html", guild_count = guild_count, guilds = guilds, username=name, user_id=user.id)

@app.route("/info")
async def info():
	guild_count = await ipc_client.request("get_guild_count")
	user = await discord.fetch_user()
	return await render_template("info.html", guild_count = guild_count)

@app.route("/terms-of-service")
async def tos():
	return await render_template("tos.html")

@app.route("/dashboard/<int:guild_id>")
async def dashboard_server(guild_id):
	if not await discord.authorized:
		return redirect(url_for("login")) 

	guild = await ipc_client.request("get_guild", guild_id = guild_id)
	if guild is None:
		return redirect(f'https://discord.com/oauth2/authorize?&client_id={app.config["DISCORD_CLIENT_ID"]}&scope=bot&permissions=4294832119&guild_id={guild_id}&response_type=code&redirect_uri={app.config["DISCORD_REDIRECT_URI"]}')
	return guild["name"]

if __name__ == "__main__":
	app.run(debug=True)