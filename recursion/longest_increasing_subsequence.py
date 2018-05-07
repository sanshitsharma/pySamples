#/usr/bin/env python

'''
# Iterative solution
def lis(a):
    max_ss = []
    for i in range(len(a)):
        ss = [a[i]]
        length = 1
        for j in range(i+1, len(a)):
            if a[j] >= ss[length-1]:
                ss.append(a[j])
                length += 1

        if length > len(max_ss):
            max_ss = ss

    return max_ss
'''

global maximum

def _lis(a, n):
    if n == 1:
        return 1

    global maximum

    max_ending_here = 1

    for i in range(1, n):
        res = _lis(a, i)
        if a[i-1] < a[n-1] and res+1 > max_ending_here:
            max_ending_here = res + 1

    maximum = max(maximum, max_ending_here)

    return max_ending_here

# Recursive solution
def lis(a):
    global maximum

    maximum = 1
    _lis(a, len(a))

    return maximum

if __name__ == "__main__":
    #a = [50, 3, 10, 7, 40, 80]
    a = [10, 22, 9, 33]
    print lis(a)