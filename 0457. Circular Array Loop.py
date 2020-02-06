# time O(n), space O(1)
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        
        for i in range(len(nums)):
            if nums[i]%len(nums) == 0:
                continue
            # first pass: search circle
            j = i
            cnt = 0
            while nums[j]*nums[i] > 0:
                cnt += 1
                if cnt > len(nums):
                    return True
                nextj = (len(nums) + j + nums[j])%len(nums)
                # easy to forget, A cycle must start and end at the same index and the cycle's length > 1
                if nextj == j:   
                    break
                else:
                    j = nextj
            # second pass: mark current path as 0
            k = i
            while k != j:
                nextk = (len(nums) + k + nums[k])%len(nums)
                nums[k] = 0
                k = nextk
        return False


# time O(n), space O(n)
class Solution1(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        visited = [False]*len(nums)
        for i in range(len(nums)):
            if visited[i] or nums[i]%len(nums) == 0:
                continue
            j = i
            path = set()   # record current path/circle only
            while nums[j]*nums[i] > 0:
                if j in path:
                    return True
                path.add(j)
                visited[j] = True
                nextj = (len(nums) + j + nums[j])%len(nums)
                # easy to forget, A cycle must start and end at the same index and the cycle's length > 1
                if nextj == j:   
                    break
                else:
                    j = nextj
                
        return False


"""
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.

 

Example 1:

Input: [2,-1,1,2,2]
Output: true
Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's length is 3.
Example 2:

Input: [-1,2]
Output: false
Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because the cycle's length is 1. By definition the cycle's length must be greater than 1.
Example 3:

Input: [-2,1,-1,-2,-2]
Output: false
Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle, because movement from index 1 -> 2 is a forward movement, but movement from index 2 -> 1 is a backward movement. All movements in a cycle must follow a single direction.
 

Note:

-1000 ≤ nums[i] ≤ 1000
nums[i] ≠ 0
1 ≤ nums.length ≤ 5000
 

Follow up:

Could you solve it in O(n) time complexity and O(1) extra space complexity?
"""
