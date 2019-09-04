# method 4, use DFS to save space
from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        self.memo = defaultdict(list)
        self.memo[len(s)] = [""]  # {i:[sentences of s[i:]]}
        
        self.dfs(s, 0, wordDict)
        return self.memo[0]
    
    def dfs(self, s, start, wordDict):
        if start in self.memo:
            return self.memo[start]
        
        for i in range(start, len(s)):
            candidate = s[start:i+1]
            if candidate in wordDict:
                temp = self.dfs(s, i+1, wordDict)
                for sentence in temp:
                    if sentence:
                        self.memo[start].append(candidate + " " + sentence)
                    else:
                        self.memo[start].append(candidate)
        
        return self.memo[start]


# method 3: based on method 2
# Time limit exceeded (TLE)
# dp[i] is a list of index_sequence using s[:i]
# time/space complexity is reduced to O(n*n*L) to O(n*min(n,W)*L), 
# where W is word length, L is the wordDict length

class Solution3(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [[] for _ in range(n+1)]  # a list of a list of index_seq
        dp[0] = [[]]  # don't forget
        
        m = 0
        for word in wordDict:
            m = max(m, len(word))
        
        # generate index sequence using dp
        for i in range(1, n+1):  # index of dp
            for j in range(i, max(0,i-m), -1):
                candidate = s[j-1:i]
                if candidate in wordDict:
                    for index_seq in dp[j-1]:
                        dp[i].append(index_seq + [j-1])
        
        # use index sequence to create sentences
        res = []
        for seq in dp[-1]:
            word_list = []
            for i in range(len(seq)-1):
                word_list.append(s[seq[i]:seq[i+1]])
            word_list.append(s[seq[-1]:])
            res.append(" ".join(word_list))
        
        return res
        

# method 2: dp[i] is a list of index_sequence using s[:i]
# TLE
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [[] for _ in range(n+1)]  # a list of a list of index_seq
        dp[0] = [[]]  # don't forget
        
        m = 0
        for word in wordDict:
            m = max(m, len(word))
        
        # generate index sequence using dp
        for i in range(1, n+1):  # index of dp
            for j in range(i, max(0,i-m), -1):
                candidate = s[j-1:i]
                if candidate in wordDict:
                    for index_seq in dp[j-1]:
                        dp[i].append(index_seq + [j-1])
        
        # use index sequence to create sentences
        res = []
        for seq in dp[-1]:
            word_list = []
            for i in range(len(seq)-1):
                word_list.append(s[seq[i]:seq[i+1]])
            word_list.append(s[seq[-1]:])
            res.append(" ".join(word_list))
        
        return res
        

# method 1: dp[i] is a list of sentences using s[:i]
# memory limit exceeded
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [[] for _ in range(n+1)]  # a list of a list of sentences
        dp[0] = [""]
        
        for i in range(1, n+1):  # index of dp
            for j in range(i, 0, -1):
                candidate = s[j-1:i]
                if candidate in wordDict:
                    for sentence in dp[j-1]:
                        if i == n:
                            dp[i].append(sentence + candidate)
                        else:
                            dp[i].append(sentence + candidate + " ")
        
        return dp[-1]
        
