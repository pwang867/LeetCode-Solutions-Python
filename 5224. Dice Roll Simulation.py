
# dp[i][j] means the counts when the last dice is dice i with consecutive frequency j

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        LIMIT = 10**9 + 7
        N = max(rollMax)+1  # max allowed frequence
        dp1 = [[0 for j in range(16)] for i in range(7)]
        for i in range(1, 7):
            if rollMax[i-1] >= 1:
                dp1[i][1] = 1
        
        for time in range(2, n+1):
            dp2 = [[0 for j in range(N)] for i in range(7)]
            for i in range(1, 7):
                total = sum(dp1[i])  # next time different dice
                for temp in range(1, 7):
                    if temp != i and rollMax[temp-1] >= 1:
                        dp2[temp][1] += total
                        dp2[temp][1] %= 10**9 + 7
                for j in range(1, N):
                    if dp1[i][j] == 0:
                        continue
                    if j + 1 <= rollMax[i-1]:  # next time is still self                     
                        dp2[i][j+1] += dp1[i][j]
                        dp2[i][j+1] %= LIMIT
            dp1 = dp2
        
        return sum([sum(row)%LIMIT for row in dp1])%LIMIT


#n = 2
#rollMax = [1,1,2,2,2,3]
n = 2000
rollMax = [12,6,5,12,10,9]
print(Solution().dieSimulator(n, rollMax))

