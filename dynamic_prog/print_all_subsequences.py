#!/usr/bin/python

'''
Given a string, print all print all it's subsequences
'''

def get_all_subsequences(s):
    n = len(s)
    combinations_count = pow(2, n)

    ss = []
    for i in range(1,combinations_count):
        lst = []
        count = n - 1
        while i != 0:
            if i & 1 == 1:
                lst.append(s[count])
            count -= 1
            i = i >> 1

        lst.reverse()
        ss.append(''.join(lst))

    return ss

if __name__ == "__main__":
    string = 'ABCD'
    ss = get_all_subsequences(string)

    print ss