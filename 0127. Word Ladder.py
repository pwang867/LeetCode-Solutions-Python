# BFS, time: O(m*n*26), space O(m), where m = len(wordList), n = len(word)
from collections import defaultdict, deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        generic = self.buildMap(wordList)
        visited = set()
        queue = deque([beginWord])
        depth = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word in visited:
                    continue
                visited.add(word)
                if word == endWord:
                    return depth
                neighbors = self.getNeighbors(word, generic)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
            depth += 1
        return 0
    
    def buildMap(self, wordList):
        generic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*"  + word[i+1:]
                generic[pattern].append(word)
        return generic
    
    def getNeighbors(self, word, generic):
        res = []
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            res.extend(generic[pattern])
        return res
   
     
"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, 
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
