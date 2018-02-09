#!/usr/bin/python

from collections import OrderedDict

def find_rank_index(scores, alice_score, current_rank_index = 0):
    for i in range(current_rank_index, -1, -1):
        #print "searching start from index = ", i, " score = ", scores[i], " alice_score =", alice_score
        if scores[i] > alice_score:
            #print "Found higher score, returning: score =", scores[i], " & i =", i 
            return scores[i], i
    
    return None, None

def climbingLeaderboard(scores, alice):
    ranks = OrderedDict()

    rank = 1
    for i in range(len(scores)):
        if not ranks.has_key(scores[i]):
            ranks[scores[i]] = rank
            rank += 1

    serach_from_index = len(scores) - 1
    # Loop over Alice's scores
    highest_rank_acheived = False
    for i in range(len(alice)):
        if highest_rank_acheived:
            print 1
            continue

        if ranks.has_key(alice[i]):
            print ranks[alice[i]]
            continue

        next_largest_score, serach_from_index = find_rank_index(scores, alice[i], serach_from_index)
        #print "i =", i, " alice_score =", alice[i], " next_higher_score =", next_largest_score
        if next_largest_score is None:
            # If there is no greater score than this, then alice has reached RANK 1
            highest_rank_acheived = True
            print 1
        else:
            print ranks[next_largest_score] + 1


def main():
    #scores = [100, 100, 50, 40, 40, 20, 10]
    #alice = [5, 25, 50, 120]
    n = int(raw_input().strip())
    scores = map(int, raw_input().strip().split(' '))
    m = int(raw_input().strip())
    alice = map(int, raw_input().strip().split(' '))

    print len(alice)
    #result = climbingLeaderboard(scores, alice)
    climbingLeaderboard(scores, alice)

if __name__ == "__main__":
    main()