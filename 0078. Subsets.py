# DFS, time O(2^n) or O(result), space O(2^n*n)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        # nums.sort()  # unnecessary because nums are all distinct
        self.backtrack(nums, 0, [], ans)
        return ans

    def backtrack(self, nums, start, path, ans):
        ans.append(path[:])  # use path[:] to copy path, can not use path directly
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i + 1, path, ans)
            path.pop()



"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
