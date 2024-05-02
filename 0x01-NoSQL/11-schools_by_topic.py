#!/usr/bin/env python3
"""
Where?
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find specific value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
