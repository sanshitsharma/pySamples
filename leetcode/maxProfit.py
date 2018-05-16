#!/usr/bin/python

from ds.Heap import Heap
from pyCollections import binarySearch

class Solution(object):
    def canPerform(self, tasks, ability):
        for task in tasks:
            if ability >= task:
                return True

        return False
        
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        pdMap = {}
        for i in range(len(difficulty)):
            try:
                pdMap[profit[i]].append(difficulty[i])
                pdMap[profit[i]].sort()
            except Exception as e:
                pdMap[profit[i]] = [difficulty[i]]
        
        pHeap = Heap()
        for p in profit:
            pHeap.insert(p)

        worker = sorted(worker, reverse=True)
        print worker

        profit = 0
        for ability in worker:
            if self.canPerform(pdMap[pHeap.peek()], ability):
                profit += pHeap.peek()
                continue

            while pHeap.size() > 0 and not self.canPerform(pdMap[pHeap.peek()], ability):
                e = pHeap.pop()

            if pHeap.size() == 0:
                break

            profit += pHeap.peek()

        return profit

if __name__ == "__main__":
    '''
    d = [2,4,6,8,10]
    p = [10,20,30,40,50]
    w = [4,5,6,7]

    d = [68,35,52,47,86]
    p = [67,17,1,81,3]
    w= [92,10,85,84,82]

    d = [2,17,19,20,24,29,33,43,50,51,57,67,70,72,73,75,80,82,87,90]
    p = [6,7,10,17,18,29,30,31,34,39,40,42,48,54,57,78,78,78,83,88]
    w = [12,9,11,41,11,87,48,6,48,93,76,73,7,50,55,97,47,33,46,10]
    '''

    d = [64448,79457,42016,11665,2469,91969,46731,54320,5882,93835,21708,50277,16955,45755,72327,12268,15839,18850,10936,86865,31179,70806,862,89380,85395,37685,35989,22400,65446,89518,87777,70913,94050,19520,32338,6472,5200,80772,51039,17062,50872,15560,72431,78446,60361,6777,31654,21757,14900,97226]
    w = [55170,24810,99019,14644,60739,86776,3656,85057,88453,42411,63691,60967,64863,28688,57126,98045,43420,1719,81693,43774,89525,86382,83018,5553,3184,1542,40108,39794,79829,30024,96082,41089,60930,38049,63082,94078,7062,33691,18438,35911,30367,21478,97103,32558,53184,24942,53365,48591,38949,88794]
    p = [1934,65871,592,76268,61862,74422,53430,95603,70312,43409,30258,54173,99791,21407,42909,96179,64854,77416,24428,68409,21827,4982,72940,99041,52118,94881,31780,84764,7679,56624,41536,87404,39901,61306,81696,61301,46775,19110,95183,84615,2265,56050,69873,14041,41356,18511,15227,5037,23642,36803]

    print Solution().maxProfitAssignment(d, p, w)

'''
Find the job with maximum profit whose difficulty <= worker's ability
'''