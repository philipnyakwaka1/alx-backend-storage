#!/usr/bin/env python3
"""
This modules defines function that lists all
documents in a collection:
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    "This unction that lists all documents in a collection"
    return list(mongo_collection.find())
