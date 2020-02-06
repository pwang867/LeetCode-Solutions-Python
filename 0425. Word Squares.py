# use the problem using Trie and DFS backtracking

from collections import defaultdict
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words or not words[0]:
            return []
        trie = Trie()
        for word in words:
            trie.insertWord(word)
        self.res = []
        for word in words:
            self.dfs(trie, [word])
        return self.res
    
    def dfs(self, trie, path):
        if len(path) == len(path[0]):
            self.res.append(path[:])
            return
        i = len(path)
        prefix = "".join([word[i] for word in path])
        words = trie.startswith(prefix)
        for word in words:
            path.append(word)
            self.dfs(trie, path)
            path.pop()

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.words.append(word)
        node.is_word = True
    
    def startswith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return []
            else:
                node = node.children[c]
        return node.words


"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""
