class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans = len(words)
        
        i1, i2 = -1, -1  # index of last appearance of word1 and word2
        for i, curr in enumerate(words):
            if curr == word1:
                i1 = i
                if i2 != -1:
                    ans = min(i1 - i2, ans)
            if curr == word2:  # simply change elif to if from "Shortest Word Distance."
                i2 = i
                if i1 != -1 and i2 != i1:
                    ans = min(i2 - i1, ans)
        return ans
    

"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
Note:
You may assume word1 and word2 are both in the list.
"""
