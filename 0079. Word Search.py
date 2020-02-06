# DFS, label visited location

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        m = len(board)
        n = len(board[0])
        used = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    if self.helper(board, word, 0, used, i, j):
                        return True
                    used[i][j] = False
        return False
    
    def helper(self, board, word, k, used, i, j):
        # word[k] is already matched, used[i][j] is already processed
        if k == len(word)-1:
            return True
        for v in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            p, q = i + v[0], j + v[1]
            if 0 <= p < len(board) and 0 <= q < len(board[0]) \
                and (not used[p][q]) and word[k+1] == board[p][q]:
                used[p][q] = True
                if self.helper(board, word, k+1, used, p, q):
                    return True
                used[p][q] = False
        return False



"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

