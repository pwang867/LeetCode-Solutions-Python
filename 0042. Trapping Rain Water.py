# method 2: time O(n), space O(1)
# there is no difference between using height[left] < height[right] 
# and left_max < right_max in the if-else clause, because in this problem, 
# those two conditions are equivalent, and it can be proved that at any time, 
# either height[left]==left_max or height[right] == right_max

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # method 2, 05/02/2019
        if len(height) <= 2:
            return 0
        
        n = len(height)
        left, right = 0, n-1
        left_max, right_max = height[0], height[n-1]
        ans = 0
        
        while left <= right:
            # if the following two sentences are moved inside the if-else clause
            # the index may be out of bound
            left_max = max(left_max, height[left])  
            right_max = max(right_max, height[right])
            # if height[left] <= height[right]:
            if left_max < right_max:  # both are OK
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
                
        return ans


# method 1, time O(n), space O(n)
# find the maximum height to the left and to the right of height[i]
# then the trapped water in index i will be min(left_max, right_max) - height[i]
class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        if n < 3:
            return 0
        
        # left_max[i] is the max value of height[:i+1], including height[i]
        left_max = [0]*n  
        left_max[0] = height[0]
        right_max = [0]*n
        right_max[n - 1] = height[n - 1]
        
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        
        ans = 0
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans


# method 3: less duplicate work in moving left_bound, right_bound
class Solution3(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        left, right = 0, len(height)-1
        left_bound, right_bound = height[left], height[right]
        res = 0
        while left < right:
            if left_bound <= right_bound:
                res += left_bound - height[left]
                left += 1
                left_bound = max(left_bound, height[left])
            else:
                res += right_bound - height[right]
                right -= 1
                right_bound = max(right_bound, height[right])
        return res + min(left_bound, right_bound) - height[left]
    
    
                
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
