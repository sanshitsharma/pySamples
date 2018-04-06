#!/usr/bin/python

class Queue:
    def __init__(self):
        self.lst = []

    def enqueue(self, value):
        self.lst.append(value)

    def dequeue(self):
        try:
            return self.lst.pop(0)
        except IndexError as e:
            return None

    def is_empty(self):
        return len(self.lst) == 0

def find_jumping_numbers(x):
    res = []
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i)

        while not q.is_empty():
            num = q.dequeue()
            if num < x:
                res.append(num)
                last_digit = num%10
                if last_digit == 0:
                    q.enqueue(num*10 + (last_digit+1))
                elif last_digit == 9:
                    q.enqueue(num*10 + (last_digit-1))
                else:
                    q.enqueue(num*10 + (last_digit-1))
                    q.enqueue(num*10 + (last_digit+1))

    return res        

if __name__ == "__main__":
    x = 110
    print find_jumping_numbers(x)