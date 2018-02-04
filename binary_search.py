#!/usr/bin/python

class BinarySearch:
    def __binary_search(self, a, elem, l, r):
        if l > r:
            return -1

        mid = (l+r)/2
        if elem == a[mid]:
            return mid
        elif elem < a[mid]:
            return self.__binary_search(a, elem, l, mid-1)
        else:
            return self.__binary_search(a, elem, mid+1, r)

        return -1

    @staticmethod
    def find(a, elem):
        if len(a) == 0:
            return -1

        return BinarySearch().__binary_search(a, elem, 0, len(a)-1)

def main():
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    print BinarySearch.find(a, -1)

if __name__ == "__main__":
    main()