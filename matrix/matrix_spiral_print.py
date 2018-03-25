#!/usr/bin/python

def print_topleft_bottomright(a, rows, cols, se_indx, string):
    i = j = se_indx

    # print top
    while j < cols:
        string += str(a[i][j]) + ' '
        j += 1
        #print "printed top"
    j -= 1
    i += 1

    #print "i =", i, " j =", j

    # print right
    while i < rows:
        string += str(a[i][j]) + ' '
        i += 1
        #print "printed right"
    i -= 1
    j -= 1

    #print "i =", i, " j =", j

    # print bottom
    while j > se_indx:
        string += str(a[i][j]) + ' '
        j -= 1
        #print "printed bottom"
    
    # print left
    while i > se_indx:
        string += str(a[i][j]) + ' '
        i -= 1
        #print "printed left"

    return string

def print_spiral(a):
    rows = len(a)
    cols = len(a[0])
    se_indx = 0
    string = ''

    while rows > se_indx and cols > se_indx:
        #print "Calling with rows =", rows, "cols =", cols, " se_indx=", se_indx
        string = print_topleft_bottomright(a, rows, cols, se_indx, string)
        rows -= 1
        cols -= 1
        se_indx += 1

    print string

def main():
    print "Given a matrix, print it in sprial order"
    #a = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]
    #a = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
    #a = [[1, 2, 3]] # NOT Working
    #a = [[1], [2]] # NOT Working
    a = [[1, 2], [3, 4], [5, 6], [7, 8]]

    """
    for i in range(len(a)):
        str = ''
        for j in range(len(a[0])):
            str += a[i][j] + ' '
        print str
    """

    print_spiral(a)

if __name__ == "__main__":
    main()