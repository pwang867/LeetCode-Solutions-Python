# method 3: similar to linked list cycle
# doing p = nums[p] is similar to p = p.next
# so we need to find the cross point of the cycle
# time O(n), space O(1)
class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow
    

# method 2, use a set to store visited numbers
# time O(n), space O(n)
class Solution2(object):
    def findDuplicate(self, nums):
        seen = set(nums)
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
        

# method 1, binary search, O(n*log(n))
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)-1  # the boundary of duplicate
        while left + 1 < right:
            mid = (left + right)//2
            cnt = 0
            for num in nums:
                if num <= mid and num >= left:
                    cnt += 1
            if cnt <= mid-left+1:
                left = mid
            else:
                right = mid
        
        if nums.count(left) > 1:
            return left
        else:
            return right
        
    
    
    
                
