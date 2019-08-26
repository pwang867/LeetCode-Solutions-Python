class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        return self.numTreesHelper(n)
    
    def numTreesHelper(self, n):
        if n <= 1:
            return 1
        if n in self.memo:
            return self.memo[n]
        
        cnt = 0
        for i in range(n):
            left = self.numTreesHelper(i-0)
            right = self.numTreesHelper(n-1-i)
            cnt += left*right
        
        self.memo[n] = cnt
        return cnt
    
