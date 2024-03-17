#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """invert operators == and !="""

    def __eq__(self, operator):
        """invert operator == with !="""
        return int(self) != operator

    def __ne__(self, operator):
        """invert operator != with =="""
        return int(self) == operator
