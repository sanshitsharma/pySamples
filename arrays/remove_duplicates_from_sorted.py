#!/usr/bin/env python

def remove_dups(a):
    read = 0
    write = 0
    seen = {}

    while read < len(a):
        if a[read] in seen.keys():
            read += 1
            continue

        a[write] = a[read]
        seen[a[read]] = True
        write += 1
        read += 1

    rem = len(a) - write
    for i in range(rem):
        a.pop()

if __name__ == "__main__":
    a = [2, 2, 4, 4, 5, 10, 20, 20]
    remove_dups(a)

    print a