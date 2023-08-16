#!/usr/bin/env python3
"""
function that return a list of school having a specific topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    return a list of documents having a specific topics
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
