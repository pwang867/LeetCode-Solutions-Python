# basic DFS, the if conditions for recursion are important
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.genParenthesisHelper(n, n, [], res)
        return res
    
    def genParenthesisHelper(self, left, right, path, res):
        # left and right are the remaining counts allowed
        if left == 0 and right == 0:
            res.append("".join(path))
        
        if left > 0:  # easy to forget this if condition
            path.append("(")
            self.genParenthesisHelper(left-1, right, path, res)
            path.pop()
        
        if right > left:
            path.append(")")
            self.genParenthesisHelper(left, right-1, path, res)
            path.pop()
        
        
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

n   cnt_of_pairs
3   5
4   14
5   42
6   132
7   429
8   1430
9   4862
10  16786
13  742900
14  2674440
15  9694845

(very roughly about (2n)!/(n!*(n+1)!)
proof: https://en.m.wikipedia.org/wiki/Catalan_number#Third_proof
"""

def Catalan(n):  # count of valid n-pairs parenthesis, time O(n^2)
# divide n-pair to "(left) right ", left+right = n-1
    dp = [0]*(n+1)  # dp[n] means the cnt of valid n-pairs parenthesis
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-1-j]
    return dp



if __name__ == "__main__":
    n = 100
#    res = Solution().generateParenthesis(n)
#    print(len(res))
    
    print(Catalan(n))
    
    