# method 3: DP, time O(n^2)
# DP is always similar to DFS with memo (method 1)
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [0]*(len(s)+1)  # with padding
        dp[0] = True
        for i in range(1, len(s)+1):  # i is index in dp
            for j in range(i, 0, -1):
                if s[j-1:i] in wordDict and dp[j-1]:
                    dp[i] = True
                    break
        return dp[-1]
    

# method 2: BFS
from collections import deque
class Solution2(object):
    def wordBreak(self, s, wordDict):
        queue = deque([0])
        visited = set()  # TLE without visited (similar to memo)
        while queue:
            start = queue.popleft()
            if start in visited:
                continue
            visited.add(start)
            for i in range(start+1, len(s)+1):   # watch out index
                candidate = s[start:i]
                if candidate in wordDict:
                    if i == len(s):
                        return True
                    queue.append(i)
        
        return False



# method 1: DFS with memo m*len(wordDict)*len(word)
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = set()  # save index i which makes s[i:] not a word break 
        return self.dfs(s, 0, wordDict, memo)
    
    def dfs(self, s, start, wordDict, memo):
        if start >= len(s):
            return True
        if start in memo:
            return False
        
        for i in range(start, len(s)):
            if s[start:i+1] in wordDict and self.dfs(s, i+1, wordDict, memo):
                return True
        
        memo.add(start)
        return False

    
"""
Given a non-empty string s and a dictionary wordDict containing a list of 
non-empty words, determine if s can be segmented into a space-separated 
sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple 
pen apple".Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
