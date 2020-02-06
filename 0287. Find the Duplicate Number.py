# method 4: store nums in the way that nums[i] = i+1
# time O(n), space in place O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            num = nums[i]
            if num != i + 1:
                if nums[num-1] == num:
                    return num
                else:
                    nums[i], nums[num-1] = nums[num-1], nums[i]
            else:
                i += 1
        


# method 3: similar to linked list cycle, regard the index as the node
# doing p = nums[p] is similar to p = p.next
# so we need to find the cross point of the cycle
# time O(n), space O(1)
class Solution3(object):
    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[nums[0]]  # mistake: 0, nums[nums[0]]
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
        

# method 1, binary search the target, time O(n*log(n)), space O(1)
class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)-1  # the boundary of the value of the duplicate
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


"""
Given an array nums containing n + 1 integers 
where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3
"""

