#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if (m_a == [] or m_a == [[]]):
        raise ValueError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    "check if number of rows in m_a is equal to the number of columns in m_b"
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    "create a new null matrix with size columns of m_a and rows of m_b"
    m_c = []
    for i in range(len(m_a)):
        m_c.append([])
        for j in range(len(m_b[0])):
            m_c[i].append(0)

    "overwrite the entries of m_c with the product of m_a by m_b"
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
