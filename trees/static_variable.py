#!/usr/bin/python

def fooR():
    if fooR.var == 4:
        return

    print "called.. var =", fooR.var
    fooR.var += 1
    return fooR()

def foo():
    fooR.var = 0
    fooR()

if __name__ == "__main__":
    foo()
