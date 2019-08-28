# dp[i][j] means the max floor one can test using i eggs and j moves
# dp[i][j] = dp[i-1][j-1] (when egg cracks) + 1 (test floor) 
#           + dp[i][j-1] (when egg is fine)

# optimize space to O(N)
class Solution(object):
    def superEggDrop(self, K, N):
        dp1 = [0]*(N+1)
        
        for i in range(1, K+1):
            dp2 = [0]
            for j in range(1, N+1):
                dp2.append(dp1[j-1] + 1 + dp2[j-1])
                if dp2[-1] >= N:
                    break
            dp1 = dp2
            
        return len(dp1) - 1  # mistake: return dp1[-1]

# space O(K*N)
class Solution1(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        res = 0
        dp = [[0]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            for j in range(1, N+1):
                dp[i][j] = dp[i-1][j-1] + 1 + dp[i][j-1]
                if dp[i][j] >= N:
                    res = j
                    break
        return res
    
