#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    argc = len(sys.argv)
    for i in range(1, argc):
        total += int(sys.argv[i])
    print(total)
