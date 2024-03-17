#!/usr/bin/python3
"""inheritance from list"""


def inherits_from(obj, a_class):
    """inherit"""
    if issubclass(type(obj), (a_class)) and type(obj) is not a_class:
        return True
    return False
