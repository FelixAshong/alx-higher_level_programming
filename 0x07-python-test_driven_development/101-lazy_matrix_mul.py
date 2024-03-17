#!/usr/bin/python3
"""multiplies 2 matrices by using the module NumPy."""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""
    return (numpy.matmul(m_a, m_b))
