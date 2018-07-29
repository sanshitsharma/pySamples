#!/usr/bin/env python

class RomanToInteger:
    def __init__(self):
        self.dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def convert(self, S):
        if not S:
            return 0

        indx = 0
        num = 0

        while indx < len(S):
            if indx+1 < len(S) and self.dict[S[indx]] < self.dict[S[indx+1]]:
                num += self.dict[S[indx+1]] - self.dict[S[indx]]
                indx += 2
            else:
                num += self.dict[S[indx]]
                indx += 1

        return num

if __name__ == "__main__":
    print RomanToInteger().convert('MCMXCIV')