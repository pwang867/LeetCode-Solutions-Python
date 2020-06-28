# standard BFS, start from all gates, time/space O(n)


from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        queue = deque()
        for i in range(len(rooms)):   # collect all gates
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            for v in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                p, q = i+v[0], j+v[1]
                if p >= 0 and p < len(rooms) and q >= 0 and q < len(rooms[0])\
                and rooms[p][q] != -1 and rooms[p][q] > rooms[i][j]+1:
                    rooms[p][q] = rooms[i][j] + 1
                    queue.append((p, q))


"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
