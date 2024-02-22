#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """ rotate matrix 90 degrees clockwise """
    n = len(matrix)
    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in range(n):
            matrix[row].reverse()
