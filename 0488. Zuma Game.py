"""
I tried case "RRWWRRBBRR", "WB". The test program gave the expected answer -1. However, I thought the answer might be 2. Because:

RRWWRRBBRR -> RRWWRRBBR[W]R -> RRWWRRBB[B]RWR -> RRWWRRRWR -> RRWWWR -> RRR -> empty
"""


# this solution is greedy, and is incorrect in the above test case
from collections import Counter
from copy import deepcopy

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        board = self.board2pairs(board)   # to a list of pairs (ball, cnt)
        hand = Counter(hand)   # to a counter
        self.res = float('inf')
        self.dfs(board, hand, 0)
        return self.res if self.res != float('inf') else -1
    
    def dfs(self, board, hand, steps):
        if not board:
            self.res = min(self.res, steps)
            return
        if not hand or steps >= self.res:
            return
        for i in range(len(board)):
            ball, cnt = board[i]
            if ball in hand and hand[ball] > 0:
                new_board = self.get_new_board(deepcopy(board), i)
                hand[ball] -= 1
                self.dfs(new_board, hand, steps+1)
                hand[ball] += 1
    
    def get_new_board(self, board, i):
        # add 1 to board[i] and then remove balls if possible
        board[i][1] += 1
        if board[i][1] < 3:
            return board
        else:
            # remove balls
            left, right = i-1, i+1
            while left >= 0 and right < len(board):
                if board[left][0] == board[right][0] \
                and board[left][1] + board[right][1] >= 3:
                    left, right = left - 1, right + 1
                else:
                    break
            # merge same color though can not remove
            if left >= 0 and right < len(board) \
            and board[left][0] == board[right][0]:
                board[left][1] += board[right][1]
                right += 1
            # create new board
            res = []
            if left >= 0:
                res += board[:left+1]
            if right < len(board):
                res += board[right:]
            return res
    
    def board2pairs(self, board):
        stack = []    # [ball, count]
        for c in board:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
        return stack
    

"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
Accepted
11,986
Submissions
29,673
"""

