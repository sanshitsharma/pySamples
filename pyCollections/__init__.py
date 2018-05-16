#!/usr/bin/python

'''
@params: arr - array of items in sorted order
@params: val - value to be serached

@return: 
    index of val if found in array
    else, (-(insertion)-1) where insertion is the index at which val would be inserted
'''
def binarySearch(arr, val):
    if arr is None or arr == []:
        return -1

    low = 0
    high = len(arr)-1

    return binSearchRecurse(arr, val, low, high)

def binSearchRecurse(a, val, l, h):
    #print "Evaluating array[", a[l], "...", a[h], "]"
    if l <= h:
        mid = (l+h)/2
        if val == a[mid]:
            return mid
        elif val < a[mid]:
            if (mid > l and a[mid-1] < val) or mid == l:
                return -mid - 1
            else:
                return binSearchRecurse(a, val, l, mid - 1)
        else: # val > a[mid]
            if (mid < h and a[mid+1] > val) or mid == h:
                return -(mid+1) - 1
            else:
                return binSearchRecurse(a, val, mid+1, h)

    raise ValueError('value', val, 'not found in array')

'''
@params: arr - array of items in sorted order
@params: val - value to be serached

@return: 
    index of val if found in array
    else, -1
'''
def linearSearch(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    
    return -1