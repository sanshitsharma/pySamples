#!/usr/bin/env python

def remove_dups(a):
    read = 0
    write = 0
    seen = set()

    while read < len(a):
        if a[read] in seen:
            read += 1
            continue

        a[write] = a[read]
        seen.add(a[read])
        read += 1
        write += 1

    return a[:write]

if __name__ == "__main__":
    a = [2, 2, 4, 4, 5, 10, 20, 20]
    print remove_dups(a)