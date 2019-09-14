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
                    if self.helper(board, word, board[i][j], used, i, j):
                        return True
                    used[i][j] = False
        return False
    
    def helper(self, board, word, path, used, i, j):
        # path includes board[i][j], used includes [i][j]
        if len(path) == len(word):
            return True
        for v in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            p, q = i + v[0], j + v[1]
            if 0 <= p < len(board) and 0 <= q < len(board[0]) \
                and (not used[p][q]) and word[len(path)] == board[p][q]:
                used[p][q] = True
                if self.helper(board, word, path + board[p][q], used, p, q):
                    return True
                else:
                    used[p][q] = False
        return False
    
