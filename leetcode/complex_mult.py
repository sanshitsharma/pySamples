#!/usr/bin/python

class Solution(object):
    def getTokens(self, s):
        neg = False
        if s[0] == '-':
            neg = True
            s = s[1:]

        real = 0
        i = 0
        while s[i].isdigit():
            real = real*10 + int(s[i])
            i += 1
        
        if neg:
            real = -real
            neg = False

        i += 1
        if s[i] == '-':
            neg = True
            i += 1

        imag = 0
        while s[i].isdigit():
            imag = imag*10 + int(s[i])
            i += 1

        if neg:
            imag = -imag

        return real, imag

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p, q = self.getTokens(a)
        r, s = self.getTokens(b)
        
        return str(p*r - q*s) + '+' + str(p*s + q*r) + 'i'

if __name__ == "__main__":
    #a = "1+1i"
    #b = "1+1i"

    #a = "1+-1i"
    #b = "1+-1i"

    a = "78+-76i"
    b = "-86+72i"

    print Solution().complexNumberMultiply(a, b)