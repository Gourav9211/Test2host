
import asyncio
import os
from core import bot

async def main():
    """Main entry point for the bot"""
    try:
        # Start the bot
        await bot.start(bot.config.DISCORD_TOKEN)
    except KeyboardInterrupt:
        print("Bot shutdown requested by user")
    except Exception as e:
        print(f"Bot encountered an error: {e}")
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
