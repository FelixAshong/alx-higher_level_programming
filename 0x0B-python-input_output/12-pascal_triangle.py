#!/usr/bin/python3
"""contains pascal_triangle"""


def pascal_triangle(n):
    """Generates the pascal triangle"""
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        pascal.append(temp)
    for i in range(1, n + 1):
        for j in range(i):
            if j == 0:
                pascal[i - 1][j] = 1
            else:
                pascal[i - 1][j] = pascal[i - 2][j] + pascal[i - 2][j - 1]
    formatted = []
    for row in range(1, n + 1):
        temp = []
        for col in range(row):
            temp.append(pascal[row - 1][col])
        formatted.append(temp)
    return formatted
