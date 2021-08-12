import discord
import socket
from discord.ext import commands

class Portscan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def portscan(self, ctx, addr: str, *p: int):
        message = await ctx.send("Wait a minute...")

        # Checks if has a specific port to scan
        ports = []
        if not p:
            ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
        else:
            ports = p

        openports = []
        ip = socket.gethostbyname(addr)

        async def scan(addr, p):
            print(f"Starting portscanning for {addr} ({ip})")

            # Connects to port to check if it's open  
            try:
                for port in ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(3)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        print(f"Port {port} open.")
                        await message.edit(content=f"`Scanning... Port {port} on {ip} is open.`")
                        openports.append(port)
                    else: 
                        print(f"Port {port} is closed or behind a firewall.")
                        await message.edit(content=f"`Scanning... Port {port} on {ip} is closed or behind a firewall.`")
                print(f"Finished portscanning for {addr}")

                # Checks if has any open port in scan result
                if not openports:
                    return " All ports are closed or blocked by firewall "
                else:
                    return openports

            # Error handling
            except socket.gaierror:
                print("Couldn't resolve the host.")
                await ctx.send("Sorry, i couldn't resolve the host.")
            except socket.error:
                print("Can't connect to server.")
                await ctx.send("It seems i can't connect to server.")
        
        # Results message
        scanresult = await scan(ip, ports)
        results = str(scanresult)[1:-1]

        emb = discord.Embed(
            description=f"Finished portscanning for {addr} ({ip})."
        )
        emb.add_field(name="Open ports", value=results)
        emb.set_footer(text=f"{ctx.message.author.name}#{ctx.message.author.discriminator}")
        await message.edit(content="Here is my report, Watson:", embed = emb)

def setup(client):
    client.add_cog(Portscan(client))