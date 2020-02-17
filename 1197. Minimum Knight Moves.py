# due to symmetry, we will only allow the knight to move in the first quarant 
# to greatly reduce time
# time complexity O(x*y)
from collections import deque
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x, y = abs(x), abs(y)   # use symmetry
        
        queue = deque([(0,0)])
        depth = 0
        visited = {(0, 0)}
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == x and j == y:
                    return depth
                for v in [(2, 1), (2, -1), (1, 2), (-1, 2), 
                          (-2, 1), (-2, -1), (1, -2), (-1, -2)]:
                    p, q = i + v[0], j + v[1]
                    if (p, q) not in visited and p >= 0 and q >= 0:
                        visited.add((p, q))
                        queue.append((p, q))
            depth += 1
        
        
"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
"""
