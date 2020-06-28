# with duplicates numbers


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # necessary, to skip duplicates
        self.backtrack(nums, 0, [], res)
        return res
    
    def backtrack(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:  # skip duplicates. i > start, not i > 0
                continue
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, res)  # i + 1, not i
            path.pop()


"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
