class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.helper([], 1, k, n)
        return self.ans
    
    def helper(self, path, start, k, target):
        if k == 0:
            if target == 0:
                self.ans.append(path[:])
            return
        if start == 10:
            return
        for i in range(start, 10):
            if target - i < 0:
                break
            path.append(i)
            self.helper(path, i + 1, k - 1, target - i)
            path.pop()


"""
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
