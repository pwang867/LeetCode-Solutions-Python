# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# method 3: quick selection, time O(n)
class Solution3(object):
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
        
        # move numbers that are smaller than nums[pivot] into the front
        pivot = 0
        ref = nums[-1]
        for i in range(len(nums)):  
            if nums[i] <= ref:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                pivot += 1
        pivot -= 1
        
        if len(nums) - pivot == k:
            return nums[pivot]
        elif len(nums) - pivot > k:  # throw half of the array each time
            return self.findKthLargest(nums[pivot+1:], k)
        else:
            return self.findKthLargest(nums[:pivot], k - len(nums) + pivot)
        
        

# method 2: time: O(k+(n-k)*log(k)), space: O(k) of the min heap
import heapq
class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
                # heapq.heappop(heap)
                # heapq.heappush(heap, nums[i])
        return heap[0]


# method 1: use python built-in heapq
# and its builtin functions: heapq.nlargest(), heapq.nsmallest().
# time: O(n+k*log(n)), space: O(n) for a heap
import heapq
class Solution1(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums):
            return -1
        heapq.heapify(nums)  # O(n)
        klargest = heapq.nlargest(k, nums)  # O(k*log(n))
        return klargest[-1]




"""
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
