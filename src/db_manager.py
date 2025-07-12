
import os
import json
import asyncio
from typing import Any, Dict, Optional
from replit import db

class ReplitDBManager:
    """Manager for Replit Key-Value Database operations"""
    
    def __init__(self):
        self.db = db
    
    async def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the database"""
        try:
            return self.db.get(key, default)
        except Exception:
            return default
    
    async def set(self, key: str, value: Any) -> None:
        """Set a value in the database"""
        self.db[key] = value
    
    async def delete(self, key: str) -> None:
        """Delete a key from the database"""
        if key in self.db:
            del self.db[key]
    
    async def exists(self, key: str) -> bool:
        """Check if a key exists"""
        return key in self.db
    
    async def get_guild_data(self, guild_id: int) -> Dict[str, Any]:
        """Get guild data"""
        key = f"guild:{guild_id}"
        default_data = {
            "prefix": "q",
            "color": 0x00FFB3,
            "footer": "Quotient Bot",
            "is_premium": False
        }
        return await self.get(key, default_data)
    
    async def set_guild_data(self, guild_id: int, data: Dict[str, Any]) -> None:
        """Set guild data"""
        key = f"guild:{guild_id}"
        await self.set(key, data)
    
    async def get_user_data(self, user_id: int) -> Dict[str, Any]:
        """Get user data"""
        key = f"user:{user_id}"
        default_data = {
            "votes": 0,
            "premium": False
        }
        return await self.get(key, default_data)
    
    async def set_user_data(self, user_id: int, data: Dict[str, Any]) -> None:
        """Set user data"""
        key = f"user:{user_id}"
        await self.set(key, data)
    
    async def get_scrim_data(self, scrim_id: str) -> Optional[Dict[str, Any]]:
        """Get scrim data"""
        key = f"scrim:{scrim_id}"
        return await self.get(key)
    
    async def set_scrim_data(self, scrim_id: str, data: Dict[str, Any]) -> None:
        """Set scrim data"""
        key = f"scrim:{scrim_id}"
        await self.set(key, data)
    
    async def get_tourney_data(self, tourney_id: str) -> Optional[Dict[str, Any]]:
        """Get tournament data"""
        key = f"tourney:{tourney_id}"
        return await self.get(key)
    
    async def set_tourney_data(self, tourney_id: str, data: Dict[str, Any]) -> None:
        """Set tournament data"""
        key = f"tourney:{tourney_id}"
        await self.set(key, data)
    
    async def execute(self, query: str, *args) -> None:
        """Compatibility method for raw SQL queries - converts to key-value operations"""
        # This is a simplified compatibility layer
        # You'll need to adapt your specific queries to key-value operations
        pass
    
    async def fetchval(self, query: str, *args) -> Any:
        """Compatibility method for fetchval - returns simple test value"""
        if "SELECT 1" in query:
            return 1
        return None
