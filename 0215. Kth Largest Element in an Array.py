# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# method 3: quick selection, O(n)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return 
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)
        
        pivot = 0
        ref = nums[-1]
        for i in range(len(nums)):
            if nums[i] <= ref:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        pivot -= 1
        
        if len(nums) - pivot == k:
            return nums[pivot]
        elif len(nums) - pivot > k:
            return self.findKthLargest(nums[pivot+1:], k)
        else:
            return self.findKthLargest(nums[:pivot], k - len(nums) + pivot)
        
        

# method 2: time: O(k+(n-k)*log(k)), space: O(k) of the min heap
# import heapq
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         heap = nums[:k]
#         heapq.heapify(heap)
#         for i in range(k, len(nums)):
#             if nums[i] > heap[0]:
#                 heapq.heappushpop(heap, nums[i])
#                 # heapq.heappop(heap)
#                 # heapq.heappush(heap, nums[i])
#         return heap[0]


# method 1: use python built in heapq
# and the builtin functions heapq.nlargest(), heapq.nsmallest()
# time: O(n+k*log(n)), space: O(n)
# import heapq
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if k > len(nums):
#             return -1
#         heapq.heapify(nums)
#         klargest = heapq.nlargest(k, nums)
#         return klargest[-1]
    
