#!/usr/bin/env python3
"""
This module defines Cache class that provides methods to
manage data the redis database
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    This class provides methods to manage data in a Redis database.
    The Redis database is flushed each time a new instance is created.
    """
    def __init__(self) -> None:
        """Initializes an instance of Redis client and flushes the
        instance using flushdb
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """
        Store an instance of the Redis client as a private variable and
        flushes the redis database
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id
