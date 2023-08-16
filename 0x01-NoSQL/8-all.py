#!/usr/bin/python3
"""
function that list all documents in a collection
"""


def list_all(mongo_collection):
    """
    Take a collection as arg and list all
    the documents in the collection
    """
    return mongo_collection.find()
