#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        new.append(0)
    len1 = len(my_list_1)
    len2 = len(my_list_2)
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new[i] = result
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except IndexError:
                print("out of range")
            except TypeError:
                print("wrong type")
    finally:
        return new
