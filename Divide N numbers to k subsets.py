# count the number of ways to divide n numbers to k subsets

def countP(n, k): 
      
    # Table to store results of subproblems 
    dp = [[0 for i in range(k + 1)]  
             for j in range(n + 1)] 
  
    # Base cases 
    for i in range(n + 1): 
        dp[i][0] = 0
  
    for i in range(k + 1): 
        dp[0][k] = 0
  
    # Fill rest of the entries in  
    # dp[][] in bottom up manner 
    for i in range(1, n + 1): 
        for j in range(1, k + 1): 
            if (j == 1 or i == j): 
                dp[i][j] = 1
            else: 
                dp[i][j] = (j * dp[i - 1][j] +
                                dp[i - 1][j - 1]) 
                  
    return dp[n][k] 

n = 100
k = 8
print(countP(n, k))

# roughly about k**n/k! - (k-1)**n/(k-1)!  
# (having two or more empty sets needs to be dealt with better)

