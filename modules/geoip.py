import discord
import requests
from discord.ext import commands

class GeoIP(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def geoip(self, ctx, ip: str):

        # Request to GEO-IP API
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url)
        values = res.json()

        # Results message
        results = discord.Embed(
            description = f"GEO IP request for {ip} returned: "
        )
        results.add_field(name="Country", value=values["country"])
        results.add_field(name="Region", value=values["regionName"])
        results.add_field(name="City", value=values["city"])
        results.add_field(name="Latitude", value=values["lat"])
        results.add_field(name="Longitude", value=values["lon"])
        results.add_field(name="Timezone", value=values["timezone"])
        results.add_field(name="ISP", value=values["isp"])
        results.add_field(name="Organization", value=values["org"])
        results.add_field(name="AS", value=values["as"])
        if res.status_code == 200:
            await ctx.send(embed=results)
        else:
            await ctx.send(f"`Error {res.status_code}`")


def setup(client):
    client.add_cog(GeoIP(client))