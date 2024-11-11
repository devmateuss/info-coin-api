import redis
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
            try:
                redis_client = RedisClient.get_client()
                cached_data = redis_client.get(cache_key)
                if cached_data:
                    return json.loads(cached_data)
            except (redis.ConnectionError, redis.TimeoutError) as e:
                print(f"Redis connection error: {e}. Proceeding without cache.")
            result = func(*args, **kwargs)
            try:
                if redis_client:
                    redis_client.setex(cache_key, ttl or settings.redis_cache_ttl, json.dumps(result))
            except (redis.ConnectionError, redis.TimeoutError) as e:
                print(f"Redis connection error on setting cache: {e}. Result not cached.")

            return result

        return wrapper

    return decorator
