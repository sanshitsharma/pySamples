#!/usr/bin/python

def climb_stairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    all_ways = 0
    one_step_behind = 2
    two_step_behind = 1

    for _ in range(2, n):
        all_ways = one_step_behind + two_step_behind
        two_step_behind = one_step_behind
        one_step_behind = all_ways

    return all_ways

def main():
    print "Given 'n' stairs, return how many ways are there to climb the stairs. You can take either 1 step or 2 steps"
    print climb_stairs(7)

if __name__ == "__main__":
    main()