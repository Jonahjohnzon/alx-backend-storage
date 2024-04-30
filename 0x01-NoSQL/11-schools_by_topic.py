#!/usr/bin/env python3
"""
Top student
"""


def top_students(mongo_collection):
    """
    return students sorted by average score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
