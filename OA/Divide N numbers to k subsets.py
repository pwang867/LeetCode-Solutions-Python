# time: roughly about k**n/k! - (k-1)**n/(k-1)!  
# (having two or more empty sets needs to be dealt with better)

def countP(n, k):
    # Table to store results of subproblems 
    dp = [[0 for j in range(k + 1)]  
             for i in range(n + 1)] 
  
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


if __name__ == "__main__":
    n = 100
    k = 8
    print(countP(n, k))


"""
count the number of ways to divide a set of n numbers to k subsets
numbers are unique
"""
