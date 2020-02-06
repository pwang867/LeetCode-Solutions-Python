class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        if not board or not board[0]:
            return [0, 0]
        m, n = len(board), len(board[0])
        dp = [[[0, 0] for j in range(n)] for i in range(m)]
        dp[0][0][1] = 1
        N = 10**9 + 7
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                for p, q in [(i-1, j), (i-1, j-1), (i, j-1)]:
                    if p < 0 or q < 0:
                        continue
                    if board[p][q] == "X":
                        continue
                    if dp[p][q][0] > dp[i][j][0]:
                        dp[i][j][0] = dp[p][q][0]
                        dp[i][j][1] = dp[p][q][1]
                    elif dp[p][q][0] == dp[i][j][0]:
                        dp[i][j][1] += dp[p][q][1]
                if dp[i][j][1] > 0:    # only when there is path to [i,j]
                    if "1" <= board[i][j] <= "9":
                        dp[i][j][0] += int(board[i][j])
                dp[i][j][1] %= N
        
        return dp[-1][-1]


"""
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].

 

Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]
Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]
Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]
"""
