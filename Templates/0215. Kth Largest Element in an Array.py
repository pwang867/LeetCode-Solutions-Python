# quick selection, using iteration instead of recursion, optimize space to O(1)
# time O(n)

# ask: the k-th unique number, or the k-th number


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k + 1    # change the problem to "find k-th smallest"
        left, right = 0, len(nums) - 1
        while left < right:
            mid = self.partition(nums, left, right)
            if mid + 1 == k:
                return nums[mid]
            elif mid + 1 > k:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]

    def partition(self, nums, left, right):
        if left > right:
            raise ValueError("left should be no larger than right")
        if left == right:
            return left
        pivot = nums[right]
        i, j = left, right - 1
        while i <= j:
            if nums[i] <= pivot:
                i += 1
            elif nums[j] > pivot:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        nums[i], nums[right] = nums[right], nums[i]
        return i


# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# method 3: quick selection, time O(n)
# quick selection, O(n) time, O(recursion depth) space


# Standard quick selection
# time: average O(n) with random shuffle, space O(depth)=average O(log(n))


import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)   # to make time complexity of O(n) more possible
        return self.findKthSmallest(nums, 0, len(nums)-1, len(nums)-k+1)
    
    def findKthSmallest(self, nums, left, right, k):
        mid = self.partition(nums, left, right)
        if mid-left+1 == k:
            return nums[mid]
        elif mid-left+1 > k:
            return self.findKthSmallest(nums, left, mid-1, k)
        else:
            return self.findKthSmallest(nums, mid+1, right, k-(mid-left+1))
    
    def partition(self, nums, left, right):
        pivot = nums[right]
        mid = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[mid], nums[j] = nums[j], nums[mid]
                mid += 1
        nums[mid], nums[right] = nums[right], nums[mid]
        return mid


# method 2: time: O(k+(n-k)*log(k)), space: O(k) of the min heap


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
You may assume k is always valid, 1 <= k <= array's length.
"""
