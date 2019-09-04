# metdhod 4: use mathematical law, beat 99%
# every integer can be expressed by no more than perfect squares
# if and only if n%8 == 7, then n requires four perfect squares
class Solution(object):
    def numSquares(self, n):
        while n%4 == 0:
            n = n//4
            
        if n%8 == 7:
            return 4
        
        for i in range(int(pow(n,0.5))+1):
            j = int(pow(n-i*i, 0.5))
            if i*i + j*j == n:
                return int(j>0) + int(i>0)
        
        return 3


# method 3: dp, reduce time to O(n*1.5), beat 24%
class Solution3(object):
    def numSquares(self, n):
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(1, int(pow(i, 0.5))+1):
                dp[i] = min(dp[i], 1 + dp[i-j*j])

        return dp[n]

# method 2: dp, time O(n^2), space O(n), TLE, beat 5%
class Solution2(object):
    def numSquares(self, n):
        if n < 4:
            return n  # mistake: return 1
        dp = [float('inf')]*(n+1)
        k = 1
        while k*k <= n:
            if k*k == n:
                return 1
            dp[k*k] = 1
            k += 1
        
        for i in range(2, n+1):
            if dp[i] == 1:
                continue
            for j in range(1, i//2+1):
                dp[i] = min(dp[i], dp[j]+dp[i-j])
        
        return dp[n]


# method 1: recursion with memo
class Solution1(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        k = 1
        while k*k <= n:
            self.memo[k*k] = 1
            k += 1
        
        return self.dfs(n)
    
    def dfs(self, n):
        if n in self.memo:
            return self.memo[n]
        
        m = int(pow(n, 0.5))
        ans = float('inf')
        for i in range(m, 0, -1):
            ans = min(ans, 1 + self.dfs(n-i*i))
        
        self.memo[n] = ans
        return ans
    
