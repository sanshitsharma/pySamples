#!/usr/bin/env python

class IntegerToRoman():
    def __init__(self):
        self.__minimalDict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        self.__baseValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    def _getBaseValue(self, num):
        if num < 1:
            return 0

        for bv in self.__baseValues:
            if bv <= num:
                return bv

    def convert(self, num):
        if num < 1 or num > 4999:
            return ''

        ans = ''
        while num != 0:
            baseValue = self._getBaseValue(num)
            ans += self.__minimalDict[baseValue] * (num/baseValue)
            num %= baseValue

        return ans

if __name__ == "__main__":
    print IntegerToRoman().convert(4999)