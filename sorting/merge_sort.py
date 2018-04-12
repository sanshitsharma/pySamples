#!/usr/bin/env python

def merge(a, l, mid, r):
    n1 = mid - l + 1
    n2 = r - mid

    # Create two arrays of size n1 and n2
    L = [0] * n1
    R = [0] * n2

    # Copy data
    for i in range(n1):
        L[i] = a[l+i]

    for i in range(n2):
        R[i] = a[mid+1+i]

    # Sort and put in original array
    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:
        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # Add any remaining element of L to a
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    # Add remaining elements of R to a
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def merge_sort_recurse(a, l, r):
    if l < r:
        mid = (l+r)/2
        merge_sort_recurse(a, l, mid)
        merge_sort_recurse(a, mid+1, r)
        merge(a, l, mid, r)

def merge_sort(a):
    merge_sort_recurse(a, 0, len(a) - 1)

if __name__ == "__main__":
    a = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(a)

    print a