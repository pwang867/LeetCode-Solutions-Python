# use binary search on the result
# time O(n*log(n) + n*long(k))
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
    
    def count(self, nums, target):
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
    
