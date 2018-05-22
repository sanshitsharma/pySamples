#!/usr/bin/python

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.d = {0: v1, 1: v2}

        self.currItr = 0
        self.itrsIndx = []
        if len(self.d[0]) > 0:
            self.itrsIndx.append(0)   
        else:
            self.isCurrV1 = False
            self.itrsIndx.append(-1)
        
        if len(self.d[1]) > 0:
            self.itrsIndx.append(0)
        else:
            self.itrsIndx.append(-1)

    def next(self):
        """
        :rtype: int
        """
        val = self.d[self.currItr][self.itrsIndx[self.currItr]]
        self.itrsIndx[self.currItr] += 1
        if self.itrsIndx[self.currItr] > len(self.d[self.currItr])-1:
            self.itrsIndx[self.currItr] = -1

        if self.currItr == 0 and self.itrsIndx[1] != -1:
            self.currItr = 1
        elif self.currItr == 1 and self.itrsIndx[0] != -1:
            self.currItr = 0

        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.itrsIndx[self.currItr] != -1:
            return True
        
        i = self.currItr
        while i < len(self.itrsIndx) and self.itrsIndx[i] == -1:
            i += 1

        if i > len(self.itrsIndx) - 1:
            return False

        self.currItr = i
        return True
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

if __name__ == "__main__":
    v1 = [1,2]
    v2 = [3,4,5,6] 

    i, v, = ZigzagIterator(v1, v2), []
    while i.hasNext():
        v.append(i.next())

    print v