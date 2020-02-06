# use recursion to reduce NSum() finally to twoSum()
# time/space O(n^(N-1))
# must sort first

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        ans = []  # list[list[int]]
        self.NSum(nums, 0, target, 4, [], ans)
        return ans
    
    def NSum(self, nums, start, target, N, path, ans):
        """ 
        path: [int], previous chosen value 
        choose N values from nums[start:]
        """
        if N < 2:
            raise ValueError("N needs two be at least 2")
        if target < nums[start]*N or target > nums[-1]*N:  # early termination
            return
        if N == 2:
            self.twoSum(nums, start, target, path, ans)
            return
        # when N > 2, recursively reduce N
        for i in range(start, len(nums) - N + 1):
            # skip duplicates
            if i == start or nums[i] != nums[i - 1]:  # easy to miss i==start
                self.NSum(nums, i+1, target - nums[i], N - 1, path + [nums[i]], ans)
    
    def twoSum(self, nums, start, target, path, ans):
        left, right = start, len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp == target:
                ans.append(path + [nums[left], nums[right]])
                left += 1  # dead loop if these two lines are missing !
                right -= 1  
                while left < right and nums[left] == nums[left - 1]:  # skip duplicates
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif temp > target:
                right -= 1
            else:
                left += 1

"""
Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
