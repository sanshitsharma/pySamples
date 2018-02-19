#!/usr/bin/python

from itertools import *

backtrack_count = 0

def is_valid(board, x, y):
    rows = len(board)
    cols = len(board[0])

    # Check row
    for j in range(cols):
        if board[x][j] == 1 and j != y:
            return False

    # Check col
    for i in range(rows):
        if board[i][y] == 1 and i != x:
            return False

    # Check diags:

    # Check bottom right
    i = x + 1
    j = y + 1
    while i < rows and j < cols:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    # Check bottom left
    i = x + 1
    j = y - 1
    while i < rows and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # Check top right
    i = x - 1
    j = y + 1
    while i >= 0 and j < cols:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Check top left
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    return True

def is_board_valid(board):
    for r, c in product(range(len(board)), repeat=2):
        if board[r][c] == 1 and not is_valid(board, r, c):
            return False

    return True

def solve(board, queens_left, r):
    if queens_left == 0:
        return is_board_valid(board)
    
    for c in range(len(board)):
        board[r][c] = 1
        if is_valid(board, r, c) and solve(board, queens_left - 1, r + 1):
            return True
        #global backtrack_count
        #backtrack_count += 1
        board[r][c] = 0 # backtrack

def place_queens(board):
    queens_left = len(board)
    row = 0

    return solve(board, queens_left, row)

if __name__ == "__main__":
    #board = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
    #board = [[0,0], [0,0]]
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # 4 Queens
    #board = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] # 6 Queens
    #board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]] # 8 queens

    res = place_queens(board)
    #print "Backtrack Count =", backtrack_count
    if res:
        for r in range(len(board)):
            string = ''
            for c in range(len(board[0])):
                string += str(board[r][c]) + ' '
            print string
    else:
        print "no solution found"