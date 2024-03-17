#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    "replaces an element of a list at a specific position."

    "if idx is negative or out of range, return None"
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
