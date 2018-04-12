#!/usr/bin/env python

def partition(a, l, r):
    pivot_indx = l

    while l <= r:
        while l <= r and a[l] <= a[pivot_indx]:
            l += 1

        while r >= l and a[r] >= a[pivot_indx]:
            r -= 1

        if l < r:
            a[l], a[r] = a[r], a[l]

    # At this point, r is pointing to the correct location of the pivot element
    a[r], a[pivot_indx] = a[pivot_indx], a[r]
    return r

def quick_sort_recurse(a, l, r):
    if l > r:
        return

    pivot_indx = partition(a, l, r)
    quick_sort_recurse(a, l, pivot_indx-1)
    quick_sort_recurse(a, pivot_indx+1, r)

def quick_sort(a):
    quick_sort_recurse(a, 0, len(a)-1)

if __name__ == "__main__":
    a = [10, 7, 8, 9, 1, 5]
    quick_sort(a)

    print a