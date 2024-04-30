from discord.ext import commands

from loggers import setup_package_logger

from .tasks import FanTasks
from .utils import FanPosition

logger = setup_package_logger(__name__)


class FanCMD(FanTasks):
    @commands.hybrid_group(ephemeral=True)
    async def fan(self, ctx: commands.Context):
        pass

    @fan.command("on")
    @commands.has_permissions(administrator=True)
    async def fan_on(self, ctx: commands.Context, fan_position: FanPosition):
        await ctx.send(await self.utils.turn_on(fan_position))

    @fan.command("off")
    @commands.has_permissions(administrator=True)
    async def fan_off(self, ctx: commands.Context, fan_position: FanPosition):
        await ctx.send(await self.utils.turn_off(fan_position))

    @fan.command("stat")
    @commands.has_permissions(administrator=True)
    async def fan_stat(self, ctx: commands.Context, fan_position: FanPosition):
        await ctx.send(await self.utils.get_stat(fan_position))
