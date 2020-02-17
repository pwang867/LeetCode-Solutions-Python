# method 2, optimal solution, since in worst condition k=n^2
# use binary search on the result
# time O(n*log(n) + n*log(k))
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        
        left, right = 0, nums[-1] - nums[0]
        while left + 1 < right:
            mid = left + (right - left)//2
            if self.count(nums, mid) >= k:
                right = mid
            else:
                left = mid
        
        if self.count(nums, left) >= k:
            return left
        else:
            return right
    
    def count(self, nums, target):    # most interesting part
        # find the counts of pairs with distance <= target
        cnt = 0
        
        left, right = 0, 0
        while right < len(nums):
            if nums[right] - nums[left] > target:
                left += 1
            else:
                cnt += right - left  # count all pairs ending in right
                right += 1
        
        return cnt


# use a heap, initialize the heap with k-pairs: [(nums[i+1] - nums[i], i, i+1)]
# then always pop out the pair with smallest distance, and push the successor of (i, j) 
# into the heap, which is (nums[j+1]-nums[i, i, j+1)
# time (n+k)*log(n), time limit exceeded, space O(n)
import heapq
class Solution1(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums)*(len(nums)-1)/2:
            return None
        
        nums.sort()
        h = []
        for i in range(len(nums)-1): # mistake: range(k)
            h.append((nums[i+1]-nums[i], i, i+1))
        heapq.heapify(h)  # h is not ordered yet after initialization
        
        res = 0
        while h and k > 0:
            res, i, j = heapq.heappop(h)
            if j+1 < len(nums):
                heapq.heappush(h, (nums[j+1]-nums[i], i, j+1))
            k -= 1
        
        return res
    
"""
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
"""
