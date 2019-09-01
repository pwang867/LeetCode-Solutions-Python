# Time: (length of strs)*m*n
        # dynamic programming
        # dp[i][j] means the max number of traversed strings 
        # that could be constructed using i '0' and j '1'
        # for every str, update dp backwards
        
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # add 1 to m and n to make index simple
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        # add every str one by one to update dp
        for s in strs:
            cnt0 = s.count('0')  # counts of '0' in s
            cnt1 = len(s) - cnt0
            # update every dp element
            # dp in range i < cnt0 and j < cnt1 smaller than current str, ignored
            for i in range(m, cnt0 - 1, -1):  
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        
        return dp[-1][-1]
    
