# method 2: dP, O(m*n), n=len(prob), m=target


class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        if not prob or target > len(prob):
            return 0
        n = target + 1
        dp = [0]*n
        dp[0] = 1-prob[0]
        if target > 0:
            dp[1] = prob[0]
        
        for j in range(1, len(prob)):
            p = prob[j]
            for i in range(target, 0, -1):
                dp[i] = dp[i]*(1-p) + dp[i-1]*p
            dp[0] = dp[0]*(1-p)
        return dp[-1]
        

# method 1: DFS, time O(n!/m!/(n-m)!)  < 2^n


class Solution1(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        if not prob:
            return 0
        if target > len(prob):
            return 0
        
        self.res = 0
        self.dfs(prob, 0, 1, target)
        return self.res
    
    def dfs(self, prob, i, path, target):
        if i == len(prob):
            if target == 0:
                self.res += path
            return
        if target > 0:  # choose head
            self.dfs(prob, i+1, path*prob[i], target-1)
        if len(prob) - i > target:  # the other side
            self.dfs(prob, i+1, path*(1-prob[i]), target)


# target = 8

prob = [0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2]
target = 7
print(Solution().probabilityOfHeads(prob, target))
print(Solution1().probabilityOfHeads(prob, target))


"""
You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.

Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.


Example 1:

Input: prob = [0.4], target = 1
Output: 0.40000
Example 2:

Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125
"""
