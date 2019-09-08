# use a heap to record the boundary of the pool
# pop out the boundary elements one by one 
# and then push its neighbors into the heap
# each element goes in and out of the heap once, so 
# time worst case O(m*n*log(m*n)), space O(m*n), 
# where (m,n) is the dimension of heightMap

import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        
        # push pool boundaries into a heap
        heap = []
        visited = set()
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited.add((0, j))
            visited.add((m-1, j))
        for i in range(1, m-1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited.add((i, 0))
            visited.add((i, n-1))
        
        vol = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for v in [(0,1),(0,-1),(-1,0),(1,0)]:
                p, q = i+v[0], j+v[1]
                # do not forget  0 <= p < m and 0 <= q < n
                if (p, q) not in visited and 0 <= p < m and 0 <= q < n:
                    h_max = max(h, heightMap[p][q])
                    heapq.heappush(heap, (h_max, p, q))  # tricky point: use h_max, not h
                    vol += h_max - heightMap[p][q]
                    visited.add((p, q))
        
        return vol
    
