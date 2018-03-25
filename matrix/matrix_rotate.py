#!/usr/bin/python

def swap_mirrors(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def rotate_clockwise(matrix):
    reverse_on_rows(matrix)
    swap_mirrors(matrix)

def rotate_anticlockwise(matrix):
    reverse_on_cols(matrix)
    swap_mirrors(matrix)

def reverse_on_rows(a):
    rows = len(a)
    cols = len(a[0])
    l = 0
    h = rows - 1

    while l < h:
        for j in range(cols):
            a[l][j], a[h][j] = a[h][j], a[l][j]
        l += 1
        h -= 1

def reverse_on_cols(a):
    l = 0
    h = len(a[0]) - 1

    while l < h:
        for i in range(len(a)):
            a[i][l], a[i][h] = a[i][h], a[i][l]
        l += 1
        h -= 1

def main():
    print "Given a 2D nxn matrix, rotate it 90 deg in place"
    #a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    rotate_clockwise(a)
    for i in range(len(a)):
        string = ''
        for j in range(len(a)):
            string += str(a[i][j]) + ' '
        print string
    print

    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_anticlockwise(a)
    for i in range(len(a)):
        string = ''
        for j in range(len(a)):
            string += str(a[i][j]) + ' '
        print string

if __name__ == "__main__":
    main()