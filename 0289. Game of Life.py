# time O(n^2), space O(1)
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        m, n = len(board), len(board[0])
        neighbors = [(0,1),(0,-1),(1,0),(-1,0), (1, 1), (1,-1), (-1,1), (-1,-1)]
        
        for i in range(m):
            for j in range(n):
                
                # count live neighbors
                cnt = 0
                for neighbor in neighbors: 
                    tempi, tempj = i + neighbor[0], j + neighbor[1]
                    if 0 <= tempi < m and 0 <= tempj  < n \
                        and (board[tempi][tempj]%2):
                        cnt += 1
                
                # modify board[i][j] to 2-bit, (next_state) + (now_state)
                if board[i][j]:
                    if cnt == 2 or cnt == 3:
                        board[i][j] = 3  # 3 = 0b11, "11" means live to live
                else:
                    if cnt == 3:
                        board[i][j] = 2  # dead to live
        
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j]//2
        
        
                        
        
