#!/usr/bin/python

from string import punctuation

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        wordCounts = {}
        maxCount = 0
        mostCommon = ''

        for word in paragraph.lower().split():
            word = word.strip("!?',;.")
            if word not in banned:
                try:
                    wordCounts[word] += 1
                except:
                    wordCounts[word] = 1

                if wordCounts[word] > maxCount:
                    maxCount = wordCounts[word]
                    mostCommon = word

        return mostCommon

if __name__ == "__main__":
    s = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print Solution().mostCommonWord(s, banned)

