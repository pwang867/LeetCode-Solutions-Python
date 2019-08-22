# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:59:39 2019

@author: WEIMIN ZHOU
"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        roots = [[-1]*n for _ in range(m)]  # works like a linked list
        dirs = [(1, 0), (-1,0), (0,1), (0,-1)]
        res = []
        cnt = 0
        
        for i, j in positions:
            if roots[i][j] >= 0 or i < 0 or i >= m or j < 0 or j >= n: 
                # already visited, or invalid input
                res.append(cnt)
                continue
            roots[i][j] = (i, j)
            cnt += 1
            for _dir in dirs:
                x, y = i + _dir[0], j + _dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or roots[x][y] == -1:
                    continue
                q = self.getRoot(roots, x, y)
                if q != (i, j):
                    roots[q[0]][q[1]] = (i, j)
                    cnt -= 1
            res.append(cnt)
        return res
    
    def getRoot(self, roots, x, y):
        # recursively find the root
        if roots[x][y] == (x, y):
            return (x, y)
        else:
            self.getRoot(roots, roots[x][y][0], roots[x][y][1])

print(Solution().numIslands2(3, 3, [[0,0], [0,1], [1,2], [2,1]]))
