# same as LeetCode #509
class Solution(object):
    def __init__(self):
        self.memo = {0:0, 1:1, 2:1}
        
    def tribonacci(self, n):
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) \
                        + self.tribonacci(n-3)
        return self.memo[n]
    

# dp
class Solution(object):
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
    
