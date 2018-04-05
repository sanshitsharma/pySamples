#!/usr/bin/python

"""
Given an array of integers and a number k, write a function that returns true if given array can be divided into pairs
such that sum of every pair is divisible by k.

Examples:

Input: arr[] = {9, 7, 5, 3}, 
           k = 6
Output: True
We can divide array into (9, 3) and
(7, 5). Sum of both of these pairs 
is a multiple of 6.

Input: arr[] = {92, 75, 65, 48, 45, 35}, 
           k = 10
Output: True
We can divide array into (92, 48), (75, 65) 
and (45, 35). Sum of all these pairs is a
multiple of 10.

Input: arr[] = {91, 74, 66, 48}, k = 10
Output: False
"""
def sum_of_pairs_by_k(arr, k):
    if len(arr)%2 != 0:
        return False

    # Reduce all elements to there individual mod values with k
    for i in range(len(arr)):
        arr[i] = arr[i]%k

    # Now the problem is basically reduced to finding the a + b = k inequality
    itemMap = {}
    #res = []
    for a in arr:
        try:
            itemMap[k-a] -= 1
            #res.append((k-a, a))
            if itemMap[k-a] == 0:
                itemMap.pop(k-a)
        except:
            itemMap[a] = 1

    #print res
    return len(itemMap.keys()) == 0
    
if __name__ == "__main__":
    a = [91, 74, 66, 48]
    k = 10
    print sum_of_pairs_by_k(a, k)
