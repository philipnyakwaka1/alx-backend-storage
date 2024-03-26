#!/usr/bin/env python3
"""
This module defines function that inserts a new
document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    This is a function that inserts a new document in a
    collection based on kwargs
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
