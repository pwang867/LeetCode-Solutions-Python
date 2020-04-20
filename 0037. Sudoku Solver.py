# use backtrack

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != ".":
                    self.update(board, i, j, rows, cols, boxes, board[i][j])
        self.dfs(board, 0, 0, rows, cols, boxes)

    def dfs(self, board, i, j, rows, cols, boxes):
        if i == len(board):
            return True
        if j == len(board[0]):
            return self.dfs(board, i + 1, 0, rows, cols, boxes)
        if board[i][j] != ".":
            return self.dfs(board, i, j + 1, rows, cols, boxes)
        else:
            for num in range(1, 10):
                num = str(num)
                if self.is_valid(i, j, rows, cols, boxes, num):
                    self.update(board, i, j, rows, cols, boxes, num)
                    if self.dfs(board, i, j + 1, rows, cols, boxes):
                        return True
                    else:
                        self.remove(board, i, j, rows, cols, boxes, num, ".")
            return False

    def is_valid(self, i, j, rows, cols, boxes, num):
        if num in rows[i]:
            return False
        if num in cols[j]:
            return False
        k = (i // 3) * 3 + (j // 3)
        if num in boxes[k]:
            return False
        return True

    def update(self, board, i, j, rows, cols, boxes, num):
        rows[i].add(num)
        cols[j].add(num)
        k = (i // 3) * 3 + (j // 3)
        boxes[k].add(num)
        board[i][j] = num

    def remove(self, board, i, j, rows, cols, boxes, num, copy):
        rows[i].remove(num)
        cols[j].remove(num)
        k = (i // 3) * 3 + (j // 3)
        boxes[k].remove(num)
        board[i][j] = copy


# possible improvement:
# 1. fill the empty cells with least candidates first
# 2. use extra hashmap to make validation faster. 
# rows = {row: set(nums)}, cols = {col: set(nums)}, boxes = {i:set(nums)}
# use set union() function to get candidates for (row, col)


# dfs, space O(n^2), time O(n*9^n)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # corner cases
        N = 9
        if len(board) != N and len(board[0]) != N:
            return
        
        # find cells to fill
        to_fill = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    to_fill.append((i,j))
        
        # call recursive DFS function
        self.Sudoku_DFS(board, to_fill, 0)
        
    def Sudoku_DFS(self, board, to_fill, m):
        # to_fill: list of positions to fill, (i, j)
        # m is the starting index of the unchecked items in to_fill
        if m == len(to_fill):
            return True
        
        N = 9
        i, j = to_fill[m]
        for val in range(1, N+1):
            val = str(val)
            if self.is_valid(board, i, j, val):
                board[i][j] = val
                if self.Sudoku_DFS(board, to_fill, m+1):
                    return True
                else:
                    board[i][j] = "."  # backtrack
        
        return False
    
    def is_valid(self, board, i, j, val):
        # check if it is safe to assign val to board[i][j]
        if (val in board[i][:j] or val in board[i][j+1:]):  # row
            return False
        if val in [board[m][j] for m in range(9) if m != i]:  # col
            return False
        icell, jcell = i//3*3, j//3*3  # index of topleft corner of the cell
        if val in [board[m][n] for m in range(icell, icell+3) 
                   for n in range(jcell, jcell+3) if m != i and n != j]:
            return False
        
        return True
        

"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
Accepted
"""

