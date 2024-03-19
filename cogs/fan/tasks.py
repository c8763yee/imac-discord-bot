import datetime
import os

from discord.ext import tasks

from cogs import CogsExtension
from .utils import FanUtils


class FanTasks(CogsExtension):
    # variables
    def __init__(self, bot):
        super().__init__(bot)
        self.utils = FanUtils(bot)

    # def cog_load(self):

    # def cog_unload(self):


