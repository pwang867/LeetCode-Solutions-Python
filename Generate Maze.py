# coding=utf-8
"""
Generate
Maze
初始化为全部是墙【1】， 第一个位置为出口所以不是墙【0】。每次随机挑选一个方向。往前看两步，如果前面两步是墙，把前面一步和前面两步的墙拆掉。
不知道为什么能work
"""


import random

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution(object):
    def getMaze(self, m, n):
        maze = [[1] * n for _ in range(m)]
        maze[0][0] = 0

        self.generateMaze(maze, n, n, 0, 0)

        return maze

    def generateMaze(self, maze, m, n, x, y):
        direc = DIRECTIONS
        random.shuffle(direc)
        for dx, dy in direc:
            next_x, next_y = x + 2 * dx, y + 2 * dy
            if self.validWall(maze, m, n, next_x, next_y):
                maze[x + dx][y + dy] = 0
                maze[next_x][next_y] = 0
                self.generateMaze(maze, m, n, next_x, next_y)

    def validWall(self, maze, m, n, x, y):
        return 0 <= x < m and 0 <= y < n and maze[x][y]

if __name__ == "__main__":
    maze = Solution().getMaze(9, 9)
    for row in maze:
        print(row)
