# for tortoise-orm
TORTOISE = {
    "connections": {"default": "sqlite://data.db"},
    "apps": {
        "models": {
            "models": ["aerich.models"],  # adjust to your actual models
            "default_connection": "default",
        }
    }
}

POSTGRESQL = {
    "connections": {"default": "sqlite://data.db"},  # or empty if not used
}
EXTENSIONS = (
    "cogs.events",
    "cogs.esports",
    "cogs.mod", 
    "cogs.premium",
    "cogs.quomisc",
    "cogs.reminder",
    "cogs.utility",
)

import os
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

COLOR = 0x00FFB3

FOOTER = "quo is lub!"

PREFIX = "q"

SERVER_LINK = ""

BOT_INVITE = ""

WEBSITE = ""

REPOSITORY = ""

DEVS = ()

# LOGS
SHARD_LOG = ""
ERROR_LOG = ""
PUBLIC_LOG = ""
