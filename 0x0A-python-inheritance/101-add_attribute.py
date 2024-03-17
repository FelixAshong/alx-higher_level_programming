#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object if it’s possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
