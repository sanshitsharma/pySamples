#!/usr/bin/python

class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return '()'

        team = map(str, range(1, n+1))

        while n > 1:
            for i in range(n/2):
                team[i] = "({},{})".format(team[i], team.pop())
            n /= 2

        #print matchUps
        return team[0]

if __name__ == "__main__":
    n = 4
    res = Solution().findContestMatch(n)
    print res