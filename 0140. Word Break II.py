# method 4, use DFS to save space, otherwise memory out of limit

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset = set(wordDict)
        self.memo = {len(s): [""]}  # {i: [sentences for s[i:]]}
        return self.dfs(s, 0, wordset)
    
    def dfs(self, s, start, wordset):
        if start in self.memo:
            return self.memo[start]
        sentences = []
        for i in range(start, len(s)):
            word = s[start:i+1]
            if word in wordset:
                subsentences = self.dfs(s, i+1, wordset)
                for subsentence in subsentences:
                    if subsentence:
                        sentences.append(word + " " + subsentence)
                    else:
                        sentences.append(word)
        self.memo[start] = sentences
        return sentences
    

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


"""
Given a non-empty string s and a dictionary wordDict containing a list 
of non-empty words, add spaces in s to construct a sentence where 
each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
