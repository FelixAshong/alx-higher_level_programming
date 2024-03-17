#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    "finds all multiples of 2 in a list"

    multiples = []
    "append True or False in the new list, depending if i is a multiple of 2"
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
