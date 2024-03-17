#!/usr/bin/python3
for i in range(9):
    for a in range(i + 1, 10):
        if i != 8 or a != 9:
            print("{:n}{:n}".format(i, a), end=", ")
print("{:n}{:n}".format(i, a))
