#!/usr/bin/env python3
"""
This module defines a function that tracks how many times
a particular url was accessed and caches the result
"""

import redis
import requests


def get_page(url: str) -> str:
    """
    This function that tracks how many times
    a particular url was accessed and caches the result
    """
    r = redis.Redis()
    r.incr(f'count:{url}', 1)
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode('utf-8')
    response = requests.get(url)
    r.setex(url, 10, response.text)
    return response.text
