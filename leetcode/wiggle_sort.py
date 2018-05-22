#!/usr/bin/python

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        xL = True
        for i in range(len(nums)-1):
            if xL:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                elif nums[i] == nums[i+1]:
                    # Find next bigger number and swap with i+1
                    j = i + 1
                    while j < len(nums) and nums[j] <= nums[i]:
                        j += 1
                    if j < len(nums):
                        nums[i+1], nums[j] = nums[j], nums[i+1]
            elif not xL:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                elif nums[i] == nums[i+1]:
                    # Find next smaller number and swap with i+1
                    j = i + 1
                    while j < len(nums) and nums[j] >= nums[i]:
                        j += 1
                    if j < len(nums):
                        nums[i+1], nums[j] = nums[j], nums[i+1]
            xL = not xL

if __name__ == "__main__":
    #s = [3, 5, 2, 1, 6, 4]
    #s = [5, 4, 3, 7, 9]
    #s = [1, 2, 1, 1, 3, 6]
    s = [1,1,1,1,2,2,2]
    print "Before:", s
    Solution().wiggleSort(s)
    print "After :", s