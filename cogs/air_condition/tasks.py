# from discord.ext import tasks

from cogs import CogsExtension
from .utils import AirConditionUtils


class AirConditionTasks(CogsExtension):
    # variables
    def __init__(self, bot):
        super().__init__(bot)
        self.utils = AirConditionUtils(bot)

    # def cog_load(self):

    # def cog_unload(self):
