#!/usr/bin/python

from ds.Heap import Heap, Type

def main():
    min_heap = Heap(Type.MIN)

    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.insert(6)
    min_heap.insert(4)
    min_heap.insert(7)
    min_heap.insert(1)

    min_heap.print_heap()

    if min_heap.delete(1):
        print min_heap.print_heap()
    
    print min_heap.pop()
    print min_heap.print_heap()

if __name__ == "__main__":
    main()