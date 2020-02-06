# two pointers
# time O(n^2), space O(n*log(n)) space used by sorting
# watch out: 1. duplicates 2. use early termination

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        
        res = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:  # skip duplicates
                continue
            if num > 0:  # early termination
                continue 
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[left] + nums[right] + num
                if total == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1  # dead loop will occur without those two lines !!!
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:  # skip duplicates
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        
        return res


"""

Given an array nums of n integers, 
are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""
