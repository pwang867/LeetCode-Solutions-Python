# method 2: dp, O(n)
class Solution(object):
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        pre, cur = 0, 1
        for i in range(2, N+1):
            pre, cur = cur, pre + cur
        return cur
    

# method 1: recursion with memo, O(n)
class Solution1(object):
    def __init__(self):
        self.memo = {0:0, 1:1}
        
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N in self.memo:
            return self.memo[N]
        res = self.fib(N-1) + self.fib(N-2)
        self.memo[N] = res
        return res
    
