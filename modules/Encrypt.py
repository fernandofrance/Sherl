import hashlib
from discord.ext import commands

class Encrypt(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def encrypt(self, ctx, type: str, *, text: str):
        
        # Validates if hash type is valid
        type = type.upper()
        h = None
        supportedhashes = ["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512"]
        def validate_input(type):
            return type in supportedhashes
        if not validate_input(type):
            await ctx.send("`Invalid hash type.`")
        else:
            if type == "MD5":
                h = hashlib.md5()
            elif type == "SHA1":
                h = hashlib.sha1()
            elif type == "SHA224":
                h = hashlib.sha224()
            elif type == "SHA256":
                h = hashlib.sha256()
            elif type == "SHA384":
                h = hashlib.sha384()
            elif type == "SHA512":
                h = hashlib.sha512()

        # Results message with hash
            h.update(text.encode("utf-8"))
            result = h.hexdigest()
            print(f"Generated hash {type} for {text} --> {result}")
            await ctx.reply(f"Here is your hash ({type}): `{result}`")

def setup(client):
    client.add_cog(Encrypt(client))