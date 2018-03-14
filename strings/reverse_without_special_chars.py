#!/usr/bin/python

def reverse_wo_sc(data):
    string = list(data)
    l = 0
    r = len(string) - 1

    while l < r:
        while not string[l].isalpha():
            l = l + 1
        print "l =", l
        
        while not string[r].isalpha():
            r = r - 1
        print "r =", r
        if l >= r:
            break

        # Swap
        string[l], string[r] = string[r], string[l]
        l = l + 1
        r = r - 1

    return "".join(string)
    

if __name__ == "__main__":
    string = 'a,b$c'
    res = reverse_wo_sc(string)
    print res