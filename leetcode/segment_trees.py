#!/usr/bin/python

import math

class SegmentTree:
    def __init__(self, arr):
        self.a = arr
        self.n = len(self.a)
        h = int(math.ceil(math.log(self.n, 2)))
        maxSize = 2*pow(2, h) - 1
        self.st = [0] * maxSize
        
        self._buildSTUtil(self.a, 0, self.n-1, self.st, 0)

    def __repr__(self):
        return str(self.st)

    def _buildSTUtil(self, a, ss, se, st, si):
        #print "a =", a, "ss = 0, se =", se, "st =", st, "si =", si
        if ss == se:
            #print "Matched.. "
            st[si] = a[ss]
            return a[ss]

        mid = self._getMid(ss, se)
        #print "Mid =", mid
        st[si] = self._buildSTUtil(a, ss, mid, st, 2*si+1) + self._buildSTUtil(a, mid+1, se, st, 2*si+2)
        return st[si]

    def _getMid(self, ss, se):
        return ss + (se - ss)/2

    def getSum(self, qs, qe):
        if qs < 0 or qe > self.n-1 or qs > qe:
            print "invalid range"
            return -1

        return self._getSumUtil(0, self.n-1, qs, qe, 0)

    def _getSumUtil(self, ss, se, qs, qe, si):
        if se < qs or ss > qe:
            #print "ss =", ss, "se =", se, "qs =", qs, "qe =", qe, "returning.. 0"
            return 0

        if ss >= qs and se <= qe:
            #print "ss =", ss, "se =", se, "qs =", qs, "qe =", qe, "returning... ", st[qs]
            return self.st[si]

        mid = self._getMid(ss, se)
        return self._getSumUtil(ss, mid, qs, qe, 2*si+1) + self._getSumUtil(mid+1, se, qs, qe, 2*si+2)

    def _updateUtil(self, ss, se, indx, diff, si):
        if indx < ss or indx > se:
            return
        
        before = self.st[si]
        self.st[si] += diff
        mid = self._getMid(ss, se)
        if ss != se:
            self._updateUtil(ss, mid, indx, diff, 2*si+1)
            self._updateUtil(mid+1, se, indx, diff, 2*si+2)

    def update(self, indx, newVal):
        if indx < 0 or indx > self.n-1:
            print "invalid index"
            return False

        diff = newVal - self.a[indx]
        self._updateUtil(0, self.n-1, indx, diff, 0)
        return True

if __name__ == "__main__":
    a = [3, 5, 2, 4, 7]
    st = SegmentTree(a)
    print "Segment Tree:", st

    rSum = st.getSum(2, 4)
    print "Range Sum (2,4) =", rSum

    indx = 2
    newVal = 9
    st.update(indx, newVal)

    print "After Update:", st

    rSum = st.getSum(2, 4)
    print "Range Sum (2,4) =", rSum