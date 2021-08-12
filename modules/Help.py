import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, *input: str):
        version = 1.0
        prefix = "." # Change this

        if not input:  
            help = discord.Embed(
                    title="Sherl",
                    url="https://github.com/sirfern4ndo/sherl",
                    description=f"You see but you don't observe.",
                    color=0xe87d8b
                )
            help.add_field(name="About", value="A Discord based toolkit for CTF/pentest.\nThis bot is developed by @Sir Fer of the Fernando³. Please visit https://github.com/sirfern4ndo/sherl to submit ideas or report bugs.")
            help.add_field(name="Currently prefix:", value=f"{prefix}", inline=False)
            help.add_field(name="Commands list", value="For now, this is what i can do:", inline=False)

            help.add_field(name="portscan", 
            value=f"Scan a host for open ports\nUsage: `{prefix}portscan scanme.nmap.org`\nor `portscan scanme.nmap.org 21 80 443` for specific ports.",
            inline=False
            )
            help.add_field(name="encrypt", 
            value=f"Creates a hash from text\nUsage: `{prefix}encrypt md5 i love my cat`\nSupported hashes: `MD5, SHA1, SHA224, SHA256, SHA384, SHA512`",
            inline=False
            )
            help.add_field(name="geoip", 
            value=f"Provides IP location\nUsage: `{prefix}geoip google.com`",
            inline=False
            )
            help.add_field(name="dirsearch", 
            value=f"Perform a brute-force attack for directories/files in webservers.\nUsage: `{prefix}dirsearch google.com\n# Don't use http://google.com/, instead use only google.com`",
            inline=False
            )

            help.set_footer(text=f"Sherl by Sir Fer of the Fernando³ • v{version} • https://github.com/sirfern4ndo", icon_url="https://avatars.githubusercontent.com/u/59847257?s=400&u=c784ce3daf1e3f50a0ce923149f526da06812d43&v=4")
            await ctx.send(embed=help)

def setup(client):
    client.add_cog(Help(client))

