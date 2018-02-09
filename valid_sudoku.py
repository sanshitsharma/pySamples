#!/usr/bin/python

def map_contains(m, k, elem):
    #print m
    if not m.has_key(k):
        return False
       
    if m[k] is None:
        return False

    values = m[k]
    for v in values:
        if elem == v:
            return True

    return False


def map_insert(m, k, elem):
    if not m.has_key(k):
        m[k] = [elem]
        return

    m[k].append(elem)
    
def is_valid_sudoku(a):
    row_map = {}
    col_map = {}
    cube_map = {}

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == '.':
                continue
            
            cube_id = (i/3 * 3) + j/3
            if map_contains(row_map, i, a[i][j]) or map_contains(col_map, j, a[i][j]) or map_contains(cube_map, cube_id, a[i][j] ):
                return False
            
            # Insert to maps
            map_insert(row_map, i, a[i][j])
            map_insert(col_map, j, a[i][j])
            map_insert(cube_map, cube_id, a[i][j])
    
    return True

def main():
    print "check if a given sudoku is valid or not"

    mat = [[4, 3, 5, 2, 6, 9, 7, 8, 1], [6, 8, 2, 5, 7, 1, 4, 9, 3], [1, 9, 7, 8, 3, 4, 5, 6, 2], [8, 2, 6, 1, 9, 5, 3, 4, 7], [3, 7, 4, 6, 8, 2, 9, 1, 5], [9, 5, 1, 7, 4, 3, 6, 2, 8], [5, 1, 9, 3, 2, 6, 8, 7, 4], [2, 4, 8, 9, 5, 7, 1, 3, 6], [7, 6, 3, 4, 1, 8, 2, 5, 9]]
    #mat = [[5, 3, '.', '.', 7, '.', '.', '.', '.'], [6, '.', '.', 1, 9, 5, '.', '.', '.'], ['.', 9, 8, '.', '.', '.', '.', 6, '.'], [8, '.', '.', '.', 6, '.', '.', '.', 3], [4, '.', '.', 8, '.', 3, '.', '.', 1], [7, '.', '.', '.', 2, '.', '.', '.', 6], ['.', 6, '.', '.', '.', '.', 2, 8, '.'], ['.', '.', '.', '.', 8, '.', '.', 7, 9]]
    """
    for i in range(len(mat)):
        string = ''
        for j in range(len(mat[0])):
            string += str(mat[i][j]) + ' '
        print string
    """

    print is_valid_sudoku(mat)

if __name__ == "__main__":
    main()