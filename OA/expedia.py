
"""
Find the total number of ways to assign n people to k computers, 
The number of people assigned to computers should be equal or increasing

each computer should have at least 1 person
"""


# dynamic programming
class Solution:
    def partition(self, n, k):
        # k: number of computer, n: person
        dp1 = [[0]*(n+1) for j in range(n+1)]
        dp1[0][0] = 1
        
        for i in range(1, k+1):
            dp2 = [[0]*(n+1) for j in range(n+1)]
            for j in range(i, n+1):
                for p in range(max(1, j/i), j-i+2):
                    if j + p*(k-i) > n:  # very efficient cutoff, p must be <= the average of the persons for the rest computers
                        break
                    for q in range(min(j-p, p)+1):
                        dp2[j][p] += dp1[j-p][q]
            dp1 = dp2
        
        return sum(dp1[n])

n, k = 200, 200
print(Solution().partition(n, k))
