# BFS, time O(m*n), space: in place

# only save the stopping positions, then we don't need to 
# keep track of the current directions
from collections import deque
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0] or maze[start[0]][start[1]] != 0:
            return False
        queue = deque([start])   # queue only save stopping positions
        maze[start[0]][start[1]] = 2  # mark visited stopping position nodes as 2
        while queue:
            i, j = queue.popleft()
            if [i, j] == destination:
                return True
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                p, q = i, j
                while 0 <= p + dx < len(maze) and 0 <= q + dy < len(maze[0]) \
                and maze[p+dx][q+dy] != 1:
                    p, q = p + dx, q + dy
                if maze[p][q] == 0:
                    queue.append([p, q])
                    maze[p][q] = 2
        return False


"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
Accepted
"""
