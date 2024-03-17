#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary.copy():
        if a_dictionary[i] is value:
            a_dictionary.pop(i)
    return a_dictionary
