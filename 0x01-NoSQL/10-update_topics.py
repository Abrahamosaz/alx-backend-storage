#!/usr/bin/env python3
"""
function that change all topics of a school document base
on the name argument
"""


def update_topics(mongo_collection, name, topics):
    """
    change all topics base on the name arg
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
