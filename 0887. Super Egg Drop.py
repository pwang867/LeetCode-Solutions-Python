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


# dp[k][n] means the minimum trials you need to test N floors using K eggs
class Solution3(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        self.memo = {}
        return self.helper(K, N)
    
    def helper(self, K, N):
        # return the minMax trials when you have K eggs and N floors
        if N == 0:
            return 0
        if K == 0:
            return float('inf')
        if K == 1:
            return N
        if N == 1:
            return 1
        if (K, N) in self.memo:
            return self.memo[(K, N)]
        
        res = float('inf')
        left, right = 0, N+1
        while left + 1 < right:
            mid = left + (right-left)//2
            a = self.helper(K-1, mid-1) + 1
            b = self.helper(K, N-mid) + 1
            res = min(res, max(a, b))
            if a >= b:
                right = mid
            else:
                left = mid
            
        self.memo[(K, N)] = res
        return res
        

"""
You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped 
at a floor higher than F will break, and any egg dropped at 
or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and 
drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with 
certainty what F is, regardless of the initial value of F?

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, 
we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000
"""
