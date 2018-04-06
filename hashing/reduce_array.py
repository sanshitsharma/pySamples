#!/usr/bin/python

'''
Given an array with n distinct elements, convert the given array to a form where all elements are in range from 0 to n-1.
The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, 
... n-1 is placed for largest element.

Input:  arr[] = {10, 40, 20}
Output: arr[] = {0, 2, 1}

Input:  arr[] = {5, 10, 40, 30, 20}
Output: arr[] = {0, 1, 4, 3, 2}
Expected time complexity is O(n Log n).

Ref: https://www.geeksforgeeks.org/convert-an-array-to-reduced-form-set-1-simple-and-hashing/ 

Solution:
Use hashing and sorting. 
```
Step 1: Create a hash which will store the index of the element
Step 2: Sort the array, using a sorting algorithm of your choice and store the result in a temp array
Step 3: For each a[i] in sorted array, get it's index from hash and start replacing with reduced values

To handle duplicates in the input array, store the indexes as a list in the index_map
'''

def reduce(a):
    index_map = {}

    # Step 1
    for i in range(len(a)):
        try:
            index_map[a[i]].append(i)
        except KeyError as ke:
            index_map[a[i]] = [i]
    
    # Step 2
    temp = sorted(a)

    reduced_value = 0
    # Step 3:
    for elem in temp:
        indexes = index_map[elem]
        for index in indexes:
            a[index] = reduced_value
        reduced_value += 1

    return a

if __name__ == "__main__":
    a = [5, 10, 40, 30, 20]
    print "Reduced Form:", reduce(a)