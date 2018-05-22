#!/usr/bin/python

def abbr(s, indx, li):
    if indx == len(s):
        print ''.join(li)
        return

    # Option 1: Add the character at indx and recurse
    li.append(s[indx])
    abbr(s, indx+1, li)
    li.pop()

    # Option 2: Add the count instead of the character and recurse
    if len(li) != 0 and li[len(li)-1].isdigit():
        li[len(li)-1] = str(int(li[len(li)-1]) + 1)
        abbr(s, indx+1, li)
        li[len(li)-1] = str(int(li[len(li)-1]) - 1)
    else:
        li.append('1')
        abbr(s, indx+1, li)
        li.pop()

def alphanumericAbbr(s):
    li = []
    abbr(s, 0, [])

if __name__ == "__main__":
    s = 'GFG'
    alphanumericAbbr(s)