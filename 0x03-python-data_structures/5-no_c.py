#!/usr/bin/python3
def no_c(my_string):
    new_ = ""
    for i in my_string:
        if i not in "cC":
            new_ += i
    return (new_)
