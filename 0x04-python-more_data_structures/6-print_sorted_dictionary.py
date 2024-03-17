#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary.keys()).sort()
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
