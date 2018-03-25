#!/usr/bin/python

"""
Given k sorted arrays of size n each, merge them and print the sorted output.

Example:

Input:
k = 3, n =  4
arr[][] = { {1, 3, 5, 7},
            {2, 4, 6, 8},
            {0, 9, 10, 11}} ;

Output: 0 1 2 3 4 5 6 7 8 9 10 11 
"""

"""
Solution:

1. Create a MIN heap of size k and insert the first element of each array into the heap
2. Repeat the following steps n*k times
    i. Get MIN from heap and add to output array
    ii. Insert the next element from the array which the MIN belonged to into MIN heap. If not element exists, add INF
    iii. Heapify
"""

from ds.PriorityQueue import PriorityQueue

INF = float("inf")

def merge_k_sorted(arrays):
    k = len(arrays)
    n = len(arrays[0])
    
    # I will use my implementation of priority queues as I can store complex objects in it
    pq = PriorityQueue()

    # Get first elements from each of the k subarrays and add them to pq
    for indx in range(k):
        elem = arrays[indx][0]
        # Insert to pq. Set the priority as elem value and data as k, the subbarray number
        pq.add(elem, indx)

    next_indx = [1, 1, 1]
    output_arr = []
    # Now basically we keep extracting min from heap and keep adding the next number from the 
    # proper sub-array until we consume all elements
    for indx in range(n*k):
        (elem, k_value) = pq.remove()

        # Append MIN element to output array
        if elem == INF:
            continue
 
        output_arr.append(elem)

        # Add the next element from k_value array into the heap
        next_elem_indx = next_indx[k_value]
        next_indx[k_value] = next_indx[k_value] + 1
        
        if next_elem_indx < len(arrays[k_value]):
            pq.add(arrays[k_value][next_elem_indx], k_value)
        else:
            pq.add(INF, k_value)

    return output_arr

if __name__ == "__main__":
    arrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
    sorted_arr = merge_k_sorted(arrays)
    print sorted_arr