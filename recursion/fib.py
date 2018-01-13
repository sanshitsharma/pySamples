#!/usr/bin/python

import argparse 

def fib(n):
    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs=1, help="Index of the fibonacci number", type=int)

    args = parser.parse_args()

    print "Fibonacci number at index '" + str(args.n[0]) + "' = " + str(fib(args.n[0]-1))

if __name__ == "__main__":
    main()
