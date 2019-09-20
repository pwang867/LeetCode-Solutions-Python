# use two heaps: O(n*log(n)) in worst case
# ref: https://leetcode.com/problems/sliding-window-median/
# discuss/262689/Python-Small-and-Large-Heaps
import heapq
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        small = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(small)
        large = []
        for _ in range((k+1)//2):  # make len(large) >= len(small)
            self.move(small, large)
        
        res = [self.getMedian(small, large, k)]
        for i, num in enumerate(nums[k:]):
            if num < large[0][0]:
                heapq.heappush(small, (-num, i+k))
                if nums[i] >= large[0][0]:
                    self.move(small, large)
            else:
                heapq.heappush(large, (num, i+k))
                if nums[i] <= large[0][0]:  # mistake: if nums[i] <= large[0][0]
                    self.move(large, small)
            # only clear the value in the heap top
            # the number of values in the window are 
            # equally distributed between the two heaps
            # but the values outside the window might still exist in the window
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            res.append(self.getMedian(small, large, k))
        
        return res
      
            
    def move(self, heap1, heap2):
        # pop one element out from heap1, and push it into heap2
        num, i = heapq.heappop(heap1)
        heapq.heappush(heap2, (-num, i))
    
    
    def getMedian(self, small, large, k):
        if k%2 == 0:
            return (-small[0][0] + large[0][0])/2.0
        else:
            return large[0][0]
    
    
    
