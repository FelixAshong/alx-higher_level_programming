#!/usr/bin/python3
"""inheritance from list"""


class MyList(list):
    """ print_sorted version of list"""
    def print_sorted(self):
        print(sorted(self))
