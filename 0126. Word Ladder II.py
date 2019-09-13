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
        
