# method 3, sum[i] means the total probability from 0 to i
# this can reduce time from O(K+2*W) to O(K+W)
# equation is similar to method 2, but the details are a little more complex

class Solution(object):
    def new21Game(self, N, K, W):
        if K==0 or N >= K+W:
            return 1.0
        
        dp = [0]*(K+W)
        dp[0] = 1.0
        
        for i in range(1, K+W):
            dp[i] = dp[i-1]
            
            if i <= W:
                dp[i] += dp[i-1]/W
            else:
                dp[i] += (dp[i-1] - dp[i-1-W])/W
            
            if i > K:
                dp[i] -= (dp[i-1] - dp[K-1])/W
            
        return dp[N] - dp[K-1]
    
        

# method 2, simplified from method 1, time O(K+2*W)
# dp[i] means the probability to get to points i
# sum(dp[K:])
class Solution2(object):
    def new21Game(self, N, K, W):
        # W >= 1
        if K == 0 or N >= K+W:
            return 1
        
        dp = [0]*(K+W)
        dp[0] = 1.0
        if K+W > 1:
            dp[1] = 1.0/W
        
        for i in range(2, min(K+W,N+1)):
            dp[i] = dp[i-1]
            if i-1 < K:
                dp[i] += dp[i-1]/W
            if i-1-W >= 0:
                dp[i] -= dp[i-1-W]/W
        
        # return sum(dp[K:N+1])/sum(dp[K:])
        # sum(dp[K:]) must be 1.0
        return sum(dp[K:])


# method 1: time O(K*W), time limit exceeded
class Solution1(object):
    def new21Game(self, N, K, W):
        # W >= 1
        dp = [0]*(K+W)
        dp[0] = 1.0
        for i in range(K):
            for j in range(1, W+1):
                dp[i+j] += dp[i]/W
        
        print(dp)
        return sum(dp[K:N+1])/sum(dp[K:])
    

# wrong solution: because different ways getting the same point 
# have different probability 
# dp[i] means the number of ways to get i points
# dp[i] = sum(dp[i-W:min(i,K)])
class Solution1(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0]*(1+K+W-1)  # max point is K+W-1
        dp[0] = 1
        
        for i in range(1, K+W):
            for j in range(W, 0, -1):
                if 0 <= i - j < K:  # don't forget i - j >= 0
                    dp[i] += dp[i-j]
                elif i-j >= K:
                    break  # early cutoff
        
        return sum(dp[K:N+1])*1.0/sum(dp[K:])
    
