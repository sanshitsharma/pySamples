#!/usr/bin/python env

def remove_dups(l):
    read = 0
    write = 0
    seen = {}

    while read < len(l):
        if l[read] in seen.keys():
            if write == read:
                write = read
            read += 1
            continue
        
        if write != read:
            l[write] = l[read]
        seen[l[read]] = True
        read += 1
        write += 1

    remaining = len(l) - write
    for i in range(remaining):
        l.pop()

if __name__ == "__main__":
    #l = [28, 42, 28, 16, 90, 42, 42, 28]
    #l = [1, 4, 2, 1, 9, 4]
    l = [2, 4, 10, 20, 5, 2, 20, 4]
    remove_dups(l)
    print l