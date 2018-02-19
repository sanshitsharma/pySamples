#!/usr/bin/python

def sum(lst):
    sum = 0
    for item in lst:
        sum += item

    return sum

def find_subset_sum(w, t, start, sol):
    if sum(sol) == target:
        return True

    for i in range(start, len(w)):
        sol.append(w[i])
        if find_subset_sum(w, t, i+1, sol):
            return True
        
        sol.pop() #backtrack

    return False
if __name__ == "__main__":
    weights = [10, 7, 5, 18, 12, 20, 15]
    target = 53
    sol = []
    start = 0

    find_subset_sum(weights, target, start, sol)
    print sol