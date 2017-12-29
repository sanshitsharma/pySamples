#!/usr/bin/python

from enum import Enum

class Type(Enum):
    MAX = 1
    MIN = 2

class Heap:
    def __init__(self, type=Type.MAX):
        self.__items = []
        self.__type = type

    def print_heap(self):
        print "--------------------"
        if self.__type == Type.MIN:
            print "Heap Type: MIN"
        else:
            print "Heap Type: MAX"
        print self.__items

    def size(self):
        return len(self.__items)

    def __swap(self, elem_1_index, elem_2_index):
        temp = self.__items[elem_1_index]
        self.__items[elem_1_index] = self.__items[elem_2_index]
        self.__items[elem_2_index] = temp

    def __comparator(self, curr, parent):
        if self.__type == Type.MAX:
            return self.__items[curr] > self.__items[parent]
        else: 
            return self.__items[curr] < self.__items[parent]

    def heapify(self):
        curr = len(self.__items) - 1
        parent = (curr - 1)/2

        while curr > 0 and self.__comparator(curr, parent):
            # Swap current and parent
            self.__swap(curr, parent)

            # Recalculate the indices 
            curr = parent
            parent = (curr - 1)/2

    def insert(self, elem):
        self.__items.append(elem)
        self.heapify()

    def contains(self, elem):
        try:
            indx = self.__items.index(elem)
        except ValueError:
            return False
        else:
            return True

    def __get_prime_child_index(self, child_1_index, child_2_index):
        if self.__type == Type.MAX:
            # Find the bigger of two children
            if self.__items[child_1_index] > self.__items[child_2_index]:
                return child_1_index
            else:
                return child_2_index
        else:
            # Find the smaller of two children
            if self.__items[child_1_index] > self.__items[child_2_index]:
                return child_2_index
            else:
                return child_1_index

    def reheapify(self, elem_index):
        # Given index of an elements in the heap, push it down
        # to it's proper position in the heap
        last_index = len(self.__items) - 1

        while elem_index <= last_index:
            child_1_index = 2 * elem_index + 1
            child_2_index = 2 * elem_index + 2
            
            if child_1_index <= last_index and child_2_index <= last_index:
                prime_child_index = self.__get_prime_child_index(child_1_index, child_2_index)
                if self.__comparator(prime_child_index, elem_index):
                    self.__swap(prime_child_index, elem_index)
                    elem_index = prime_child_index
            elif child_1_index <= last_index and self.__comparator(child_1_index, elem_index):
                self.__swap(child_1_index, elem_index)
                elem_index = child_1_index
                continue
            else:
                break

    def delete(self, elem):
        if not self.contains(elem):
            print "elem", elem, "does not exist in heap"
            return False

        elem_index = self.__items.index(elem)

        # Replace the element to be deleted with the last element in the list
        # and delete the last element
        self.__items[elem_index] = self.__items[len(self.__items) - 1]
        self.__items.pop()

        self.reheapify(elem_index)
        return True

    def peek(self):
        return self.__items[0]

    def pop(self):
        num = self.__items[0]
        self.delete(self.__items[0])
        return num