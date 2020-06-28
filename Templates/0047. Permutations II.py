class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        ans = []
        self.helper(nums, [], ans, len(nums))
        return ans
    
    def helper(self, nums, path, ans, n):
        if len(path) == n:  # stop condition
            ans.append(path)
            return 
        
        for i in range(len(nums)):  # get elements one by one and then use recursion
            if i > 0 and nums[i] == nums[i-1]:  # no duplicates
                continue
            self.helper(nums[:i] + nums[i+1:], path + [nums[i]], ans, n)


"""
Given a collection of numbers that might contain duplicates, 
return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

