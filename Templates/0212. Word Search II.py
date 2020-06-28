# use Trie to solve this problem
# time < O(m*n*len(words)*word_length)
# space < O(len(words)*word_length) for Trie

# edge case: board = [["a"]], words=["a"]

import collections


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
        node.word = word


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []
        trie = Trie()
        for word in words:
            trie.add_word(word)
        root = trie.root
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    self.dfs(board, i, j, root.children[board[i][j]], res)
        return res

    def dfs(self, board, i, j, node, res):
        if node.is_word:
            res.append(node.word)
            # delete the used word from trie, or res needs to be a hashset
            node.is_word = False
        cur = board[i][j]
        board[i][j] = "#"  # a trick, or use visited[i][j]
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r, c = i + di, j + dj
            if 0 <= r < len(board) and 0 <= c < len(board[0]) \
                    and board[r][c] in node.children:
                self.dfs(board, r, c, node.children[board[r][c]], res)
        board[i][j] = cur


"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are 
those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
