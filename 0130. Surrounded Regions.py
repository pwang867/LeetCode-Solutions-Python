# method 1: search from the boundary
# another method: be very careful if you choose to search from inside, 
# think twice for backtracking
# do two DFS: one to check if it is surronded, one to change O to X 
# if surrrounded

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        for i in range(m):
            if board[i][0] == "O":
                self.dfs(board, i, 0, visited)
            if board[i][n-1] == "O":
                self.dfs(board, i, n-1, visited)
        for j in range(n):
            if board[0][j] == "O":
                self.dfs(board, 0, j, visited)
            if board[m-1][j] == "O":
                self.dfs(board, m-1, j, visited)
        self.changeBoard(board)
    
    def dfs(self, board, i, j, visited):
        # mark all "O" to "#", meaning not surrounded
        # (i, j) is a boundary location, board[i][j] is "O"
        board[i][j] = "#"
        visited[i][j] = True
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            p, q = i + dx, j + dy
            if 0 <= p < len(board) and 0 <= q < len(board[0]) \
            and board[p][q] == "O" and not visited[p][q]:
                self.dfs(board, p, q, visited)
        visited[i][j] = False
        
    
    def changeBoard(self, board):
        # change "O" to "X"
        # change "#" (not surrounded "O") back to "O"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions 
surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
