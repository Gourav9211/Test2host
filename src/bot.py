
import asyncio
import os
import discord
from core import bot

async def main():
    """Main entry point for the bot"""
    try:
        # Start the bot
        await bot.start(bot.config.DISCORD_TOKEN)
    except KeyboardInterrupt:
        print("Bot shutdown requested by user")
    except discord.HTTPException as e:
        if e.status == 429:
            print("Rate limited by Discord. Please wait before restarting the bot.")
        else:
            print(f"Discord HTTP error: {e}")
    except Exception as e:
        print(f"Bot encountered an error: {e}")
    finally:
        # Only close if the bot was actually started
        if bot.is_ready():
            await bot.close()
        else:
            # If bot wasn't ready, force close connections
            try:
                await bot.close()
            except:
                pass

if __name__ == "__main__":
    asyncio.run(main())
