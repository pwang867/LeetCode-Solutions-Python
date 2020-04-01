# method 2, use Trie

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.sum = 0
        self.val = 0   # if not isWord, self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def get_word_val(self, word):
        # return the val of the word if it is a word, else 0
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.val
    
    def insert(self, key, val):
        pre_val = self.get_word_val(key)
        diff = val - pre_val
        node = self.root
        for c in key:
            node = node.children[c]
            node.sum += diff
        node.val = val
    
    def get_sum(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0   # prefix does not exist
            node = node.children[c]
        return node.sum

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.trie.insert(key, val)
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.get_sum(prefix)





# method 1: save all prefix, and save all original key-val pairs
class MapSum1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.original = {}     # must use a separate map to save all orignal key-val pairs
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        diff = val
        if key in self.original:
            diff -= self.original[key]
        self.original[key] = val
        for i in range(len(key)):
            prefix = key[:i+1]
            self.map[prefix] = self.map.get(prefix, 0) + diff
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.map.get(prefix, 0)
        
        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). 
The string represents the key and the integer represents the value. 
If the key already existed, then the original key-value pair 
will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, 
and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
Accepted
"""
