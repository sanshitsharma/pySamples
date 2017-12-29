#!/usr/bin/python

def third_max(nums):
    v = [float('-inf'), float('-inf'), float('-inf')]
    for num in nums:
        if num not in v:
            if num > v[0]:
                v = [num, v[0], v[1]]
            elif num > v[1]:
                v = [v[0], num, v[1]]
            elif num > v[2]:
                v = [v[0], v[1], num]

    return v[0] if float('-inf') in v else v[2]

def main():
    print "Given a list of numbers, return the third maximum number. If a third max does not exist then return the greatest number"
    nums = [2, 1, 5]
    print third_max(nums)

if __name__ == "__main__":
    main()