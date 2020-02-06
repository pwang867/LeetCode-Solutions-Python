# method 1: backtrack, with memo
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n < 2:
            return False
        self.memo = {}
        return self.helper(s)
        
    def helper(self, s):
        if s in self.memo:
            return self.memo[s]
        
        for i in range(len(s) - 1):
            if s[i] == "+" and s[i + 1] == "+":
                new_s = s[:i] + "--" + s[i + 2:]
                if not self.helper(new_s):
                    self.memo[s] = True
                    return True
        self.memo[s] = False
        return False



# method 2: dp, game theory (too hard to understand)
# ref: https://leetcode.com/problems/flip-game-ii/discuss/73954/Theory-matters-from-Backtracking(128ms)-to-DP-(0ms)


"""
You are playing the following Flip Game with your friend: 
Given a string that contains only these two characters: + and -, 
you and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move and therefore the 
other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.
"""
