#!/usr/bin/python3
def max_integer(my_list=[]):
    "finds the biggest integer of a list"

    "if the list is empty, return None"
    if len(my_list) == 0:
        return (None)

    "find biggest int"
    biggest = my_list[0]
    for i in range(len(my_list)):
        if biggest < my_list[i]:
            biggest = my_list[i]

    return (biggest)
