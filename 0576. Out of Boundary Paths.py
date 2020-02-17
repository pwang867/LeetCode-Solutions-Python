# method 2: dp, 3D
# dp[k][i][j] means the number of ways going from out of bound 
# using  <= k steps towards position (i, j)
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        
        istart, jstart = i, j
        limit = 10**9 + 7
        dp = [[[0]*n for i in range(m)] for k in range(N+1)]  # space can be optimized
        
        for k in range(1, N+1):  # number of steps
            for i in range(m):  # positions
                for j in range(n):
                    dp[k][i][j] += 1 if i == 0 else dp[k-1][i-1][j]
                    dp[k][i][j] += 1 if i == m-1 else dp[k-1][i+1][j]
                    dp[k][i][j] += 1 if j == 0 else dp[k-1][i][j-1]
                    dp[k][i][j] += 1 if j == n-1 else dp[k-1][i][j+1]
                    dp[k][i][j] %= limit
        
        return dp[N][istart][jstart]
                    

# method 1, DFS, time O(m*n*N), space O(m*n*N)
# dfs with memo, memorize (i, j, k) where k is the number of steps left
# and (i, j) is the current position, memo records the counts moving from out of bound
# to position (i, j) using k steps
class Solution1(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        self.memo = {}
        return self.dfs(m, n, N, i, j)
    
    def dfs(self, m, n, N, i, j):
        # N is number of step left
        if N == 0:
            return 0
        if (i, j, N) in self.memo:
            return self.memo[(i, j, N)]
        
        cnt = 0
        for d in [(1,0), (-1,0), (0,1), (0,-1)]:
            p, q = i + d[0], j + d[1]
            if p < 0 or p >= m or q < 0 or q >= n:
                cnt += 1
            else:
                cnt += self.dfs(m, n, N-1, p, q)
        
        cnt %= (10**9+7)
        self.memo[(i, j, N)] = cnt
        return cnt

    
"""
There is an m by n grid with a ball. Given the start coordinate (i,j) 
of the ball, you can move the ball to adjacent cell or cross 
the grid boundary in four directions (up, down, left, right). 
However, you can at most move N times. Find out the number of paths 
to move the ball out of grid boundary. The answer may be very large, 
return it after mod 109 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].
"""
