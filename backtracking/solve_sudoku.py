#!/usr/bin/python

from itertools import *

cell_map = {0: [0, 2, 0, 2], 1: [0, 2, 3, 5], 2: [0, 2, 6, 8], 3: [3, 5, 0, 2], 4: [3, 5, 3, 5], 5: [3, 5, 6, 8], 6: [6, 8, 0, 2], 7: [6, 8, 3, 5], 8: [6, 8, 6, 8]}

'''
def get_cell_indices(r, c):
    i = r/3
    j = c/3

    return cell_map[3*i+j]
'''

def get_cell_members(brd, cell_id):
    r_min = cell_map[cell_id][0]
    r_max = cell_map[cell_id][1]
    c_min = cell_map[cell_id][2]
    c_max = cell_map[cell_id][3]

    members = []

    for r in range(r_min, r_max+1):
        for c in range(c_min, c_max+1):
            members.append(brd[r][c])

    return members

def is_distinct(lst):
    used = []
    for item in lst:
        if item == 0:
            continue

        if item in used:
            return False
        
        used.append(item)

    return True

def is_valid(brd):
    # Check all rows
    for i in range(len(brd)):
        row = [brd[i][j] for j in range(len(brd[0]))]
        #print "checking row:", row
        if not is_distinct(row):
            return False

    # Check all columns
    for i in range(len(brd[0])):
        col = [brd[j][i] for j in range(len(brd))]
        #print "checking col:", col
        if not is_distinct(col):
            return False

    # Check all cells
    for cell_id in cell_map:
        cell_members = get_cell_members(brd, cell_id)
        #print "checking cell:", cell_members
        if not is_distinct(cell_members):
            return False

    return True

def solve(brd, empties=81):
    if empties == 0:
        return is_valid(brd)

    for r, c in product(range(len(brd)), repeat=2):
        if brd[r][c] != 0:
            continue

        for choice in range(1, len(brd)+1):
            brd[r][c] = choice
            print "testing:", brd
            if is_valid(brd) and solve(brd, empties-1):
                return True

            print "invalid board... Backtracking", brd
            brd[r][c] = 0 #bracktrack

    return False

if __name__ == "__main__":
    brd = [[3, 2, 0, 6, 7, 0, 9, 5, 8], [5, 0, 0, 0, 4, 0, 6, 0, 2], [9, 6, 0, 8, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 5, 0, 4], [8, 5, 2, 0, 9, 0, 3, 7, 1], [4, 0, 7, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 8, 7, 0, 3, 6], [6, 0, 5, 0, 1, 0, 0, 0, 7], [7, 1, 3, 0, 6, 4, 0, 2, 5]]
    #print is_valid(brd)
    empties = 0
    for r, c in product(range(len(brd)), repeat=2):
        if brd[r][c] == 0:
            empties += 1

    res = solve(brd, empties)
    if res:
        for r in range(len(brd)):
            string = ''
            for c in range(len(brd[0])):
                string += str(brd[r][c]) + ' '
            print string
    else:
        print "no solution found for given board"