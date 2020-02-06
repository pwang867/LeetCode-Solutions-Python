# union find

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        self.parent = {}
        self.size = {}
        self.unionfind(pairs)
        for i in range(len(words1)):
            word1 = words1[i]
            word2 = words2[i]
            if word1 == word2:  # don't forget
                continue
            if word1 not in self.parent or word2 not in self.parent \
            or self.find(word1) != self.find(word2):
                return False
        return True
    
    def unionfind(self, pairs):
        for word1, word2 in pairs:
            if word1 not in self.parent:
                self.parent[word1] = word1
                self.size[word1] = 1
            if word2 not in self.parent:
                self.parent[word2] = word2
                self.size[word2] = 1
            self.union(word1, word2)
    
    def find(self, word):
        if self.parent[word] == word:
            return word
        self.parent[word] = self.find(self.parent[word])
        return self.parent[word]
    
    def union(self, word1, word2):
        parent1 = self.find(word1)
        parent2 = self.find(word2)
        if parent1 == parent2:
            return
        if self.size[parent1] > self.size[parent2]:
            parent1, parent2 = parent2, parent1
        self.parent[parent1] = parent2
        self.size[parent2] += self.size[parent1]

        

"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
