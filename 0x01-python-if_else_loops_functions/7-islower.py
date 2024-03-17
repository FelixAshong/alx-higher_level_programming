#!/usr/bin/python3
"""
This checks for lowercase character
"""


def islower(c):
    for i in range(ord('a'), ord('{')):
        if i == ord(c):
            return True
    return False
