#!/usr/bin/python

'''
Given a nxm matrix, return the sum of the a sub matrix axb such that a <= n
b <= m

Original matrix is static
Support multiple queries on that original matrix
'''

import numpy as np 

class Solution(object):
    def __init__(self, mat):
        self.mat = mat
        self.__preprocess()

    def __repr__(self):
        return str(self.mat)

    def __preprocess(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    self.mat[i][j] += self.mat[i][j-1]
                elif j == 0:
                    self.mat[i][j] += self.mat[i-1][j]
                else:
                    self.mat[i][j] += self.mat[i-1][j] + self.mat[i][j-1] - self.mat[i-1][j-1]

        return
    
    def rectangleSum(self, upperLeft, bottomRight):
        return self.getSum(bottomRight[0], bottomRight[1]) + self.getSum(upperLeft[0]-1, upperLeft[1]-1) - self.getSum(bottomRight[0], upperLeft[1]-1) - self.getSum(upperLeft[0]-1, bottomRight[1])


    def getSum(self, i, j):
        if i < 0 or j < 0:
            return 0

        return self.mat[i][j]

def printMat(a):
    for i in range(len(a)):
        s = ''
        for j in range(len(a[0])):
            s += str(a[i][j]) + ' '
        print s

if __name__ == "__main__":
    #m = [[1, 2, 5], [4, 3, 1], [2, 5, 4]]
    m = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    printMat(m)
    
    obj = Solution(m)
    print "Preprocessed matrix:"#, obj
    printMat(obj.mat)

    uL = (1,1)
    bR = (2,2)
    print "Sum of rectangle", uL, "and", bR, "=", obj.rectangleSum(uL, bR)

    uL = (0,0)
    bR = (2,2)
    print "Sum of rectangle", uL, "and", bR, "=", obj.rectangleSum(uL, bR)

    uL = (0,0)
    bR = (2,0)
    print "Sum of rectangle", uL, "and", bR, "=", obj.rectangleSum(uL, bR)

    uL = (0,1)
    bR = (1,2)
    print "Sum of rectangle", uL, "and", bR, "=", obj.rectangleSum(uL, bR)

