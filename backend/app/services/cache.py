from __future__ import annotations

import redis

from app.core.config import settings


class CacheService:
    def __init__(self):
        self.client = redis.Redis.from_url(settings.redis_url, decode_responses=True)

    def get(self, key: str):
        try:
            value = self.client.get(key)
            if value is None:
                return None
            import json
            return json.loads(value)
        except Exception:
            return None

    def set(self, key: str, value, ttl: int = 300):
        try:
            import json
            self.client.set(key, json.dumps(value), ex=ttl)
        except Exception:
            pass


cache_service = CacheService()
