import os
import discord
from dotenv.main import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix=".")

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
async def reload(ctx):
    print("[+] Reloading modules...")
    for filename in os.listdir('./modules'):
        if filename.startswith('_'):
            continue
        if filename.endswith('.py'):
            client.reload_extension(f'modules.{filename[:-3]}')
            print(f'-> {filename[:-3]} reloaded')
        else:
            print(f'Unable to load {filename[:-3]}')
    print("[+] Modules reloaded successfully.")
    await ctx.send("`Modules reloaded successfully.`")

load_dotenv() # Insert your token in the .env file or replace the function below with client.run("token")
client.run(os.getenv("DISCORD_TOKEN")) # and remove the dotenv functions.