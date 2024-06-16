#!/usr/bin/env python3
"""
a Python function that inserts a new document in a collection based on kwargs:

Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    """
    insert_result = mongo_collection.insert_one(kwargs)
    return insert_result.inserted_id
