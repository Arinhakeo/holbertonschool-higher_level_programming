#!/usr/bin/python3
"""
This is a module for matrix operations.
It contains a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list): List of lists containing int or float
        div (int or float): Number to divide matrix by

    Returns:
        list: New matrix with elements divided by div

    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(err_msg)

    if not all(isinstance(num, (int, float))
               for row in matrix for num in row):
        raise TypeError(err_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
