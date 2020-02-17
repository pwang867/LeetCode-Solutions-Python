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

    
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of 
the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Note:

0 ≤ N ≤ 30.
"""

