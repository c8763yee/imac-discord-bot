from typing import Optional

from discord.ext import commands

from loggers import setup_package_logger

from .tasks import AirConditionTasks

logger = setup_package_logger(__name__)


class AirConditionCMD(AirConditionTasks):
    @commands.hybrid_group(ephemeral=True)
    async def aircondition(self, ctx: commands.Context):
        pass

    @aircondition.command("on")
    @commands.has_permissions(administrator=True)
    async def aircondition_on(
        self, ctx: commands.Context, temperature: Optional[commands.Range[16, 30]] = 25
    ):
        await ctx.send(await self.utils.turn_on(temperature))

    @aircondition.command("off")
    @commands.has_permissions(administrator=True)
    async def aircondition_off(self, ctx: commands.Context):
        await ctx.send(await self.utils.turn_off())
