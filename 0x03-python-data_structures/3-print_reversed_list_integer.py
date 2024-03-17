#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    "prints all integers of a list, in reverse order"
    if my_list:
        for n in range(0, len(my_list)):
            print("{:d}".format(my_list[(-n) - 1]))
