# method 2: save the last index j in nums2 for every index i in nums1
# time O(k*log(k)), space O(k)
import heapq
class Solution2(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        
        heap = []
        for i in range(min(len(nums1), k)):
            heap.append((nums1[i]+nums2[0], i, 0))
        
        res = []
        while heap and k > 0:
            val, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j+1 < len(nums2):  # mistake: j < len(nums2)
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            k -= 1
        
        return res


# method 1, use a max heap (min heap storing -val)
# time O(k*k*log(k)), space O(k)
import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for u in nums1:
            for v in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-u-v, u, v))
                elif -u-v > heap[0][0]:  # mistake: -u-v > heap[0]
                    heapq.heappushpop(heap, (-u-v, u, v))
                else:
                    break  # early termination, save time
        
        return [[u,v] for s, u, v in heap]
    
