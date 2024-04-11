from discord.ext import commands

from .cmd import AirConditionCMD


async def setup(bot: commands.Bot):
    await bot.add_cog(AirConditionCMD(bot))


async def teardown(bot: commands.Bot):
    await bot.remove_cog("AirConditionCMD")
