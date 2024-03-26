#!/usr/bin/env python3
"""
This module defines function that returns the
list of school having a specific topic:
"""


def schools_by_topic(mongo_collection, topic):
    """
    This function that returns the list of school
    having a specific topic:
    """
    return mongo_collection.find({'topics': topic})
