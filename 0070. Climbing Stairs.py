# method 2: dp
class Solution(object):
    def climbStairs(self, n):
        pre, cur = 1, 1
        for _ in range(n-1):
            pre, cur = cur, pre + cur
        return cur


# method 1: recursion with memo, O(n) time, O(n) recursion depth
class Solution(object):
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
    
