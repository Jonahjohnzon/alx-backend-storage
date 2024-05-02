#!/usr/bin/env python3
"""
school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    changes topics of a school
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
