import os
import discord
from dotenv.main import load_dotenv
from discord.ext import commands
from discord.ext.commands.core import has_permissions

# Set client as global variable to refer to our bot
# If you change the prefix, don't forget to change it in the "modules/Help.py" file too.
client = commands.Bot(command_prefix=".", case_insensitive=True) 

token = "" # Place your app token here.

# Removes the default help command from discord.py lib
client.remove_command("help")

# Set a message on terminal when the bot gets online and set activity in Discord
@client.event
async def on_ready():
    print("==========")
    print(f"[>] {client.user.name} has connected to Discord.")
    print(f"[>] Logged as: {client.user.name}#{client.user.discriminator}")
    print(f"[>] ID: {client.user.id}")
    print(f"[>] URL for invite: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot")
    print("==========")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you."))

# Loads the commands from the modules folder
for filename in os.listdir("./modules"):
    if filename.endswith(".py"):
        client.load_extension(f"modules.{filename[:-3]}")
        print(f"-> {filename[:-3]} loaded")
    elif filename.startswith("_"):
        continue
    else:
        print(f"[X] Unable to load {filename[:-3]}")
print("[+] Modules loaded successfully.")

# Command to reload modules
@client.command()
@has_permissions(administrator=True)
async def reload(ctx):
    print("[+] Reloading modules...")
    for filename in os.listdir("./modules"):
        if filename.startswith("_"):
            continue
        if filename.endswith(".py"):
            client.reload_extension(f"modules.{filename[:-3]}")
            print(f"-> {filename[:-3]} reloaded")
        else:
            print(f"Unable to load {filename[:-3]}")
    print("[+] Modules reloaded successfully.")
    await ctx.send("`Modules reloaded successfully.`")

client.run(token)