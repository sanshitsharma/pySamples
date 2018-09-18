#!/usr/bin/python

'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform
the multiplications, but merely to decide in which order to perform the multiplications.

We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we
parenthesize the product, the result will be the same.
For example, if we had four matrices A, B, C, and D, we would have:

(ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product,
or the efficiency. For example, suppose A is a 10 x 30 matrix, B is a 30 x 5 matrix, and C is a 5 x 60 matrix. Then,
    (AB)C = (10x30x5) + (10x5x60) = 1500 + 3000 = 4500 operations
    A(BC) = (30x5x60) + (10x30x60) = 9000 + 18000 = 27000 operations.
Clearly the first parenthesization requires less number of operations.

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
We need to write a function MatrixChainOrder() that should return the minimum number of multiplications needed to multiply the chain.

  Input: p[] = {40, 20, 30, 10, 30}   
  Output: 26000  
  There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of 
  multiplications are obtained by putting parenthesis in following way
  (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

  Input: p[] = {10, 20, 30, 40, 30} 
  Output: 30000 
  There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
  Let the input 4 matrices be A, B, C and D.  The minimum number of 
  multiplications are obtained by putting parenthesis in following way
  ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

  Input: p[] = {10, 20, 30}  
  Output: 6000  
  There are only two matrices of dimensions 10x20 and 20x30. So there 
  is only one way to multiply the matrices, cost of which is 10*20*30

Ref: https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
'''
import numpy as np 
import sys

def MatrixChainOrder(p):
    n = len(p)
    m = np.ones([n, n], dtype=int)

    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                #print "L =", L, "i =", i, "j =", j, "k =", k, "q =", q
                if q < m[i][j]:
                    m[i][j] = q
    print m
    return m[1][n-1]

if __name__ == "__main__":
    p = [10, 20, 30, 40, 30]
    print MatrixChainOrder(p)