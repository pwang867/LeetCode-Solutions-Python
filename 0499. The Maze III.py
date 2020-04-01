# BFS
# index is easy to be wrong
from collections import deque


class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        if not maze or not maze[0]:
            return ""
        queue = deque([])  # store (i, j, path, idir)
        dirs = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
        m, n = len(maze), len(maze[0])
        visited = [[0] * n for _ in range(m)]    # 4-bit integer
        for i in range(len(dirs)):
            dx, dy, c = dirs[i]
            p, q = ball[0] + dx, ball[1] + dy
            if 0 <= p < m and 0 <= q < n and maze[p][q] == 0:  # this is easy to forget
                queue.append([ball[0], ball[1], c, i])
                visited[ball[0]][ball[1]] |= 1 << i
        while queue:
            i, j, path, idir = queue.popleft()
            if [i, j] == hole:
                return path
            p, q = i + dirs[idir][0], j + dirs[idir][1]
            if p < 0 or p >= m or q < 0 or q >= n or maze[p][q] == 1:  # change direction
                for k in range(4):
                    # if visited[i][j]&(1<<k) == 0: continue   # adding this sentence is a mistake !!!  nodes in same level might be affecting each other
                    visited[i][j] |= 1 << k
                    p, q = i + dirs[k][0], j + dirs[k][1]
                    if 0 <= p < m and 0 <= q < n and maze[p][q] == 0 and visited[p][q] & (1 << k) == 0:
                        visited[p][q] |= 1 << k
                        queue.append((p, q, path + dirs[k][2], k))
            else:  # continue walk
                if (visited[p][q] & (1 << idir)) == 0:  # this condition is easy to be wrong
                    visited[p][q] |= 1 << idir
                    queue.append((p, q, path, idir))
        return "impossible"


"""
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and the hole coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.

 

Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.
Accepted
"""
