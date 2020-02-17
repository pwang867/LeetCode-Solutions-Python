# method 2: BFS, starting from "L", "R" and evolve layer by layer with time




# method 1, time/space O(n), find the closest "R" to the left, 
# and closest "L" to the right
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        if not dominoes:
            return ""
        
        n = len(dominoes)
        # left[i] is the distance from dominoes[i] to the closest "R" to its left
        left = [-1]*n  
        right = [-1]*n
        
        # find the closest "R"
        last_R = - float('inf')
        for i, c in enumerate(dominoes):
            if c == "R":
                last_R = i
            elif c == ".":
                left[i] = i - last_R
            else:  # easy to miss
                last_R = -float('inf')  
        
        # find the closest "L"
        last_L = float('inf')
        for i in range(n-1, -1, -1):
            c = dominoes[i]
            if c == "L":
                last_L = i
            elif c == ".":
                right[i] = last_L - i
            else:
                last_L = float('inf')
        
        # find final results
        res = []
        for i, c in enumerate(dominoes):
            if c != ".":
                res.append(c)
            else:
                if left[i] == right[i]:
                    res.append('.')
                elif left[i] > right[i]:
                    res.append('L')
                else:
                    res.append('R')
        
        return ''.join(res)
    
"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either 
to the left or to the right.


After each second, each domino that is falling to the left pushes 
the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes 
standing on the right.

When a vertical domino has dominoes falling on it from both sides, 
it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino 
expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', 
if the i-th domino has been pushed to the left; 
S[i] = 'R', if the i-th domino has been pushed to the right; 
S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""

