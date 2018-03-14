#!/usr/bin/python

def remove_spaces(string):
    lst = []
    for c in string:
        if not c == ' ':
            lst.append(c)

    return ''.join(lst)

if __name__ == "__main__":
    print remove_spaces("g  eeks   for ge  eeks  ")