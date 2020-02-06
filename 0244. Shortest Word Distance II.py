from collections import defaultdict
class WordDistance(object):
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_dict = defaultdict(list)  # word_dict = {word:[index]}
        for i in range(len(words)):
            self.word_dict[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 not in self.word_dict or word2 not in self.word_dict:
            return -1
        list1 = self.word_dict[word1]
        list2 = self.word_dict[word2]
        i, j = 0, 0
        ans = max(list1[-1], list2[-1])
        while i < len(list1) and j < len(list2):
            ans = min(ans, abs(list1[i] - list2[j]))   # can not be moved to the end of while loop
            if list1[i] < list2[j]:  # equal is not possible
                i += 1
            else:
                j += 1
        return ans


        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
        
        
"""
Design a class which receives a list of words in the constructor, 
and implements a method that takes two words word1 and word2 and return the 
shortest distance between these two words in the list. Your method will be 
called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
