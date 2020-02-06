# time O(m*n), space in place O(1)
# use two bit integer to represent the next_state and cur_state
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                cnt = self.countLiveNeighbors(board, i, j)
                # modify board[i][j] to 2-bit, (next_state) + (cur_state)
                if board[i][j]:
                    if cnt == 2 or cnt == 3:
                        board[i][j] = 3  # 3 = 0b11, "11" means live to live
                else:
                    if cnt == 3:
                        board[i][j] = 2  # dead to live
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]//2
        
    def countLiveNeighbors(self, board, i, j):
        # count live neighbors
        cnt = 0
        for v in [(0,1),(0,-1),(1,0),(-1,0), (1, 1), (1,-1), (-1,1), (-1,-1)]:
            p, q = i + v[0], j + v[1]
            if 0 <= p < len(board) and 0 <= q  < len(board[0]) and (board[p][q]%2):
                cnt += 1
        return cnt    
        

# follow up: to simulate infinite board, we can use symmetry to deal with the boundary cells

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""
