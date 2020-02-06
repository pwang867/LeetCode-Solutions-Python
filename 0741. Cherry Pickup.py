# method 3: simplified from method 1 and 2 to save space to O(n^2)
# and use only one dp array
# but method 1 shows the logic much better
class Solution(object):
    def cherryPickup(self, grid):
        if not grid or not grid[0]:
            return 0
        
        N = len(grid)
        dp = [[-float('inf')]*N for _ in range(N)]
        dp[0][0] = grid[0][0]
        
        for step in range(1, 2*N-1):
            for i in range(min(step,N-1), max(step-(N-1),0) - 1, -1):
                # the iteration order of i and p is important for saving space
                j = step - i
                if grid[i][j] < 0:
                    continue
                for p in range(i, max(step-(N-1), 0) - 1, -1): 
                    q = step - p
                    if grid[p][q] < 0:
                        continue
                    dp[i][p] = max([dp[x][y] for x in [i, i-1] \
                                     for y in [p, p-1] if x >= 0 and y >= 0])
                    dp[i][p] += grid[i][j]
                    if p != i:
                        dp[i][p] += grid[p][q]
        
        return max(0, dp[-1][-1])



# method 2: simplified from method 1 to save space to O(n^2)
# but method 1 shows the logic much better
class Solution(object):
    def cherryPickup(self, grid):
        if not grid or not grid[0]:
            return 0
        
        N = len(grid)
        dp1 = [[-float('inf')]*N for _ in range(N)]
        dp1[0][0] = grid[0][0]
        
        for step in range(1, 2*N-1):
            dp2 = [[-float('inf')]*N for _ in range(N)]
            
            for i in range(min(step,N-1), max(step-(N-1),0) - 1, -1):
                j = step - i
                if grid[i][j] < 0:
                    continue
                for p in range(i, max(step-(N-1), 0) - 1, -1):
                    q = step - p
                    if grid[p][q] < 0:
                        continue
                    dp2[i][p] = max([dp1[x][y] for x in [i, i-1] \
                                     for y in [p, p-1] if x >= 0 and y >= 0])
                    dp2[i][p] += grid[i][j]
                    if p != i:
                        dp2[i][p] += grid[p][q]
            
            dp1 = dp2
        
        return max(0, dp1[-1][-1])


# method 1: dp, think as two persons walking at the same pace
# dp[step][i][q] means after a count of step of pickups, the position
# of two persons are at (i, j) and (p, q)
class Solution1(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        N = len(grid)
        dp = [[[-1]*N for i in range(N)] for step in range(2*N-1)]
        dp[0][0][0] = grid[0][0]
        
        for step in range(1, 2*N-1):
            # two persons: (i, j), (p, q)
            # i + j = p + q = step
            for i in range(N-1, -1, -1):
                j = step - i
                if j < 0 or j >= N or grid[i][j] < 0:  # obstacle at (i, j)
                    continue
                for p in range(i, -1, -1):
                    q = step - p
                    if q < 0 or q >= N or grid[p][q] < 0: # obstacle at (p, q)
                        continue
                    dp[step][i][p] = max(dp[step][i][p], dp[step-1][i][p])
                    if p > 0:
                        dp[step][i][p] = max(dp[step][i][p], dp[step-1][i][p-1])
                    if i > 0:
                        dp[step][i][p] = max(dp[step][i][p], dp[step-1][i-1][p])
                    if i > 0 and p > 0:
                        dp[step][i][p] = max(dp[step][i][p], dp[step-1][i-1][p-1])
                    if dp[step][i][p] >= 0:  # easy to miss !
                        # check if (i,p) is achievable from a previous step
                        dp[step][i][p] += grid[i][j]
                        if p != i:  # when two persons meet
                            dp[step][i][p] += grid[p][q]
        
        return max(0, dp[-1][-1][-1])
    
