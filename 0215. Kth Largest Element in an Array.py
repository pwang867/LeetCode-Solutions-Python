# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# method 3: quick selection, time O(n)
# quick selection, O(n) time, O(1) space
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums) or k <= 0:
            return float('inf')
        return self.findKthSmallest(nums, 0, len(nums)-1, len(nums)-k+1)
    
    def findKthSmallest(self, nums, left, right, k):
        mid = self.partition(nums, left, right)
        if mid-left+1 == k:
            return nums[mid]
        if mid-left+1 > k:
            return self.findKthSmallest(nums, left, mid-1, k)
        else:
            return self.findKthSmallest(nums, mid+1, right, k-(mid-left+1))
    
    def partition(self, nums, left, right):
        
        guess = random.randint(left, right)  # randomly choose a pivot
        nums[guess], nums[right] = nums[right], nums[guess]
        
        pivot = nums[right]
        end = left  # nums[end] >= pivot
        for i in range(left, right):
            if nums[i] < pivot:
                nums[end], nums[i] = nums[i], nums[end]
                end += 1
        nums[end], nums[right] = nums[right], nums[end]
        return end
    

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
