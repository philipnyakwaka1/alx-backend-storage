#!/usr/bin/env python3
"""
This module defines Cache class that provides methods to
manage data the redis database
"""
import redis
from typing import Union, Callable
import uuid
from functools import wraps


def replay(func):
    """display the history of calls of a particular function."""
    n = func.__qualname__
    inputs = n + ':inputs'
    outputs = n + ':outputs'
    r = redis.Redis()
    id_list = r.lrange(outputs, 0, -1)
    value_list = r.lrange(inputs, 0, -1)
    print(f'{n} was called {len(id_list)} times')
    for key, val in zip(id_list, value_list):
        print(f"{n}(*('{val.decode('utf-8')}')) -> {key.decode('utf-8')}")


def call_history(method) -> Callable:
    """decorator"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper"""
        inputs = method.__qualname__ + ':inputs'
        outputs = method.__qualname__ + ':outputs'
        self._redis.rpush(inputs, str(args))
        id = method(self, *args, **kwargs)
        self._redis.rpush(outputs, id)
        return id
    return wrapper


def get_decorator(f):
    "decorator for get function"
    @wraps(f)
    def wrapper(self, key: str, fn: Callable =
                None) -> Union[str, bytes, int, None]:
        """wrapper function for get_decorator"""
        value = f(self, key)
        if value is None:
            return None
        if fn:
            return fn(value)
        else:
            return value
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    This decorator implements a system to count how many times methods of
    the Cache class are called.
    """

    @wraps(method)
    def wrapper(self, *args,  **kwargs):
        """wrapper function for get_count decorator"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @call_history
    @count_calls
    def store(self, data: Union[int, float, str, bytes]) -> str:
        """
        Store an instance of the Redis client as a private variable
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    @get_decorator
    def get(self, key: str, fn: Callable =
            None) -> Union[str, bytes, int, None]:
        """
        This method retrieves value from redis database. The callable argument
        will be used to convert the data back to the desired format
        """
        return self._redis.get(key)

    def get_str(self, key: str) -> Union[str, None]:
        """returns a string"""
        value = self._redis.get(key)
        return value.decode('utf-8') if value is not None else None

    def get_int(self, key: str) -> Union[int, None]:
        """returns int"""

        value = self._redis.get(key)
        return int(value) if value is not None else None
