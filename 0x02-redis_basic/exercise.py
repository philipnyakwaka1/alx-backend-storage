#!/usr/bin/env python3
"""
This module defines Cache class
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    Definantion of class Cache
    """
    def __init__(self) -> None:
        """Initializes a Cache object"""
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
