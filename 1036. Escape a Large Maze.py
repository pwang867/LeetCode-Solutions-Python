# we only need to prove that there is no loop of blocks enclosing
# the source and target, so we need to do BFS twice.
# If the BFS depth is larger than len(blocked), then it means the source
# is not in the loop

# because maze size is much much larger than len(blocks)

from collections import deque
class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        blocked = map(tuple, blocked)  # list is not hashable
        blocked = set(blocked)  # don't forget !
        source = tuple(source)
        target = tuple(target)
        if not blocked: return True
        if target in blocked or source in blocked:
            return False
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)
    
    def bfs(self, blocked, source, target):
        queue = deque([source])
        visited = set([source])
        seen_block = set()
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) == target:
                    return True
                for v in ((0, 1), (0,-1), (1,0), (-1,0)):
                    p, q = i+v[0], j+v[1]
                    if (p, q) in blocked:
                        seen_block.add((p, q))
                        continue
                    if p >= 0 and q >= 0 and (p, q) not in visited:
                        queue.append((p, q))
                        visited.add((p, q))
            if len(queue) > len(blocked) - len(seen_block):
                return True
        return False
    
    
"""
In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.

 

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: 
The target square is inaccessible starting from the source square, because we can't walk outside the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: 
Because there are no blocked cells, it's possible to reach the target square.
 

Note:

0 <= blocked.length <= 200
blocked[i].length == 2
0 <= blocked[i][j] < 10^6
source.length == target.length == 2
0 <= source[i][j], target[i][j] < 10^6
source != target
"""
