# BFS, sort, time complexity O(m*n)

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest or not forest[0]:
            return 0
        m, n = len(forest), len(forest[0])
        
        # get all trees and sort trees by height
        trees = [(0,0,-1)]  # to make (0, 0) always as a start point
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 0:
                    trees.append((i, j, forest[i][j]))
        trees = sorted(trees, key=lambda x: x[-1])
        
        # cut trees
        cnt = 0
        for i in range(len(trees)-1):
            start = trees[i]
            end = trees[i+1]
            visited = [[False for j in range(n)] for i in range(m)]
            visited[start[0]][start[1]] = True
            steps = self.bfs(forest, visited, start[:2], end[:2])
            if steps == -1:
                return -1
            cnt += steps
        
        return cnt
    
    def bfs(self, forest, visited, start, end):
        # level order traversal
        # find number of moves needed to move from start to end
        if end == start:
            return 0
        
        stack = [start]
        level = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while stack:
            level += 1
            new_stack = []
            for i, j in stack:
                for d in dirs:
                    p, q = i + d[0], j + d[1]
                    if (p, q) == end:
                        return level
                    if p >= 0 and p < len(forest) and q >= 0 \
                    and q < len(forest[0]) and not visited[p][q] and \
                    forest[p][q] > 0:
                        visited[p][q] = True
                        new_stack.append((p, q))
            stack = new_stack
        
        return -1
        
        
"""
You are asked to cut off trees in a forest for a golf event. 
The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, 
and this positive number represents the tree's height.


You are asked to cut off all the trees in this forest in the order of tree's 
height - always cut off the tree with lowest height first. And after cutting, 
the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps 
you need to walk to cut off all the trees. If you can't cut off all the trees, 
output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least 
one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree 
in (0,0) directly without walking.
 

Hint: size of the given matrix will not exceed 50x50.        
"""

