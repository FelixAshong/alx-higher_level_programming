#!/usr/bin/python3
for i in range(ord('a'), ord('{')):
    if (i != 101 and i != 113):
        print("{:c}".format(i), end='')
