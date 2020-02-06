# method 2: dp, O(n^4)
# dp[len][i][p] means if s1[i:i+len] and s2[p:p+len] matches
class Solution(object):
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if len(s1) < 2:
            return s1 == s2
        
        n = len(s1)
        dp = [[[False]*n for i in range(n)] for j in range(n+1)]
        # initialize dp[1][.][.]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = (s1[i] == s2[j])
        
        for k in range(2, n+1):  # k is length of the substring, dp[k][.][.]
            for i in range(n-k+1):
                for j in range(n-k+1):
                    for m in range(1, k):
                        if dp[m][i][j] and dp[k-m][i+m][j+m]:
                            dp[k][i][j] = True
                            break
                        if dp[m][i][j+k-m] and dp[k-m][i+m][j]:
                            dp[k][i][j] = True
                            break
        
        return dp[n][0][0]
        

# method 1: recursion with memo, space O(m^2*n^2) time ???
class Solution1(object):
    def __init__(self):
        self.memo = {}
        
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if len(s1) < 2:
            return s1 == s2
        if (s1, s2) in self.memo:
            return self.memo[(s1,s2)]
        
        if set(s1) != set(s2):
            self.memo[(s1, s2)] = False
            return False
        
        for i in range(len(s1)-1):
            # slice s1 into two parts s1[:i+1] and s1[i+1:]
            left_len = i+1  # s1[i] belongs to left part
            right_len = len(s1) - left_len
            if self.isScramble(s1[:left_len], s2[:left_len]) \
                and self.isScramble(s1[left_len:], s2[left_len:]):
                self.memo[(s1, s2)] = True
                return True
            if self.isScramble(s1[:left_len], s2[-left_len:]) \
                and self.isScramble(s1[left_len:], s2[:right_len]):
                self.memo[(s1, s2)] = True
                return True
        
        self.memo[(s1, s2)] = False
        return False

  

"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""
