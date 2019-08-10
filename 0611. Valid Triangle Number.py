# method 2: time O(n^2), space O(1)
# search from behind, use the property that (smallest + middle < largest)
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        cnt = 0
        for i in range(len(nums)-1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1
        return cnt
        

# method 1, brute force
# time O(n*n*log(n)), space O(1)

# class Solution(object):
#     def triangleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) < 3:
#             return 0
        
#         nums.sort()
        
#         cnt = 0
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)-1):
#                 cnt += self.countTriangles(nums, i, j)
        
#         return cnt
    
#     def countTriangles(self, nums, i, j):
#         # count the number of triangles formed by nums[i], nums[j] and nums[k]
#         # where 0 <= i < j < k < len(nums)
        
#         left = j + 1
#         right = len(nums) - 1
        
#         while left <= right:
#             mid = (left + right)//2
#             if nums[mid] >= nums[i] + nums[j]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
        
#         return left - 1 - j
    
