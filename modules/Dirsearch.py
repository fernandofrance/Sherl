import requests
import discord
from discord.ext import commands

class Dirsearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dirsearch(self, ctx, rhost: str):

        # Checks if directory exists
        def request(host, directory):
            try:
                response = requests.get("http://" + host + "/" + directory).status_code
                if response == 200:
                    print(f"Directory found -> http://{host}/{directory}")
            except Exception:
                print("An unexpected error occured.")

        wordlist = map(str.strip, open("wordlist.txt").readlines())

        # Performs a loop for directory wordlist
        def scan():
            found = []
            for i in wordlist:
                print("Testing " + i)
                request(rhost, i)
                found.append(i)
            print("Scan complete")
            print(found)
            return found
        
        # Results message
        results = str(scan())[1:-1]

        emb = discord.Embed(
            title="Directory Search",
            description=f"Finished directory search for {rhost}."
        )
        emb.add_field(name="Paths found", value=f"`{results}`", inline=True)

        scan()
        await ctx.send(embed=emb)



def setup(client):
    client.add_cog(Dirsearch(client))