from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core import Quotient

from discord.ext import tasks

import config
from core import Cog


class QuoTasks(Cog):
    def __init__(self, bot: Quotient):
        self.bot = bot

        self.insert_guilds.start()

    @tasks.loop(count=1)
    async def insert_guilds(self):
        for guild in self.bot.guilds:
            guild_data = {
                "prefix": config.PREFIX,
                "color": config.COLOR,
                "footer": config.FOOTER
            }
            await self.bot.db.set_guild_data(guild.id, guild_data)

    @insert_guilds.before_loop
    async def before_loops(self):
        await self.bot.wait_until_ready()
