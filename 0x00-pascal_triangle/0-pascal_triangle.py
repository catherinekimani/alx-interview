#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    # store rows of pascal's tri
    pascal_tri = []
    # iterate through each row idx
    for row_idx in range(n):
        # create new row with '1's
        row = [1] * (row_idx + 1)
        # check if curr row is greater than 1
        if row_idx > 1:
            # iterate through the cols of the curr row
            for col_idx in range(1, row_idx):
                # access previous row & update curr element(sum)
                prev_row = pascal_tri[row_idx - 1]
                row[col_idx] = prev_row[col_idx - 1] + prev_row[col_idx]
        # append curr row to the pascal's tri
        pascal_tri.append(row)
    # return pascal's tri
    return pascal_tri