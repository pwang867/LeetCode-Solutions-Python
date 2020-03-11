# method 2, heap sort, O(n*log(n))


class Solution2(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)

        def heapify(nums, n, i):  # implementing a max heap
            # heapify nums[:n] starting from nums[i]
            left, right = 2 * i + 1, 2 * i + 2  # children of nums[i]
            largest = i
            if left < n and nums[left] > nums[i]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        for i in range(N - 1, -1, -1):
            heapify(nums, N, i)
        for i in range(N - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)
        return nums


# use quicksort, in place sort, worst O(n^2), average O(n*log(n))
# quick sort


class Solution1(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, left, right):
        if left >= right:
            return
        i, j = left, right
        pivot = right
        right -= 1
        while left <= right:
            if nums[left] <= nums[pivot]:
                left += 1
            elif nums[right] >= nums[pivot]:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        nums[pivot], nums[left] = nums[left], nums[pivot]
        self.quicksort(nums, i, left - 1)
        self.quicksort(nums, left + 1, j)


"""
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
"""

