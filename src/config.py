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
EXTENSIONS = ()

DISCORD_TOKEN = "MTM5MjU1NDI4MzkwNzQyMDE2MA.GK9YcE.LyDpx4EruGw2j6pSpWaSxZTJ1oR2eMMDWT1qo4"

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
