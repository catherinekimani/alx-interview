#!/usr/bin/python3
""" N queens """
import sys


def is_safe(board, row, col, n):
    """ check if its safe to place a queen on the board """
    for idx in range(row):
        if board[idx] == col or  \
           board[idx] - idx == col - row or \
           board[idx] + idx == col + row:
            return False
    return True


def print_sol(board):
    """ solution """
    print([[idx, board[idx]] for idx in range(len(board))])


def solve_nqueens(board, row, n):
    """ solve """
    if row == n:
        print_sol(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """ input check """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
