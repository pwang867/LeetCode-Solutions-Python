class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = len(words)
        
        i1, i2 = -1, -1  # index of last appearance of word1 and word2
        for i in xrange(len(words)):
            curr = words[i]
            if curr == word1:
                i1 = i
                if i2 != -1:
                    ans = min(i1 - i2, ans)  # abs(i1 - i2) is not necessary
            elif curr == word2:
                i2 = i
                if i1 != -1:
                    ans = min(i2 - i1, ans)
        return ans


"""
Given a list of words and two words word1 and word2, return the 
shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
