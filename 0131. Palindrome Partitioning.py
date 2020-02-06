# method 2, dp
# we need two dp arrays
# dp1[i][j] means whether s[i:j+1] is a palindrome
# dp2[i] means all partitions for s[:i+1]
class Solution(object):
    def partition(self, s):
        if not s:
            return []
        n = len(s)
        dp1 = [[False]*n for _ in range(n)]
        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (i+1 >= j-1 or dp1[i+1][j-1]):
                    dp1[i][j] = True
        dp2 = [[[s[0]]]]  # dp2[i] is a list of partitions
        for j in range(1, n):
            cur = []
            for i in range(j+1):
                if dp1[i][j]:
                    word = s[i:j+1]
                    if i == 0:
                        cur.append([word])
                    else:
                        for path in dp2[i-1]:
                            cur.append(path+[word])
            dp2.append(cur)
        return dp2[-1]


# method 1: dfs 
class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.memo = {}
        self.ans = []
        self.dfs(s, [], 0)
        return self.ans
    
    def dfs(self, s, path, start):
        if start == len(s):
            self.saveResult(s, path)
            return
        for i in range(start, len(s)):
            if self.isPalindrome(s, start, i):
                path.append(i)
                self.dfs(s, path, i + 1)
                path.pop()
    
    def isPalindrome(self, s, left, right):
        if len(s) < 2:
            return True
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        
        while left < right:
            if s[left] != s[right]:
                self.memo[(left, right)] = False
                return False
            left += 1
            right -= 1
        self.memo[(left, right)] = True
        return True
    
    def saveResult(self, s, path):
        res = []
        pre = 0
        for i in path:
            res.append(s[pre:i+1])
            pre = i+1
        self.ans.append(res)


"""
Given a string s, partition s such that every 
substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
