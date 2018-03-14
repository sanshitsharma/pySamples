#!/usr/bin/python

def p_rev(str, indx=-1, out=''):
    try:
        out = out + str[indx]
        return p_rev(str, indx-1, out)
    except IndexError:
        return out

if __name__ == "__main__":
    print p_rev('sanshit')