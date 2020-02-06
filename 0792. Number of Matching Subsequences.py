# time m*n/26 in average
from collections import defaultdict
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        d = defaultdict(list)
        for i, word in enumerate(words):
            if word == "":
                cnt += 1
            else:
                # [i, 0], means index 0 of words[i] is to be matched
                d[word[0]].append([i, 0])  
        
        for c in S:
            candidates = d[c]
            d[c] = []
            for i, j in candidates:
                word = words[i]
                if j == len(word) - 1:
                    cnt += 1
                else:
                    d[word[j+1]].append([i, j+1])
        
        return cnt


# brute force, O(m*n), m = len(words), n = len(S), time limit exceeded
class Solution1(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def match(word):  
            # check if word is subsequence of S, two pointers
            if not word:
                return True
            if not S:
                return False
            i, j = 0, 0
            while i < len(S) and j < len(word):
                if S[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(word)
        
        return sum(map(match, words))
    

"""
Given string S and a dictionary of words words, 
find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of 
S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
Accepted
"""
