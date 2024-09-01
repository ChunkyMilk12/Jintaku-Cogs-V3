from .booru import Booru

async def setup(bot):
    await bot.add_cog(Booru())
