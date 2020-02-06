# timeO(n^2), can be improved to O(n) by grouping along row or column first

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones or not stones[0]:
            return 0
        stones = map(tuple, stones)
        parent = {stone: stone for stone in stones}
        size = {stone: 1 for stone in stones}
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
            return False
        # the for loops can be optimized to improve the time from O(n^2) to O(n)
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(stones[i], stones[j])
        for stone in stones:
            find(stone)
        return len(stones) - len(set(parent.values()))


"""
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
Accepted
"""
