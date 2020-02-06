# method 2: dp, time O(n), space O(1)
class Solution(object):
    def climbStairs(self, n):
        pre, cur = 1, 1
        for _ in range(n-1):
            pre, cur = cur, pre + cur
        return cur

# method 1: recursion with memo, O(n) time, O(n) recursion depth
class Solution1(object):
    def __init__(self):
        self.memo = {}
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        if n in self.memo:
            return self.memo[n]
        
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = res
        return res


"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

