#!/usr/bin/env python3
"""Return the list of schools having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Return list of schools with the given topic"""
    return list(mongo_collection.find({"topics": topic}))
