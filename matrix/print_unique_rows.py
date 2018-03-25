#!/usr/bin/python

"""
Given a binary matrix, print all unique rows of the given matrix.

Input:
	{0, 1, 0, 0, 1}
    {1, 0, 1, 1, 0}
    {0, 1, 0, 0, 1}
    {1, 1, 1, 0, 0}
Output:
	0 1 0 0 1 
	1 0 1 1 0 
	1 1 1 0 0 
"""

def print_unique_rows(mat):
    # Create a list which will contain the decimal number equivalent for the row
    lst = []

    # Read one row at a time, create the print string and also the decimal number
    for i in range(len(mat)):
        string = ''
        num = 0
        for j in range(len(mat[0])):
            string = string + str(mat[i][j]) + ' '
            num = (num << 1) | mat[i][j]
        try:
            lst.index(num)
        except ValueError as e:
            # If a value error is raised, then decimal number does not exist in list
            # So print the string and add the number to lst
            print string
            lst.append(num)

if __name__ == "__main__":
    mat = [[0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 1, 1, 0, 0]]
    print_unique_rows(mat)