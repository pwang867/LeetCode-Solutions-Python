# time O(n), space O(1)

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        res = {}
        for queen in queens:
            v = self.findDirection(king, queen)
            if v == (0, 0):
                continue
            if v not in res:
                res[v] = queen
            elif self.findDist(king, queen) < self.findDist(king, res[v]):
                res[v] = queen
        
        return res.values()
    
    def findDist(self, king, queen):
        x = queen[0] - king[0]
        y = queen[1] - king[1]
        return x**2 + y**2
    
    def findDirection(self, king, queen):
        # x == 0 and y == 0 is not possible since only 
        # one piece is allowed in one cell
        x = queen[0] - king[0]
        y = queen[1] - king[1]
        if x == 0:
            return (0, y//abs(y))
        if y == 0:
            return (x/abs(x), 0)
        if abs(x) != abs(y):
            return (0, 0)   # can not attack
        return (x//abs(x), y//abs(y))


"""
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

 

Example 1:



Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
"""

        
