class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        size = {}
        num_islands = 0
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            p, q = find(u), find(v)
            if p != q:
                if size[p] < size[q]:
                    p, q = q, p
                parent[q] = p
                size[p] += size[q]
                return True
            else:
                return False
        res = []
        for pos in positions:
            pos = tuple(pos)
            if pos not in parent:  # watch out for duplicates
                parent[pos] = pos
                size[pos] = 1
                num_islands += 1
                for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    x, y = pos[0] + dx, pos[1] + dy
                    nei = (x, y)
                    if nei in parent and union(pos, nei):
                        num_islands -= 1
                        # break  # mistake, can not break here, one extra land can reduce num_island at most by 3
            res.append(num_islands)
        return res


"""
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""

