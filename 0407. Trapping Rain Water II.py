# use a heap to record the boundary of the pool
# pop out the boundary elements one by one 
# and then push its neighbors into the heap
# each element goes in and out of the heap once, so 
# time worst case O(m*n*log(m*n)), general case O(m*n*log(m+n)) 
# space worst case O(m*n), general case O(m+n)
# depending on the max boundary of the pool, 
# where (m, n) is the dimension of heightMap


import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0] \
        or len(heightMap)==1 or len(heightMap[0])==1:
            return 0
        
        # initialize the boundary
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        heap = []
        for i in range(m):
            heap.append((heightMap[i][0], i, 0))
            heap.append((heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True
        for j in range(n):
            heap.append((heightMap[0][j], 0, j))
            heap.append((heightMap[m-1][j], m-1, j))
            visited[0][j] = True
            visited[m-1][j] = True
        heapq.heapify(heap)
        
        # process elements from shortest to highest
        vol = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                p, q = i + dx, j + dy
                if 0 <= p < m and 0 <= q < n and not visited[p][q]:
                    visited[p][q] = True    # don't forget
                    h_max = max(h, heightMap[p][q])
                    vol += h_max - heightMap[p][q]
                    heapq.heappush(heap, (h_max, p, q))
        return vol


"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, 
compute the volume of water it is able to trap after raining.

 

Note:

Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

 

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.


The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.

 



After the rain, water is trapped between the blocks. The total volume of water trapped is 4.

Accepted
"""

