# DFS

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["."] * n for _ in range(n)]
        res = []
        cols = set()
        diag = set()
        adiag = set()
        self.dfs(board, 0, cols, diag, adiag, res)
        return res

    def dfs(self, board, i, cols, diag, adiag, res):
        if i == len(board):
            res.append(map("".join, board))
            return
        for j in range(len(board[0])):
            if j in cols or (i + j) in diag or (i - j) in adiag:
                continue
            cols.add(j)
            diag.add(i + j)
            adiag.add(i - j)
            board[i][j] = "Q"
            self.dfs(board, i + 1, cols, diag, adiag, res)
            board[i][j] = "."
            cols.remove(j)
            diag.remove(i + j)
            adiag.remove(i - j)


# DFS, don't need memorization

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # use recursion
        if n == 0:
            return []
        if n == 1:
            return [["Q"]]
        if n == 2:
            return []
        
        ans = []
        self.helper(n, [], ans)
        
        boards = []
        for _list in ans:
            board = []
            for i in range(n):
                j = _list[i]
                board.append('.'*j + 'Q' + '.'*(n-1-j))
            boards.append(board)
        return boards
        
        
    def helper(self, n, path, ans):
        if len(path) == n:
            ans.append(path + [])
            return
        for j in range(n):
            if self.isValid(n, path, j):
                path.append(j)
                self.helper(n, path, ans)
                path.pop()
    
    def isValid(self, n, path, j):
        m = len(path)
        
        # check vertical
        if j in path:
            return False
        
        # check two diagonals
        for i in range(m):
            if i + path[i] == m + j or i - path[i] == m - j:
                return False
        
        return True
        
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
