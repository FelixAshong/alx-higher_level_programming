#!/usr/bin/python3
"""
This prints the numbers from 1 to 100
multiples of three print Fizz
instead of the number and
multiples of five print Buzz
numbers which are multiples of both
three and five print FizzBuzz
"""


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
