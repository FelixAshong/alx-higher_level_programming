#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as error:
        print("Exception: {}".format(str(error)), file=sys.stderr)
    return result
