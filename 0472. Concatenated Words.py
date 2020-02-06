# similar to 0140: Word Break II


# time complexity: O(N*M^M), where N is len(words), M is len(words[i])
# space O(N+M) for a wordset, and a self.visited to store index 
# time limit exceeded
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        wordset = set(words)
        res = []
        for word in words:
            if not word:  # when word is ""
                continue
            wordset.remove(word)
            self.visited = set()
            
            if self.checkConcat(word, 0, wordset):
                res.append(word)
            
            wordset.add(word)
            
        return res
    
    def checkConcat(self, word, i, words):
        # basic DFS
        if i == len(word):
            return True
        
        if i in self.visited:
            return False
        for j in range(len(word)-1, i-1, -1):
            # to search from longer substring to shorter to reduce recursion depth
            if word[i:j+1] in words and self.checkConcat(word, j+1, words):
                return True
        
        self.visited.add(i)
        return False
    
                
