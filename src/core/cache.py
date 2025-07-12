from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

import config
from constants import IST
from models import Guild, EasyTag, TagCheck, Scrim, Tourney, AutoPurge, SSVerify, BlockList


class CacheManager:
    def __init__(self, bot):
        if TYPE_CHECKING:
            from .Bot import Quotient

        self.bot: Quotient = bot

        self.guild_data = {}
        self.eztagchannels = set()
        self.tagcheck = set()
        self.scrim_channels = set()
        self.tourney_channels = set()
        self.autopurge_channels = set()
        self.media_partner_channels = set()
        self.ssverify_channels = set()

        self.blocked_ids = set()

    async def fill_temp_cache(self):
        # Load guild data from Replit DB
        # For now, we'll just set up empty caches since we're migrating from Tortoise ORM
        # Guild data will be populated as needed when guilds are accessed
        
        # Initialize empty sets for various channel types
        # These will be populated from Replit DB as needed
        pass

    def guild_color(self, guild_id: int):
        return self.guild_data.get(guild_id, {}).get("color", config.COLOR)

    def guild_footer(self, guild_id: int):
        return self.guild_data.get(guild_id, {}).get("footer", config.FOOTER)

    async def update_guild_cache(self, guild_id: int, *, set_default=False) -> None:
        if set_default:
            await self.bot.db.set_guild_data(guild_id, {
                "prefix": config.PREFIX,
                "color": config.COLOR,
                "footer": config.FOOTER,
                "is_premium": False
            })

        guild_data = await self.bot.db.get_guild_data(guild_id)
        self.guild_data[guild_id] = {
            "prefix": guild_data.get("prefix", config.PREFIX),
            "color": guild_data.get("color", config.COLOR),
            "footer": guild_data.get("footer", config.FOOTER),
        }

    # @staticmethod
    # @cached(ttl=10, serializer=JsonSerializer())
    # async def match_bot_guild(guild_id: int, bot_id: int) -> bool:
    #     return await Guild.filter(pk=guild_id, bot_id=bot_id).exists()
