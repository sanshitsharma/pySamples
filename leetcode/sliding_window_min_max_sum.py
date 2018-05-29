#!/usr/bin/python

class Solution(object):
    def minMaxSumSlidingWindow(self, arr, k):
        """ The solution here is similar to finding the max in sliding
        window of an array. Here we will use two queues instead of one
        """

        if not arr or k > len(arr):
            return []

        """ Create two double ended queues, minQ and maxQ. The min Q
        will store the indexes of all the useful elements in the current
        window and will maintain increasing order of values from front
        to rear, i.e., arr[minQ.front()] to arr[minQ.rear()] are sorted
        in increasing order. maxQ will do the opposite of minQ """

        minQ = []
        maxQ = []

        res = []

        # Process the first k elements
        for i in range(k):
            while minQ and arr[i] <= arr[minQ[-1]]:
                minQ.pop()

            minQ.append(i)

            while maxQ and arr[i] >= arr[maxQ[-1]]:
                maxQ.pop()

            maxQ.append(i)

        # Process the remaining element
        for i in range(k, len(arr)):
            # The element at index 0 of minQ and maxQ are the minimum
            # and maximum elements respectively of the current window
            res.append(arr[minQ[0]] + arr[maxQ[0]])

            # Remove the elements that are out of the window
            while minQ and minQ[0] <= i-k:
                minQ.pop(0)
            while maxQ and maxQ[0] <= i-k:
                maxQ.pop(0)

            # Update the queues
            while minQ and arr[i] <= arr[minQ[-1]]:
                minQ.pop()
            minQ.append(i)

            while maxQ and arr[i] >= arr[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)

        res.append(arr[minQ[0]] + arr[maxQ[0]])
        return res

if __name__ == "__main__":
    #arr = [12, 1, 78, 90, 57, 89, 56]
    #k = 3
    arr = [1,3,-1,-3,5,3,6,7]
    k = 4
    print Solution().minMaxSumSlidingWindow(arr, k)