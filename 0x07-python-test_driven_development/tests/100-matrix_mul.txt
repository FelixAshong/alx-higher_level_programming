>>> matrix_mul = __import__('100-matrix_mul').matrix_mul

#TypeError

    ### m_a and m_b must be a list

    >>> matrix_mul("Holberton", [1, 2, 3])
    Traceback (most recent call last):
    TypeError: m_a must be a list

    >>> matrix_mul("Holberton", [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a must be a list

    >>> matrix_mul([1, 2, 3], "School")
    Traceback (most recent call last):
    TypeError: m_b must be a list

    >>> matrix_mul([[1, 2], [3, 4]], "School")
    Traceback (most recent call last):
    TypeError: m_b must be a list

    >>> matrix_mul("Holberton", "School")
    Traceback (most recent call last):
    TypeError: m_a must be a list

    ### m_a and m_b must be a list of lists

    >>> matrix_mul([2, 4], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

    >>> matrix_mul([[1, 2], [3, 4]], [2, 4])
    Traceback (most recent call last):
    TypeError: m_b must be a list of lists

    >>> matrix_mul([1, 2], [3, 4])
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

    ### all elements in m_a and m_b must be integers or floats

    >>> matrix_mul([[1, 2], [3, '4']], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, '4']])
    Traceback (most recent call last):
    TypeError: m_b should contain only integers or floats

    ### each row of m_a and m_b must be of the same size

    >>> matrix_mul([[1, 2], [3, 4, 5]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: each row of m_a must be of the same size

    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4, 5]])
    Traceback (most recent call last):
    TypeError: each row of m_b must be of the same size

    ### other cases

    >>> matrix_mul()
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 2 required positional arguments: 'm_a' and 'm_b'

    >>> matrix_mul(None)
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'

    >>> matrix_mul([[1, 2], [3, 4]])
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 1 required positional argument: 'm_b'



#ValueError

    ### m_a and m_b must be not empty

    >>> matrix_mul([], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

    >>> matrix_mul([[]], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ValueError: m_a can't be empty

    >>> matrix_mul([[1, 2], [3, 4]], [])
    Traceback (most recent call last):
    ValueError: m_b can't be empty

    >>> matrix_mul([[1, 2], [3, 4]], [[]])
    Traceback (most recent call last):
    ValueError: m_b can't be empty

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6]])
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied



#General Case

    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    >>> matrix_mul([[1, 2], [3, 4]], [[5.5, 6.6], [7.7, 8.8]])
    [[20.9, 24.200000000000003], [47.3, 55.0]]

    >>> matrix_mul([[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]])
    [[22.990000000000002, 26.620000000000005], [52.03, 60.5]]
