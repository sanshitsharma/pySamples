#!/usr/bin/python

from itertools import *

def is_distinct(lst):
    used = []
    for item in lst:
        if item == 0:
            continue
        
        if item in used:
            return False
        used.append(item)

    return True

def is_valid(grid):
    for i in range(len(grid)):
        row = [grid[i][j] for j in range(0, len(grid[0]))]
        #print "Checking Row:", row
        if not is_distinct(row):
            #print "in valid row:", row
            return False

    for i in range(len(grid[0])):
        col = [grid[j][i] for j in range(0, len(grid))]
        #print "Checking Col:", col
        if not is_distinct(col):
            #print "in valid col:", col
            return False

    return True

def solve(grid, empties=9):
    #print "empties:", empties
    if empties == 0:
        #print "non-empty grid:", grid
        return is_valid(grid)

    for row, col in product(range(len(grid)), repeat=2):
        if grid[row][col] != 0:
            continue
        for choice in range(1, len(grid)+1):
            grid[row][col] = choice
            #print "testing:", grid
            if is_valid(grid) and solve(grid, empties-1):
                return True
            #print "Grid:", grid, "is invalid.. BACKTRACKING"
            grid[row][col] = 0 #backtrack

    return False

'''
def print_row_col_cell(grid):
    for r, c in product(range(len(grid)), repeat=2):
        i = r/3
        j = c/3
        cell = 3*i + j

        print "Indx (" + str(r) + ", " + str(c) + "): Cell = " + str(cell)
'''

if __name__ == "__main__":
    grid = [[0, 2, 0], [3, 1, 0], [0, 3, 0]]
    #print_row_col_cell(grid)
    res = solve(grid, empties=5)
    if res:
        for r in range(len(grid)):
            string = ''
            for c in range(len(grid[0])):
                string += str(grid[r][c]) + ' '
            print string
    else:
        print "No valid solution for sudoku board"