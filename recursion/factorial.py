#!/usr/bin/python

def fact(n):
    if n < 2:
        return 1

    return n * fact(n-1)
  
def main():
    T = raw_input()

    nums = []
    for _ in range(0, int(T)):
        n = raw_input()
        print "factorial of '" + n + "' = " + str(fact(int(n)))

if __name__ == "__main__":
    main()
