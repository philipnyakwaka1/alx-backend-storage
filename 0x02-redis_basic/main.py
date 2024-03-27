#!/usr/bin/env python3
"""
Main file
"""

from exercise import Cache
cache = Cache()

TEST_CASES = {
    b"1": None,
    123: int,
    "3": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    c = Cache()
    key = c.store(value)
    s = c.get_int(key)
    print(s, type(s))