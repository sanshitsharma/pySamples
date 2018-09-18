#!/usr/bin/python env

def remove_dups(l):
    read = 0
    write = 0
    seen = set()

    while read < len(l):
        if l[read] in seen:
            read += 1
            continue

        l[write] = l[read]
        seen.add(l[read])
        write += 1
        read += 1

    return l[:write]

if __name__ == "__main__":
    #l = [28, 42, 28, 16, 90, 42, 42, 28]
    #l = [1, 4, 2, 1, 9, 4]
    l = [2, 4, 10, 20, 5, 2, 20, 4]
    print remove_dups(l)
    #print l