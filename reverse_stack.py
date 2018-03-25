#!/usr/bin/python

from ds.Stack import Stack

def reverse_stack(stack):
    r_stk = Stack()
    while not stack.isEmpty():
        r_stk.push(stack.pop())

    return r_stk

if __name__ == "__main__":
    stk = Stack()
    stk.push(4)
    stk.push(3)
    stk.push(2)
    stk.push(1)
    
    print stk.items
    rev_stk = reverse_stack(stk)
    print rev_stk.items