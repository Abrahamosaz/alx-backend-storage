#!/usr/bin/python3
"""
insert a document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    function insert new documents in a collection
    base on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
