from discord.ext import commands

from .cmd import FanCMD


async def setup(bot: commands.Bot):
    await bot.add_cog(FanCMD(bot))


async def teardown(bot: commands.Bot):
    await bot.remove_cog("FanCMD")
