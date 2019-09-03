# method 2: dp
# dp[i][j] means whether s1[:i] and s2[:j] matches with s3[:i+j]
# dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) \
#            or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3):  # do not forget, otherwise s3[i+j-1] will be invalid
            return False
        
        # dp[i][j] means whether s1[:i] and s2[:j] matches with s3[:i+j]
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n+1):
            dp[0][j] = (s2[j-1]==s3[j-1])
            if dp[0][j] is False:
                break
        for i in range(1, m+1):
            dp[i][0] = (s1[i-1]==s3[i-1])
            if dp[i][0] is False:
                break
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) \
                            or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[m][n]

    
# recursion with memo
class Solution1(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.memo = set()
        if len(s1) + len(s2) != len(s3):
            return False
        
        return self.isInterleaveHelper(s1, s2, s3, 0, 0, 0)
    
    def isInterleaveHelper(self, s1, s2, s3, i, j, k):
        if i >= len(s1):
            return s2[j:] == s3[k:]
        if j >= len(s2):
            return s1[i:] == s3[k:]
        if k >= len(s3):
            return False
        
        if (i,j) in self.memo:
            return False
        
        if s1[i] == s3[k]:
            if self.isInterleaveHelper(s1, s2, s3, i+1, j, k+1):
                return True
        if s2[j] == s3[k]:
            if self.isInterleaveHelper(s1, s2, s3, i, j+1, k+1):
                return True
        
        self.memo.add((i,j))
        return False
    
