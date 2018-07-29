#!/usr/bin/python

class Search:
    '''
    @params: arr - array of items in sorted order
    @params: val - value to be serached

    @return: 
        index of val if found in array
        else, (-(insertion)-1) where insertion is the index at which val would be inserted
    '''
    def binarySearch(self, arr, val):
        if arr is None or arr == []:
            return -1

        low = 0
        high = len(arr)-1

        return self.__binSearch(arr, val, low, high)

    def __binSearch(self, a, val, l, h):
        #print "Evaluating array[", a[l], "...", a[h], "]"
        if l <= h:
            mid = (l+h)/2
            if val == a[mid]:
                return mid
            elif val < a[mid]:
                if (mid > l and a[mid-1] < val) or mid == l:
                    return -mid - 1
                else:
                    return self.__binSearch(a, val, l, mid - 1)
            else: # val > a[mid]
                if (mid < h and a[mid+1] > val) or mid == h:
                    return -(mid+1) - 1
                else:
                    return self.__binSearch(a, val, mid+1, h)

        #return -1
        raise ValueError('value', val, 'not found in array')

if __name__ == "__main__":
    #a = [1, 2, 3, 5, 6, 7, 8, 9]
    #val = 4

    a = [2, 3, 4, 10, 40]
    val = 5

    print Search().binarySearch(a, val)