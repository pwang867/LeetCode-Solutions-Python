# dfs with backtracking, 
# follow up: duplicates, not reusable


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        candidates.sort()
        self.backtrack(candidates, [], 0, target)
        return self.ans
    
    def backtrack(self, candidates, path, start, target):
        if target == 0:
            self.ans.append(path[:])
            return
        if target < 0:  # early termination, because candidates are all positive
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:  # early termination
                break
            path.append(candidates[i])
            # change to i+1 if not reusable
            self.backtrack(candidates, path, i, target - candidates[i]) 
            path.pop()


"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""
