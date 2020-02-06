# same as LeetCode #509
# dp, time O(n), space O(1)
class Solution2(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        n1, n2, n3 = 0, 1, 1
        for _ in range(n-2): # not (n - 3)
            n1, n2, n3 = n2, n3, n1 + n2 + n3
        
        return n3
        

# recursoin with memo
class Solution1(object):
    def __init__(self):
        self.memo = {0:0, 1:1, 2:1}
        
    def tribonacci(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) \
                        + self.tribonacci(n-3)
        return self.memo[n]
    

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
