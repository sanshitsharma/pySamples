#/usr/bin/python

import argparse

"""
This program finds all prime numbers
between 2 & n
"""

def get_all_primes(n):
    # List of all numbers from 2 to n
    nums = range(2, n+1)

    """
    Start with p = 2
    While p^2 is < n+1, for each p, mark 
    all of it's multiples to -1
    """

    p = 2
    p_idx = nums.index(p)

    i = False
    #while i is not True:
    while p*p < n+1:
        # Mark all multiples of p starting at 2p as -1
        for idx in range(p_idx+p, len(nums)):
            if nums[idx]%p == 0:
                nums[idx] = -1

        for idx in range(p_idx+1, len(nums)):
            if nums[idx] != -1:
                p = nums[idx]
                p_idx = idx
                break

        i = True

    primes = []
    for num in nums:
        if num != -1:
            primes.append(num)

    return primes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", nargs=1, help="Number which serves at the upper limit for prime number seive.\n The program will return a list of all prime numbers between 2 & num", type=int)

    args = parser.parse_args()

    print get_all_primes(args.num[0])

if __name__ == "__main__":
    main()
