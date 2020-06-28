# time/space O(m*n), BFS

import collections


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # null check
        if not A or not A[0]:
            return 0
        m, n = len(A), len(A[0])

        # get the first island idx
        queue = self.collect_first_island(A)

        # BFS search the nearest 1
        depth = 0
        visited = set(queue)
        while queue:
            print(queue)
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if A[i][j] == 1:  # found
                    return depth - 1
                for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    r, c = i + di, j + dj
                    if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))
            depth += 1
        return -1

    def collect_first_island(self, A):
        m, n = len(A), len(A[0])
        # get the first island idx
        queue = collections.deque([])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, queue)
                    return queue

    def dfs(self, A, i, j, idx):
        # collect all index of an island into a queue called idx, and mark 1 to 0
        idx.append((i, j))
        A[i][j] = 0
        for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            r, c = i + di, j + dj
            if 0 <= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == 1:
                self.dfs(A, r, c, idx)


"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally 
connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""