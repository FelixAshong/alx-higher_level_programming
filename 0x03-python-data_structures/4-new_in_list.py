#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    "replaces an element in a list at idx without modifying the original list"

    my_list_copy = my_list[:]
    "if idx is negative or out of range, return a copy of the original list"
    if idx < 0 or idx >= len(my_list):
        return (my_list_copy)
    my_list_copy[idx] = element
    return (my_list_copy)
