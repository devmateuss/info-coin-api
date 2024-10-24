import redis
from app.config.settings import aplication_settings as settings

class RedisClient:
    """
    Singleton class for Redis client.
    """

    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = redis.Redis(
                host=settings.redis_host,
                port=settings.redis_port,
                db=0,
                decode_responses=True
            )
        return cls._client
