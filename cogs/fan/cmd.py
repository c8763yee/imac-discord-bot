from typing import Literal, Optional

import discord
from discord.ext import commands, has_permissions

from loggers import setup_package_logger

from .tasks import FanTasks
from .utils import FanPosition
logger = setup_package_logger(__name__)


class FanCMD(FanTasks):
    @commands.hybrid_group(ephemeral=True)
    async def fan(self, ctx: commands.Context):
        pass

    @fan.command("on")
    @has_permissions(administrator=True)
    async def fan_on(self, ctx: commands.Context, fan_position: FanPosition):
        await ctx.send(await self.utils.turn_on(fan_position))

    @fan.command("off")
    @has_permissions(administrator=True)
    async def fan_off(self, ctx: commands.Context, fan_position: FanPosition):
        await ctx.send(await self.utils.turn_off(fan_position))
