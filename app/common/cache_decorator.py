# src/utils/cache_decorator.py

import json
import functools
from typing import Callable
from app.db.redis_client import RedisClient
from app.config.settings import aplication_settings as settings

def redis_cache(cache_key_prefix: str, ttl: int = 600) -> Callable:
    """ A decorator to cache the result of a function in Redis.
    
    Args:
        cache_key_prefix (str): The prefix for the Redis cache key.
        ttl (int): Time-to-live for the cache in seconds.
    
    Returns:
    A decorator function.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{cache_key_prefix}:{args[1].symbol.lower()}"
            redis_client = RedisClient.get_client()

            cached_data = redis_client.get(cache_key)
            if cached_data:
                return json.loads(cached_data)

            result = func(*args, **kwargs)

            redis_client.setex(cache_key, ttl or settings.redis_cache_tll, json.dumps(result))
            return result

        return wrapper

    return decorator
