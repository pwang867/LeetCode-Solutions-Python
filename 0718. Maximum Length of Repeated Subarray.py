# dp, dp[i][j] means the length of longest common subarray ending with A[i] and B[j]
# it is wrong to make dp[i][j] as the global longest subarray,
# it has to be a local longest subarray, otherwise the dp equation will fail
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        maxLen = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxLen = max(maxLen, dp[i][j])
        
        return maxLen
