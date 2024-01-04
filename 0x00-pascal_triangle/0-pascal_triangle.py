#!/usr/bin/python3
""" Function representing Pascal's triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []
    pascal_tri = []
    for row_idx in range(n):
        row = [1] * (row_idx + 1)
        if row_idx > 1:
            for col_idx in range(1, row_idx):
                prev_row = pascal_tri[row_idx - 1]
                row[col_idx] = prev_row[col_idx - 1] + prev_row[col_idx]
        pascal_tri.append(row)
    return pascal_tri
