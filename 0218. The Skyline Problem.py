import heapq
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort all left and right edges together with x position
        # store left and right edges differently
        edges = [(left, -height, right) for left, right, height in buildings] \
                + [(right, height, None) for left, right, height in buildings]
        edges.sort()
        
        heap = [(0, float('inf'))]  # heap stores (height, x location)
        res = []
        cur = 0  # current height
        
        for x, h, right in edges:
            if right is not None: # left edge
                heapq.heappush(heap, (h, right))  # push the right edge to the heap
                if -h > cur:
                    cur = -h
                    res.append([x, -h])
            else:
                # find the highest right edge in the current building blocks
                while heap and heap[0][1] <= x:
                    heapq.heappop(heap)
                highest = -heap[0][0]
                
                if highest < cur:  # highest can only be equal to of smaller than cur
                    # watch out edge case: [[0,2,3],[2,5,3]]
                    res.append([x, highest])
                    cur = highest
        
        return res
    
