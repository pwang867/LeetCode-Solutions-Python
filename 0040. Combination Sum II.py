# standard backtrack
# use candidates[i] > 0 to optimize
# skip duplicates
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.ans = []
        self.backtrack(candidates, [], 0, target)
        return self.ans
    
    def backtrack(self, candidates, path, start, target):
        if target < 0:
            return
        elif target == 0:
            self.ans.append(path[:])
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:  # candidates are all positive
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    # skip duplicates
                    continue
                path.append(candidates[i])
                self.backtrack(candidates, path, i + 1, target - candidates[i])
                path.pop()


"""
Given a collection of candidate numbers (candidates) 
and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
