# BFS, delete newly used words after finishing each level


from collections import defaultdict


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if not wordList or endWord not in wordList:
            return []
        
        # level stores paths in the same level
        # format is {lastWord: paths ending with this word}
        level = {beginWord: [[beginWord]]}  # quicker than using a list to store all paths
        words = set()  # temporarily save newly used words in current level
        res = []
        while level:
            new_level = defaultdict(list)
            # create new paths
            for lastWord in level:
                nextWords = self.getNextWords(lastWord, wordList)
                for nextWord in nextWords:
                    if nextWord == endWord:
                        res.extend([path + [nextWord] for path in level[lastWord]])
                    else:
                        new_level[nextWord].extend(
                            [path + [nextWord] for path in level[lastWord]])
                        words.add(nextWord)
            
            # check if endWord is already found
            if res:
                return res
            
            # delete newly used words, and update variables
            for word in words:
                wordList.remove(word)
            words.clear()
            level = new_level
        
        return []
    
    def getNextWords(self, cur_word, wordList):
        res = []
        for i in range(len(cur_word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = cur_word[:i] + c + cur_word[i+1:]
                if new_word in wordList:
                    res.append(new_word)
                
        return res


"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) 
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
